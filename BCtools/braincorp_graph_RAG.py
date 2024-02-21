
import os
from openai import OpenAI
from retry import retry
import re
from string import Template
import json
from neo4j import GraphDatabase
import glob
from timeit import default_timer as timer
from dotenv import load_dotenv
from time import sleep
import PyPDF2
from markdownify import markdownify as md
from langchain_community.document_loaders import PyPDFLoader
import tiktoken
from langchain.text_splitter import CharacterTextSplitter

client = OpenAI()
load_dotenv()

neo4j_url = "neo4j+ssc://cb9f7470.databases.neo4j.io:7687"
neo4j_user = "neo4j"
neo4j_password = "UECDV_L6miPn1p6Ipwnus3-G-Yru-Ds_xeQgYJ2RnnE"
gpt4_model = "gpt-4-0125-preview"
gpt35_model = "gpt-3.5-turbo-16k"
gds = GraphDatabase.driver(neo4j_url,auth=(neo4j_user, neo4j_password))

def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string))
    return num_tokens

def callGPT(file_prompt,system_msg):
    response = client.chat.completions.create(
        model= gpt4_model,
        max_tokens=4096,
        temperature=0,
        messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": file_prompt},
      ]
    )
    answer=response.choices[0].message.content
    answer = answer.replace('```json','').replace("```","")
    return answer

def graphGPT(folder,prompt_template):
    start = timer()
    files = glob.glob(f"C:/Users/korn2/Desktop/BCtools/data/{folder}/*")
    print(f"running pipelines for {len(files)} for files in {folder} folder")
    system_msg = "You are a helpful IT-project and account management expert who extracts information from documents."
    results = []
    
    for i, file in enumerate(files):
        print(f"Extracting entities and relationships for {file}")
        try:
            with open(file, "r", encoding='utf-8') as f:
                text = f.read().rstrip()
                print("here text")
                prompt = Template(prompt_template).substitute(ctext=text)
                print("here prompt")
                result = callGPT(prompt,system_msg)
                print(f"generated_resp {result}")
                results.append(json.loads(result))
        except Exception as e:
            print(f"Error processing {file}: {e}")
    end = timer()
    print(f"Pipeline completed in {end-start} seconds")
    return results


# Function to take a json-object of entitites and relationships and generate cypher query for creating those entities
def generate_cypher(json_obj):
    e_statements = []
    r_statements = []

    e_label_map = {}

    # loop through our json object
    for i, obj in enumerate(json_obj):
        print(f"Generating cypher for file {i+1} of {len(json_obj)}")
        for entity in obj["entities"]:
            label = entity["label"]
            id = entity["id"]
            id = id.replace("-", "").replace("_", "")
            properties = {k: v for k, v in entity.items() if k not in ["label", "id"]}

            cypher = f'MERGE (n:{label} {{id: "{id}"}})'
            if properties:
                props_str = ", ".join(
                    [f'n.{key} = "{val}"' for key, val in properties.items()]
                )
                cypher += f" ON CREATE SET {props_str}"
            e_statements.append(cypher)
            e_label_map[id] = label

        for rs in obj["relationships"]:
            src_id, rs_type, tgt_id = rs.split("|")
            src_id = src_id.replace("-", "").replace("_", "")
            tgt_id = tgt_id.replace("-", "").replace("_", "")

            src_label = e_label_map[src_id]
            tgt_label = e_label_map[tgt_id]

            cypher = f'MERGE (a:{src_label} {{id: "{src_id}"}}) MERGE (b:{tgt_label} {{id: "{tgt_id}"}}) MERGE (a)-[:{rs_type}]->(b)'
            r_statements.append(cypher)

    with open("cyphers.txt", "w") as outfile:
        outfile.write("\n".join(e_statements + r_statements))

    return e_statements + r_statements

# Final function to bring all the steps together
def ingestion_pipeline(folders):
    # Extrating the entites and relationships from each folder, append into one json_object
    for key, value in folders.items():
        result = graphGPT(key, value)
        with open("C:/Users/korn2/Desktop/BCtools/test.json","w") as f:
            json.dump(result,f)
    print(result)
    # Generate and execute cypher statements
    with open('C:/Users/korn2/Desktop/BCtools/test.json' , "r") as f:
        json_obj = json.load(f)
    cypher = generate_cypher(json_obj)
    for i, stmt in enumerate(cypher):
        print(f"Executing cypher statement {i+1} of {len(cypher)}")
        try:
            print(stmt)
            gds.execute_query(stmt)
        except Exception as e:
            with open("C:/Users/korn2/Desktop/BCtools/failed_statements.txt", "w") as f:
                f.write(f"{stmt} - Exception: {e}\n")


project_prompt_template = """
From the Project Brief below, extract the following Entities & relationships described in the mentioned format 
0. ALWAYS FINISH THE OUTPUT. Never send partial responses
1. First, look for these Entity types in the text and generate as comma-separated format similar to entity type.
   `id` property of each entity must be alphanumeric and must be unique among the entities. You will be referring this property to define the relationship between entities. Do not create new entity types that aren't mentioned below. Document must be summarized and stored inside Project entity under `summary` property. You will have to generate as many entities as needed as per the types below:
    Entity Types:
    label:'Project',id:string,name:string;summary:string //Project mentioned in the brief; `id` property is the full name of the project, in lowercase, with no capital letters, special characters, spaces or hyphens; Contents of original document must be summarized inside 'summary' property
    label:'Technology',id:string,name:string //Technology Entity; `id` property is the name of the technology, in camel-case. Identify as many of the technologies used as possible
    label:'Client',id:string,name:string;industry:string //Client that the project was done for; `id` property is the name of the Client, in camel-case; 'industry' is the industry that the client operates in, as mentioned in the project brief.
    
2. Next generate each relationships as triples of head, relationship and tail. To refer the head and tail entity, use their respective `id` property. Relationship property should be mentioned within brackets as comma-separated. They should follow these relationship types below. You will have to generate as many relationships as needed as defined below:
    Relationship types:
    project|USES_TECH|technology 
    project|HAS_CLIENT|client


3. The output should look like :
{
    "entities": [{"label":"Project","id":string,"name":string,"summary":string}],
    "relationships": ["projectid|USES_TECH|technologyid"]
}

Case Sheet:
$ctext
"""

research_paper_prompt_template = """From the list of research papers below, extract the following Entities & relationships in the mentioned format
0. ALWAYS FINISH THE OUTPUT. Never send partial responses

1. First, look for these Entity types in the text and generate as comma-separated format similar to entity type.
    `id` property of each entity must be alphanumeric and must be unique among the entities. You will be referring this property to define the relationship between entities. Do not create new entity types that aren't mentioned below. You will have to generate as many entities as needed as per the types below:
    start by creating the paper entity, corresponding to the actual paper you are reading.
    Entity Types:
    label:'Author',id:string,name:string //Author of the research paper. id property is the author's last name in camel-case. 'name' is the full name of the author, as spelled in the text.
    label:'Paper',id:string,title:string;abstract:string //Research Paper; id property is the first five words of the title, in lowercase with no special characters or spaces.
    label:'Institution',id:string,name:string //Institution affiliated with the research; id property is the name of the institution, in camel-case.
    label:'Concept',id:string,name:string //Key concept or technology discussed in the paper; id property is the name of the concept, in camel-case.

Next generate each relationships as triples of head, relationship and tail. To refer the head and tail entity, use their respective id property. Relationship property should be mentioned within brackets as comma-separated. They should follow these relationship types below. Never ever use tail or head that you didn't defined as entities. You cannot use a id that is not defined as entities before. You will have to generate as many relationships as needed as defined below:
Relationship types:
author|WRITES|paper
paper|DISCUSSES|concept
author|AFFILIATED_WITH|institution
paper|CITES|paper

The output should look like :
{
    "entities": [{"label":"Author","id":string,"name":string}],
    "relationships": ["authorid|WRITES|paperid"]
}

You absolutly need to create a paper label, the title of the actual paper is : organoid intelligence. Otherwise you cannot refer to paper in relationships.
Case Sheet:
$ctext
"""

# Prompt for processing peoples' profiles
people_prompt_template = """From the list of people below, extract the following Entities & relationships described in the mentioned format 
0. ALWAYS FINISH THE OUTPUT. Never send partial responses
1. First, look for these Entity types in the text and generate as comma-separated format similar to entity type.
   `id` property of each entity must be alphanumeric and must be unique among the entities. You will be referring this property to define the relationship between entities. Do not create new entity types that aren't mentioned below. You will have to generate as many entities as needed as per the types below:
    Entity Types:
    label:'Person',id:string,name:string //Person that the data is about. `id` property is the name of the person, in camel-case. 'name' is the person's name, as spelled in the text.
    label:'Project',id:string,name:string;summary:string //Project mentioned in the profile; `id` property is the full lowercase name of the project, with no capital letters, special characters, spaces or hyphens.
    label:'Technology',id:string,name:string //Technology Entity, as listed in the "skills"-section of every person; `id` property is the name of the technology, in camel-case.
    
3. Next generate each relationships as triples of head, relationship and tail. To refer the head and tail entity, use their respective `id` property. Relationship property should be mentioned within brackets as comma-separated. They should follow these relationship types below. You will have to generate as many relationships as needed as defined below:
    Relationship types:
    person|HAS_SKILLS|technology 
    project|HAS_PEOPLE|person


The output should look like :
{
    "entities": [{"label":"Person","id":string,"name":string}],
    "relationships": ["projectid|HAS_PEOPLE|personid"]
}

Case Sheet:
$ctext
"""

# Prompt for processing slack messages

slack_prompt_template = """
From the list of messages below, extract the following Entities & relationships described in the mentioned format 
0. ALWAYS FINISH THE OUTPUT. Never send partial responses
1. First, look for these Entity types in the text and generate as comma-separated format similar to entity type.
   `id` property of each entity must be alphanumeric and must be unique among the entities. You will be referring this property to define the relationship between entities. Do not create new entity types that aren't mentioned below. You will have to generate as many entities as needed as per the types below:
    Entity Types:
    label:'Person',id:string,name:string //Person that sent the message. `id` property is the name of the person, in camel-case; for example, "michaelClark", or "emmaMartinez"; 'name' is the person's name, as spelled in the text.
    label:'SlackMessage',id:string,text:string //The Slack-Message that was sent; 'id' property should be the message id, as spelled in the reference. 'text' property is the text content of the message, as spelled in the reference
    
3. Next generate each relationships as triples of head, relationship and tail. To refer the head and tail entity, use their respective `id` property. Relationship property should be mentioned within brackets as comma-separated. They should follow these relationship types below. You will have to generate as many relationships as needed as defined below:
    Relationship types:
    personid|SENT|slackmessageid

The output should look like :
```json
{
    "entities": [{"label":"SlackMessage","id":string,"text":string}],
    "relationships": ["personid|SENT|messageid"]
}
```
Case Sheet:
$ctext
"""



folders = {
    "people_profiles": research_paper_prompt_template,
    }


ingestion_pipeline(folders)
"""
def ingestion
# Load the PDF
loader = PyPDFLoader("C:/Users/korn2/Desktop/BCtools/orga.pdf")
pages = loader.load()

# Initialize variables
MAX_TOKENS = 6000
current_tokens = 0
temp_content = ""
file_count = 1

for page in pages:
    page_content = page.page_content
    tokens_in_page = num_tokens_from_string(page_content)
    
    # Check if adding this page exceeds the max token limit
    if current_tokens + tokens_in_page > MAX_TOKENS:
        # Save the current content to a markdown file
        with open(f"C:/Users/korn2/Desktop/BCtools/output_{file_count}.md", "w", encoding="utf-8") as file:
            file.write(temp_content)
        file_count += 1
        temp_content = page_content
        current_tokens = tokens_in_page
    else:
        temp_content += "\n\n" + page_content
        current_tokens += tokens_in_page

# Save the last part if there's any content left
if temp_content:
    with open(f"C:/Users/korn2/Desktop/BCtools/output_{file_count}.md", "w", encoding="utf-8") as file:
        file.write(temp_content)

print(f"Processed {file_count} files.")
"""

