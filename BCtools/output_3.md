a relevant technique, a fundamentally different approach to neuron
behavior mapping was developed in Drosophila :o p t o g e n e t i c
activation of neurons and the application of multiscale
unsupervised structure learning methods to the recorded responses
to identify discrete, statistically distinguishable, observer-unbiased
response phenotypes ( 126). This could be a starting point for
connectivity- and activity-mapping studies to further investigate the
mechanisms through which neurons mediate diverse behaviors.
However, with respect to its ap plication to brain organoid
recordings, we are entering terra incognita.
Machine learning and other mathematical models are
increasingly applied to certain parts of organoid research ( 127 –
129). However, machine learning, in the sense of deep learning and
supervised learning, deserves further comment. This is because it
presupposes that supervised learning is an appropriate theoretical
formulation of self-organization in organoids, in the sense that the
opportunities afforded by organoid research transcend questions
about how to engineer a particular behavior through supervised
learning ( 130). The opportunities probably require a more generic
theoretical framework within which to formalize self-organization
and active exchange between an organoid and its external milieu
(131,132). Practically, if one wanted to train an organoid to do this
or that, it would be impossible to implement the procedures
for supervised learning in machine learning (i.e. either
backpropagation of errors or local energy-based schemes).
Current developments favoring reinforcement learning, where
self-organization is met by feedback on functionality, lend
themselves to such problems. Strategically, if correct, this means
that the direction of travel of organoid research may be either
toward reinforcement machine learning or more aligned with some
of the foundational questions posed in neurobiology ( 133)o r ,
indeed, the physics of nonequilibrium self-organization ( 134,135).
Big-data infrastructures
Providing suitable infrastructure for the storage, curation, and
processing of OI big data is a scienti ﬁc challenge of its own. Analytic
datasets need to be stored in ef ﬁcient shared memory structures;
appropriate technology will be needed where manipulations, such
as standard matrix or tensor calculations, can be obtained without
partial or streaming access to the full dataset. Furthermore, a fast,
robust, and scalable computational analytic and curation
infrastructure for the resultin g data will be needed. A likely
requirement will be ef ﬁcient dimension-reducing transforms of
the 3D sensor arrays applicable for streaming data; e.g. by
“scattering transform ”(136), which has been particularly
successful in analyzing audio streams ( 137).
Each deep biological network computes some function,
transforming inputs to outputs depending on many variables,
chief among them: (1) the weights and biases and (2) the
activation functions. In both AI and OI, it is reasonably safe to
assume that the activation functions are essentially static; i.e. any
given node at any given time is activated only upon reaching a
certain threshold. However, Sinapayen et al. ( 138) suggest that
neural networks can autonomously change activity to avoid external
stimulation. The key difference between AI and OI networks is thatin OI networks, the weights and biases may dynamically change
over time –for example, owing to growth and/or maintaining
homeostatic equilibrium –however, with unclear changes in the
network function. Indeed, vastly different neural networks can
implement approximately the same function ( 139). A similar
result is well establishe d in biological networks ( 140). We,
therefore, hypothesize that although the precise weights and
architecture of the OI may be dynamic, the memories may be
stable over time.
The amount of data and respective curation, compression,
and processability will dramatically increase with boosted
electrophysiological recordings from OI systems. Additional
challenges come from spatiotemporal recording and the
combination of electrophysiolo gy and high-content imaging. In
addition, the training and experimental data created will require
efﬁcient frameworks for storage and analyses. This could include a
combination of in vivo proto-neural networks developed in brain
organoids and in silico analog/digital hybrid, and/or
neuromorphic computing ( 41,90,141,142). Transmedia
progressive learning will therefore exhibit the advantages of
both biological and machine computing and learning, while
mitigating the limitations of each. The main aspect of our
strategy for storage is to develop a scheme resembling the Large
Hadron Collider experiment at CERN, where sophisticated
triggers are used to detect events in real time and only events
with a potential discovery value are kept –greatly decimating the
data rate. We envisage a similar event-driven way of analyzing the
data: we will send discrete stimuli to the brain organoids, look for
coordinated responses in many channels, and store only the
discrete events related to these intervals. We will use insights
gained through multiple versions of experiment reduction to
develop a sensor correlation mod el and optimal event triggers
that optimize the trade-offs between data reduction and
discovery value.
Many large ongoing efforts aim to create data-processing tools,
storage solutions, and standa r d st oh a n d l et h es c a l eo fd a t a
generated by modern neuroscience experiments, e.g. the US
BRAIN Initiative ( 143). Open-source community solutions, which
the OI community could leverage, are being developed for terabyte-
and even petabyte-scale data across multiple modalities. As high-
throughput MEAs represent the most promising initial technology
for interfacing with organoids, solutions from the invasive and in
vitro electrophysiology communities can likely serve as the basis for
the OI community. Standardized community-processing pipelines
exist for this application, including machine learning tools such as
DataJoint Elements ( 144). Many individual tools and techniques for
electrode arrays have been developed for spike sorting ( 145) and
analysis of local ﬁeld potentials ( 146). Community cloud-based
archives are available for publishing such electrophysiological data
in an open and accessible manner, such as the OpenNeuro Archive
(147)a n dD A N D I( 148). These archives are hosting an ever-
increasing range of data from varied experimental paradigms.
Several standards initiatives could be leveraged to facilitate reuse,
reanalysis, and meta-analysis, such as the Brain Imaging Data
Standard (BIDS) ( 149) or Neurodata Without Borders (NWB)
(150). By leveraging the standards, processing pipelines, storage,Smirnova et al. 10.3389/fsci.2023.1017235
Frontiers in Science frontiersin.org 11

and dissemination techniques developed by the larger
electrophysiology community, the OI community can rapidly
establish a robust and reproducible big-data infrastructure.
Looking to the future, additio nal imaging modalities may
become critical to providing further insights into organoid
function and learning. Other processing tools and archives exist
for relevant modalities such as ﬂuorescence microscopy and also
other forms of microscopy; for example, the CaImAn pipeline for
calcium imaging data analysis ( 151) and the Brain Imaging Library
(152) for archiving and storage. In the invasive in vivo
neuroimaging community, functional and structural connectivity
(or connectomics) is also being studied with improved resolution
and larger volumes ( 153,154). Cloud-based processing pipelines for
deriving connectivity are under development ( 155), and the Brain
Observatory Storage Service and Database (BossDB) ecosystem has
been developed to host and archive large connectivity datasets at the
neuron-synapse level ( 156). Many emerging graph analysis tools
enable improved insight, such as statistical characterization of
connectomics ( 157) and identi ﬁcation of repeated motifs ( 158). In
time, multimodal datasets and infrastructure may play an
important role in the development of the OI community.
Ultimately, the OI community should seek to build on these
tools to establish standardized analysis and storage infrastructures.
Open data sharing can be a powerful approach to grow the
community and maximize the reuse of experimental data.
Establishing a large-scale, standardized set of experimental data
may rapidly improve processing tools, provide theoretical insight,
and generate hypotheses for future experiments. An interesting
model approach is the Human Connectome Project ( 159), which
used standardized approaches to high-resolution magnetic
resonance imaging to produce a gold-standard dataset for the
emerging ﬁeld of human connectomics. A similar data and
infrastructure effort for the OI community could provide
invaluable insights.
To summarize, a big-data ecosystem necessary to study OI
will require:
Standardization of experim ental data and metadata,
building on existing standards such as BIDS or NWB
Robust, repeatable, and standardized processing pipelines
that scale to large electrophysiological datasets
Efﬁcient, accessible, and open data storage, possibly
leveraging existing cloud archives such as OpenNeuro or
DANDI
The potential development of multimodal OI datasets
The establishment of standard, reference datasets for the
community
In the foregoing discussion, we have anticipated a need for the
collation, storage, and dissemination of big data, under the
assumption that organoid research will recapitulate developments
in neuroscience (and in particular imaging neuroscience). However,
there is an alternative path, which re ﬂects a move from “big data ”to
“smart data. ”In other words, we need only informative data that
enables people to answer well-posed questions. In effect, this would
represent a pushback against big data and a return to carefullydesigned experiments that elicit the right kind of data to make
inferences about the dynamics, plasticity, and functional
architectures in brain organoids. In short, the experiences of the
neuroscience community may usefully inform the kind of resourcesneeded to realize the full potential of organoid research over the
ensuing years.
Advancing biocomputing complexity
Optimized algorithms for organoid- in silico
interactions
Realizing the potential of OI requires more than interfacing a
computer with an organoid. In OI, the organoid can take on the role
of an embodied agent that interacts with an environment through
the organoid- in silico interface. This will require optimized
algorithms for organoid- in silico interactions as well as research
into theoretical frameworks for learning and adaptations in
organoids drawing from the theoretical neuroscience literature.
The viability of OI is dependent on optimized algorithms for
organoid- in silico interactions, in addition to the fast data storage
and retrieval described above.
There are two broad environments in which OI may operate:
open-loop or closed-loop:
Open-loop involves feeding i nformation into cells and
measuring the response. Recent work leveraging this
approach has found that neural systems can alter their
activity to perform various tasks, including context-
dependent encoding ( 160) and blind-source separation
(42), and to display features such as adaption toward
scale-free dynamics ( 161) or long-term activity-dependent
plasticity ( 41).
Closed-loop extends the open-loop environment to include
feedback to the neural systems about the result of the
system activity. Examples of this are limited owing to
technical dif ﬁculties, but high-latency/low-temporal
resolution analysis suggests that under these conditions,
cultures can demonstrate changes in neural dynamics ( 41)
and arbitrary learning ( 44). Moreover, real-time
implementations have recently resulted in goal-directed
learning displayed through a change in neural culture
activity when applied in line with neurocomputational
theories ( 29).
Exploring, applying, and re ﬁning empirically supported
theories of what fundamentally drives learning intelligence is a
critical factor. So far, numerous theories have been proposed to
explain how, at the fundamental level, neural systems process and
respond to information.
Theﬁrst branch of theories focuses on how neural systems are
organized, both structurally and functionally. Key notions include
neural criticality ( 162), neural Darwinism ( 163), cell assembly and
Hebbian plasticity ( 164), rule-based learning ( 165), and core ideas
behind population coding approaches ( 166,167). Generally, theseSmirnova et al. 10.3389/fsci.2023.1017235
Frontiers in Science frontiersin.org 12

theories aim to explain how the incredibly complex organization
within the brain results in its ultimate functioning. Thus, they offer
generally compatible frameworks for analyzing and interacting with
brain organoids, providing the opportunity for optimized input and
decoding of output.
A second “optimization ”category of theories generally focuses
on how a system or agent works to maintain homeostasis in a
dynamic environment. Broadly, this can be achieved either through
maximizing a utility or reward or by minimizing surprise or
uncertainty ( 165,168). Key theories include the Bayesian brain
hypothesis ( 169), efﬁcient coding hypothesis ( 170), value-
dependent learning ( 171), optimal control theory ( 172), and
learning by stimulation avoidance ( 138). Attempts have been
made to unify these theories, recently by exploring the underlying
compatibilities, most notably through the proposal of the free
energy principle ( 173), where the system or agent may engage in
active inference to construct a generative model of the external
environment and act in a manner to minimize the difference
between the internal model and the perceived external world. At
present, it is dif ﬁcult to empirically test many of these theories in a
controlled manner because in vivo organisms possess compensatory
mechanisms that hamper the interpretation of results. OI offers a
pathway for highly controlled ex periments to empirically test
these theories.
In addition to frameworks for learning in neural systems, the OI
community will require methods to assess embodied intelligence;
i.e. computational approaches to understand intelligent behavior in
organoids for both open-loop and closed-loop environments.
Previously, in vitro experiments have demonstrated the ability of
cell cultures to control both physical robotic systems and simulated
video games ( 29,174). Experience within the AI community
suggests that the OI community will likely bene ﬁtf r o m
standardized testing environments and conditions, accounting for
variability and constraints in input/output interfacing in terms ofchannel count and bandwidth. The AI reinforcement learning
community has produced a huge range of games, simulation
environments, and physical systems that could be adapted to OI
evaluation. Of particular interest to the OI community may be the
ﬁeld of continual or lifelong learning ( 175,176), where embodied
agents are assessed in learning that occurs over a sequence of
experiences (often referred to as a “lifetime ”). Such testing
environments may serve the O I community by providing
important benchmarks for understanding functional activity and
learning in organoids.
Incorporating complex biological
inputs in OI
Previous sections describe how we intend to interface organoids
and computers. Combining organoids with various types of more
complex inputs and output stimulation and recording interfaces ( 177,
178) will allow us to understand the potential for real-time controls.
The consequences of such interconnections can be explored, starting
with two brain organoids, one with complex input and one withcomplex output connections. A sensory organ, such as a retinal
organoid, could then be connected with a brain organoid. Eventually,
networks of organoids will be interconnected to implement more
complex OI. The organoid will be interfaced with electrical and
ﬂuidic-sensing and simple outputs controlling machines through
biofeedback on the cellular level; i.e. giving the brain organoid
control by feeding back the results of its induced actions.
By connecting retinal and brain organoids we can determine
whether signals can transfer between these different neuronal
organoids and how this exogenous biological signaling will be
interpreted by the brain organoid –establishing the initial baseline
of organoid –organoid communication. Retinal organoids containing
laminated retinas with outgrowth of outer segment-like structures and
synaptic ribbons have been developed ( 179,180). Synapse formation
between two organoids is complex and was demonstrated recently in
assembloids ( 48). Retinal and brain organoids can be connected either
through electrodes or directly. Since methods to generate mature,
endogenous, light-sensing retina are preliminary and very inef ﬁcient,
engineered photosensitive ion channels, which are expressed under
the control of a photoreceptor-speci ﬁcp r o m o t e r( 181 –183), can
substitute as a proxy for light-reactive photoreceptors. Optimization
of retinal organoid culture conditions to promote more robust
signaling has recently been published ( 184).
Understanding and perhaps even in ﬂuencing the connectivity
of retinal and brain neurons would be extremely exciting. Although
we and others are actively investigating ways to establish and
modulate these connections, we are still quite far away from a
system that can demonstrate robustly modifying neuronal
connections in a directed manner. Ultimately, we aim to build on
this simpli ﬁed approximation or representation of visual input
toward a system that more fully approximates vision.
Leveraging advances in the molecular basis
of biological learning
Advances in the molecular biology of synaptic plasticity will be
critical for optimizing the capacity of organoid systems for learning
and OI. Growth conditions can now be optimized to allow organoid
neurons to optimally express genes essential for learning in thehuman brain.
First, they need to express genes coding for the neurotransmitter
receptors that mediate synaptic transmission. We have already
characterized the expression dynamics of different subunits of the N-
methyl-D-aspartate (NMDA) glutam ate receptor during differentiation
(unpublished observation). The long-term organoid maturation and
age based on gene expression and swi tch of the main receptor subunits
were recently extensively characterized ( 185). The machinery of the
organoid ’s biochemistry, especially of neurotransmitters, will be an
important part of understanding the signaling cascades and synaptic
plasticity necessary for learning; to this end, a thorough
characterization of protei n expression is warranted.
Secondly, it will be important for organoids to express IEGs.
IEGs mediate synaptic processes essential to memory consolidation
and are rapidly transcribed in adult neurons as they processSmirnova et al. 10.3389/fsci.2023.1017235
Frontiers in Science frontiersin.org 13

information ( 186). Moreover, evidence indicates that IEGs are
required for circuits capable of gamma frequency rhythmicity
(187), which is associated with a ttention and information
processing. Using RNA-sequencing to compare organoids (at
different stages of maturation and grown under different culture
conditions) with fetal, adolescent, and adult brains will allow the
identi ﬁcation of growth conditions that optimize expression of
these essential genes. It is critical to ensure IEG expression that is
robust and dynamically responsive to activity evoked by a
pharmacological block of GABA Ainhibition (e.g. using
bicuculline). Dynamic, activity-dependent IEG expression would
assure the presence of molecular substrates necessary for organoids
to establish circuits with balanced excitatory and inhibitory neurons
and synapses. The cell culture conditions should be optimized so
that 10 –30% of neurons express IEGs in response to informational
inputs. This level of sparsity is typical of brain regions involved in
learning and memory (including the hippocampus and neocortex)
and may ensure that multiple ensembles can be created to uniquely
encode different streams of data. This contrasts with the global
activation of IEGs that may occur with non-informational activity,
such as a seizure. IEG expression and/or associated reporters can
also provide a means to assess the formation of ensembles of
neurons that are stably linked to speci ﬁc inputs. In the brain,
such ensembles are thought to represent memory engrams. EEG
data can then be correlated with dynamic activity reporters (Ca2+or
voltage) and IEG expression data. Ultimately, neuronal activity can
be stimulated and recorded optogenetically, as recently described
(48). To our knowledge, IEG expression has not previously been
utilized as an endpoint for optimizing organoid growth conditions.
Successful use of this parameter would establish a biological basis
for OI and address concerns regarding the uncertainty of the
developmental state of organoids and their potential utility as
information-processing memory units.
OI-led advances in medical research
and innovation
In addition to pioneering the use of human brain organoids for
computing and learning, OI research will also allow the exploration of
inter-individual neurodevelopm ental and neurodegenerative
differences between stem cell donors. Alzheimer ’s disease and other
dementias could represent one particularly important priority for
research. Globally, more than 55 million people are living with
dementia, and this number is projected to exceed 150 million by
2050 ( 188,189). Dementia is among the top 10 leading causes of
death ( 190) and globally costs at least $1 trillion annually ( 191,192).
Clinical trials of novel Alzheimer ’s disease therapies have shown very
poor success rates, in part owing to premature translation of
successful results in animal models that mirror only limited aspects
of the pathology in humans ( 193,194). The adaptation of OI research
models to neurodegenerative diseases would offer the ﬁrst human-
based preclinical model to help us understand and develop effective
treatments for these devastating diseases.In addition to neurodegenerative diseases, neurodevelopmental
disorders also lend themselves to OI, given that the different stages of
brain development are re ﬂected in the bioengineering of these models
from stem cells. Conditions such as autism are major concerns owing
to the enormous increase in prevalence. In the US, autism spectrum
disorder (ASD) was diagnosed in the 1970s in 1 in 10,000 children,
but according to the Centers for Disease Control (CDC), in 2021 it
was 1 in 44 ( 195). While the disorder has heritable aspects,
environmental in ﬂuences are an increasing focus. The brain
organoid model has shown promise for both developmental
neurotoxicity ( 196,197) and gene × environment ( 198)s t u d i e so f
autism. A varying combination of cognitive impairments
characterizes this complex spectrum of diseases ( 199). Similarly,
leukodystrophies are a diverse group of rare genetic disorders
affecting white matter and linked to cognitive impairment ( 200).
Using OI to explore the genetic basis of autism or leukodystrophies
appears to represent an important path to understanding these
disorders and to allowing screening of potential drugs that might
boost underdeveloped cognitive functions.
Schizophrenia affects around 1% of the population worldwide
and is one of the top 10 illnesses contributing to the global burden
of disease ( 201). Schizophrenia has a prominent genetic basis, and it
has been suggested that it may be neurodevelopmental in origin
(202). Prenatal complications are an important contributor to the
condition ( 203), while cognitive dysfunction is a hallmark ( 204),
with a strong similarity to autism ( 205). Human iPSC lines, e.g. with
genetic backgrounds associated with disorders, are available and
continuously growing [e.g. SFARI base for autism ( 206)]. Organoids
developed from iPSCs from individuals with various conditions
could be compared against control samples to help identify
differences that may elucidate the pathogenesis, risk factors, and
treatments. The application of an OI approach using these cell lines
would thus be very promising to aid further understanding and
characterization of the etiology of the neurodegeneration,neurodevelopmental, and psychiatric disorders. This enables a
multitude of applications, from de-risking (pediatric) drugs for
adverse effects on cognitive development (
207), the identi ﬁcation of
toxicants and illicit drugs with long-term effects on cognitive
capabilities, and the optimization of lead drug candidates acting
on respective pharmacological targets.
The study of memory, learning, and cognition –and the impact of
neurodegeneration on these functions –will require physiologically
relevant neuron-to-glia ratios and high levels of biological complexity
and interregional communication. Besides assembloids ( 48,208,209),
aspects of ventral and dorsal regions in the absence of external
morphogens or growth factors have been recapitulated ( 210 –212),
highlighting an innate ability of self-organization in both cases.
Recently, Cederquist et al. ( 213) demonstrated that a chimeric
assembloid of an early organoid and a cluster of sonic hedgehog
(SHH)-secreting cells resulted in dorsal-ventral and anterior-posterior
positional axes. However, organoids do not have predictable anatomy
nor de ﬁned topography, and generally do not re ﬂect the characteristic
developmental asymmetry ( 208,213). Nonetheless, brain organoids
do show a remarkable self-organizational capacity. This might
be further enhanced by functional demands, which may beSmirnova et al. 10.3389/fsci.2023.1017235
Frontiers in Science frontiersin.org 14