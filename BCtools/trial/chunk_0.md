Organoidintelligence(OI):the
newfrontierinbiocomputing

andintelligence-in-a-dish
Lena
Smirnova
1
,BrianS.
Caffo
2
,DavidH.
Gracias
3,4,5,6,7,8
,
Qi
Huang
3
,Itzy E.
MoralesPantoja
1
,Bohao
Tang
2
,
DonaldJ.
Zack
9
,Cynthia A.
Berlinicke
10
,J.Lomax
Boyd
11
,
TimothyD.
Harris
12,13
,Erik C.
Johnson
14
,BrettJ.
Kagan
15
,
Jeffrey
Kahn
16
,AlyssonR.
Muotri
17,18
,BartonL.
Paulhamus
19
,
JensC.
Schwamborn
20
,Jesse
Pl ot kin
1
,AlexanderS.
Szalay
21,22,23
,
JoshuaT.
Vogelstein
12
,PaulF.
Worley
24
andThomas
Hartung
1,25
\*
1
CenterforAlternativestoAnimalTesting(CAAT),Departmentof EnvironmentalHealth and
Engineering,BloombergSchool of PublicHealthandWhiting School of Engineering,

JohnsHopkins University,Baltimore,MD,UnitedStates,
2
Departmentof Biostatistics,Johns
HopkinsBloombergSchool ofPublicHealth, JohnsHopkinsUniversity,Baltimore,MD, UnitedStates,
3
DepartmentofChemicalandBiomolecularEngineering,JohnsHopkinsUniversity,Baltimore,
MD, UnitedStates,
4
Departmentof MaterialsScience andEngineering,JohnsHopkinsUniversity,
Baltimore,MD, UnitedStates,
5
DepartmentofChemistry,JohnsHopkinsUniversity,Baltimore,
MD, UnitedStates,
6
SidneyKimmelComprehensiveCancerCenter,JohnsHopkins UniversitySchool
ofMedicine,Baltimore,MD, UnitedStates,
7
LaboratoryforComputationalSensingandRobotics
(LCSR),JohnsHopkinsUniversity,Baltimore,MD, UnitedStates,
8
Departmentof Oncology,Johns
HopkinsUniversitySchool of Medicine,Baltimore,MD, UnitedStates,
9
Departmentof
Ophthalmology,JohnsHopkinsHospital, Baltimore,MD, UnitedStates,
10
WilmerEyeInstitute,Johns
HopkinsUniversitySchool of Medicine,Baltimore,MD, UnitedStates,
11
Berman Instituteof Bioethics,
JohnsHopkins University,Baltimore,MD,UnitedStates,
12
Departmentof BiomedicalEngineering,
JohnsHopkins University,Baltimore,MD,UnitedStates,
13
JaneliaResearchCampus,HowardHughes
MedicalInstitute,Ashburn,VA,UnitedStates,
14
ResearchandExploratoryDevelopmentDepartment,
JohnsHopkins UniversityAppliedPhysicsLaboratory,Laurel,MD, UnitedStates,
15
CorticalLabs,
Melbourne,VIC,Australia,
16
Departmentof HealthPolicyandManagement,BloombergSchool of
PublicHealth, JohnsHopkinsUniversity,Baltimore,MD, UnitedStates,
17
Departmentof Pediatrics,
StemCellProgram,UniversityofCalifornia,SanDiego,SanDiego,CA,UnitedStates,
18
Departmentof
Cellular&MolecularMedicine,StemCellProgram,Universityof California,SanDiego,SanDiego,

CA, UnitedStates,
19
AppliedPhysicsLaboratory,JohnsHopkinsUniversity,Baltimore,
MD, UnitedStates,
20
LuxembourgCentreforSystemsBiomedicine(LCSB),Universityof Luxembourg,
Luxembourg,Luxembourg,
21
DepartmentofComputerScience, Whiting School of Engineering,
JohnsHopkins University,Baltimore,MD,UnitedStates,
22
DepartmentofPhysicsandAstronomy,
KriegerSchoolofArts &Sciences,JohnsHopkinsUniversity,Baltimore,MD, UnitedStates,
23
Mark
FoundationCenterforAdvancedGenomicsandImaging,JohnsHopkinsUniversity,Baltimore,
MD, UnitedStates,
24
Solomon H.SnyderDepartmentof Neuroscience,JohnsHopkinsUniversity
School ofMedicine, Baltimore,MD, UnitedStates,
25
CAAT-Europe,UniversityofKonstanz,
Konstanz,Germany
Abstract
Recentadvancesinhumanstemcell-derivedbrainorganoidspromisetoreplicate
criticalmolecular andcellular aspectsoflearningandmemoryandpossibly

aspectsof cognition
invitro
.Coiningtheterm
ﬁ
organoidintelligence
ﬂ
(OI )to
encompassthesedevelopments,wepresent acollaborativeprogramto
implementthevision of
a multidisciplinary

eldofO I.This aimstoestablishO Ias
aformof genuinebiologicalcomputingthatharnesses brainorganoids using
scienti

candbioengineeringadvanc esinanethic allyresponsiblemanner.
Standardized,3D,myelinatedbrain o
rganoidscannowbeproducedwithhigh
celldensityandenrichedlevelsofglialcellsandgeneexpressioncriticalforlearning.
Integratedmicro

uidicperfusionsystemscansupportscalableanddurable
Frontiersin
Science
frontiersin.org
01
OPENACCESS
EDITEDBY
ArtiAhluwalia,
UniversityofPisa,Italy
REVIEWEDBY
KarlFriston,

UniversityCollegeLondon,

UnitedKingdom

GaryMiller,
ColumbiaUniversity,UnitedStates
\*CORRESPONDENCE
ThomasHartung
thartun1@jhu.edu
RECEIVED
11August 2022
ACCEPTED
07February2023
PUBLISHED
28February 2023
CITATION
SmirnovaL,
Caffo BS,
GraciasDH,
HuangQ,
MoralesPantoja IE,
TangB,
Zack DJ,
BerlinickeCA,
Boyd JL,
HarrisTD,
JohnsonEC,
KaganBJ,
KahnJ,
MuotriAR,
PaulhamusBL,
SchwambornJC,
PlotkinJ,
SzalayAS,
VogelsteinJT,
WorleyPFand
HartungT.Organoid intelligence(OI):
thenewfrontierinbiocomputing
andintelligence-in-a-dish.
FrontSci
(2023)1:1017235.
doi:10.3389/fsci.2023.1017235
COPYRIGHT
©2023Smirnova,Caffo,Gracias,Huang,

MoralesPan toja,T ang,Zack,Berlinicke,

Boyd,H arris,Joh nson,Kagan,Kahn ,Mu otri,
Paulhamus,Schwamborn,Plotkin,Szalay,
Vogelstein, WorleyandHartung.Thisisan

open-accessarticledistributedunderthe

termsofthe
CreativeCommonsAtt ribut ion
License (CCBY).
Theuse,distributionor
reproductioninotherforums ispermitted,

providedtheoriginalauthor(s)andthe

copyrightowner(s)are creditedandthat
theoriginalpublicationinthis journalis
cited,inaccordance withaccepted

academicpractice.Nouse,distributionor

reproductionispermitted whichdoesnot
complywiththeseterms.
TYPE
FrontiersinScienceLeadArticle
PUBLISHED
28February 2023
DOI
10.3389/fsci.2023.1017235

culturing,andspatiotemporalchemicals
ignaling.Novel3Dmicroelectrodearrays
permithigh-resolutionspatiotemporalele
ctrophysiologicalsignalingandrecording
toexplorethecapacityofbrainorganoids torecapitulatethem olecular
mechanismsoflearningandmemoryformationand,ultimately,their
computational potential. Technologies thatcouldenablenovel biocomputing
models
via
stimulus-responsetrainingandorganoid-computerinterfacesarein
development.Wee nvisageco mple x,networke dinterfaceswhere bybrain
organoidsareconnec tedw ith real-w orldsensorsand output devic es,and
ultimatelywitheachotherandwithsensoryo rganorganoids(e.g.retinal
organoids),andaretrainedusingbiof eedback,big-datawarehousing,and
machinele arningmethods.Inparallel ,weemphasiz eanembeddedethics
approach toanalyzetheethicalaspects raisedbyOIresearch inaniterative,
c ollaborativemannerinvolvingallrelevantstakeholders.Themany possible
applicationsofthisresearchurgethestrategicdevelopmentofOIasascienti

c
discipline.WeanticipateOI-based biocomputingsystemstoallowfasterdecision-
maki ng,continuouslearningduring tasks,andgreaterener gyanddataef

ciency.
Furthermore,thedevelopmentof
ﬁ
intelligence-in-a-dish
ﬂ
couldhelpelucidatethe
pathophysiologyofdevastatingdevelopm
entalanddegenerativediseases(such as
dementia),potentiallyaidingtheidenti

cationofnoveltherapeuticapproachesto
addressmajorglobal unmetneeds.
KEYWORDS
organoidintelligence,biocomputing,microphysiological systems,electrophysiology,
cognition,arti

cialintelligence
Keypoints
†
Biologicalcomputing(or biocomputing)couldbefaster,
moreef

cient,andmorepowerfulthansilicon-based
computingandAI,andonlyrequirea fractionof
theenergy.
†
‚
Organoidintelligence
™
(OI)describesanemerging
multidisciplinary

eldworkingtodevelopbiological
computingusing3D culturesofhumanbraincells(brain

organoids)andbrain-machineinterface technologies.
†
OIrequiresscalingupcurrentbrainorganoidsinto
complex,durable3Dstructures enrichedwithcellsand
genesassociatedwithlearning,andconnectingtheseto

next-generationinputandoutputdevicesandAI/

machinelearningsystems.
†
OIrequiresnewmodels,algorithms,andinterface
technologiestocommunicatewithbrainorganoids,
understandhowtheylearnandcompute,and processand
storethemassiveamountsofdatatheywillgenerate.
†
OIresearchcould alsoimproveourunderstandingof
braindevelopment,learning,andmemory,potentially
helpingto

ndtreatmentsforneurologicaldisorderssuch
asdementia.
†
EnsuringOIdevelopsinanethicallyandsocially
responsivemannerrequiresan
‚
embeddedethics
™
approachwhereinterdisciplinaryandrepresentative
teamsofethicists,researchers,andmembersofthepublic
identify,discuss,andanalyzeethicalissuesandfeedthese
back toinformfutureresearchandwork.
Introduction
Humanbrainsare slowerthanmachinesatprocessingsimple
information,suchasarithmetic,buttheyfarsurpassmachinesin
processingcomplexinformationas
brainsdealbetterwithfewand/or
uncertaindata.Brainscanperformbothsequentialandparallel
processing(whereascomputersc
andoonlytheformer),andthey
outperformcomputersindecision-makingonlarge,highly
heterogeneous,and incompletedat
asetsandotherchallengingforms
ofproces sing.Thepr ocessingpowerofthebr ainisillus trat ed by the
observationt hat in2013,theworld
™
sfourth-largestcomputertook40
minutestomodel1 secondof 1%ofahuman
™
sbrainactivity(
1
).
Moreover,each brainhasastorag
ecapacityestimatedat2,500TB,
basedonits86
Œ
100billionneuronshavingm orethan 10
15
connections
(
2
,
3
).Inthisarticle,wedescribetheemerging

eldthatweterm
ﬁ
organoidintelligence
ﬂ
(OI),whichaims toleveragetheextraordinary
biologicalprocessingpower ofthebrain.
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
02

Super

cially,bothbiologicallearningandmachinelearning/AIby
anintelligent agentbui
ldinternal representationsoftheworldto
improvetheirperformanceinconduc
tingtasks.However,fundamental
differencesbetweenbiologic
al andmac hinelearninginthe
mechanismsofimplementation
andtheirgoalsr es ultint wo
drasticallydifferentef

cienci es.First,biologicallearningusesfarless
powertosolvecomputationalproblems.Forexample,alarvalzebra

sh
navigatestheworldtosuccessfully huntprey and avoid predators(
4
)
usingonly0.1microwatts(
5
),whileahumanadultconsumes100
watts,ofwhichbrainconsumptionconstitutes 20%(
6
,
7
). Incontrast,
clustersusedto master state-of-the-artmachinelearningmodels
typicallyoperateataround10
6
watts.SinceJune2022,theUSA
™
s
Frontierhasbeentheworld
™
smostpowerfulsuperc
omputer,reaching
1102petaFlops(1.102 exaFlops)
ontheLINPACKbenchmarks.The
powerconsumptionofthenewsupe
rcomputeris21megawatts, while
thehumanbrainoperatesattheestimatedsame1exaFlopand
consumesonly20watts(
Table1
)(
8
Œ
11
).Thus,humansoperateata
10
6
-foldbetterpoweref

ciencyrelative tomodernmachinesalbeit
whileperformingquitedifferenttasks.
Second,biologicallearningusesfewerobservationstolearnhow
tosolve problems.Forexample,humanslearn asimple
ﬁ
same-versus-
different
ﬂ
taskusin garound10tr ainingsamples(
12
);simpler
organisms,suchas honeybees,alsoneedremarkablyfewsamples
(~10
2
)(
13
).I nc on tr as t,i n2011 ,m ach in esco ul dn otl ear nt hes e
distinctionsevenwith10
6
samples(
14
)andin2018,10
7
samples
remainedinsuf

cient(
15
).Thus,in thissense, at least,humans
operateata>10
6
times betterd ataef

ciencythanmodern
machines.TheAlphaGosystem,whichbeattheworldchampionat
thecomplexgameGo,offersaconcreteillustration(
16
,
17
).AlphaGo
wastrainedon datafrom160,000games(
17
);ahumanplayingfor

vehours/daywouldhavetoplay continuouslyformorethan175
yearstoexperiencethesamenumberoftraininggames
Œ
indicating
thefarhigheref

ciencyofthebraininthiscomplexlearning activity.
Theimplication isthatAIandmachine-learningapproacheshave
limitedusefulnessfortasksrequiringreal-timelearning anddynamic
ac tion sinachan gingen viron men t.Th epoweran def

ciency
advan tagesofbiologicalco mputingovermachi n ele arningare
multiplicative.Ifittakesthesameamountoftimepersample ina
human ormachine,thenthetotalenergyspenttolearnanew task
requires10
10
timesmoreenergyforthemachine.AlphaGowas
trainedfor4weeksusing50graphicsprocessingunits(GPUs)(
17
),
requiringapproximately4×10
10
Jofenergy
Œ
aboutthe same amount
ofenergyrequiredtosustainthemetabolismofanactiveadult
humanforadecade.ThishighenergyconsumptionpreventsAIfrom
ac hieving man y aspirationalgoals,forexamplematching or
exceedinghumancapabilities for complextaskssuchasdriving
(
18
).Evenlargemultinationalcorporationsarebeginningtoreach
thelimitsofmachinelearningowingtoitsinef

ciencies(
19
),andthe
associatedexponentialincrease inenergyconsumption is
unsustainable(
20
),especially iftechnologycompaniesaretoadhere
to theircommitmentsto becomecarbonnegativeby2030(
21
,
22
).At
anational level,alreadyin2016ittooktheequivalentof34coal-
poweredplants,eachgenerating500 megawatts,to meetthe power
demandsof US-baseddatacenters(
23
).Beingmuchmoreenergy
ef

cientthancurrentcomputers,human brains couldtheoretically
meet thesameUSdatastoragecapacityusingonly1,600kilowattsof
energy.Notably,thepowerdemands ofany currentorfuture
implementationofOIisverydifferentfromtheenergy
consumptionofthehumanbody,especiallyconsideringtheenergy
footprintofmoderncellculturerelativetosmallorganoidstoday.
Thesecomparisonsof brainsandcomputersserveonlyas
illustrationsofthehighef

ciencyofthehumanbrain.
Together,theseobservationshavecreatedhighexpectationsfor
biological,brain-directedcomputing (
24
Œ
26
)asanalternative to
silico n -b asedcompu ting, with thepotentialfo run preceden ted
advancesin computingspeed,processingpower,dataef

ciency,
andstoragecapabilities
Œ
allwith lowerenergyneeds.However,
realizing thepotentialofbiocomputinghasprovedchallenging,and
mostresearchremainsinitsinfancy.Todate,theterm
ﬁ
biological
computing
ﬂ
hasbeenusedmainlyto describetheuseofDNAtostore
digitaldata(
27
,
28
).Anexceptiontothisistherecent workbyKagan
etal.(
29
),whichusestheterm
ﬁ
syntheticbiologicalintelligence
ﬂ
(SBI)todescribethe useofsynthetic biology togenerateintelligent
systems through brain-directedcomputing,albeit usingonlysimple
2Dmonolayercellcultures(whichpoorlyreplicatethecomplexityof
the
invivo
brain)asaproof-of-concept.
Wehavecoined theterm
ﬁ
organoidintelligence
ﬂ
(OI )todescribe
ane merging

eldaimingtoexpandthede

nitionofbiocomputing
towardbrain-directedOIcomputing,i.e.to leveragethesel f-assembled
mach ineryof3Dhumanbr aincellcultures(brainorganoids ) t o
memorizeandcomputeinputs. Brai
norganoidsrecapitulateorgan
histoarchitecture andfunctionalityfarmore closelythantraditional2D
cultures.Theycancontainmyelinatedaxons (
30
Œ
32
)andnot only
showspontaneouselectro
physiologicalactivity(
33
)butalso
demonstratecomplexoscillatoryb ehavior(
34
),andexhibithighcell
densityandlayeringpatterns,all ofwhichm akebrainorganoids
superiortotraditionalmonolayercultures(
34
Œ
36
).Thequestionis:
canwelearn fromandharnessthecomputingcapacityofthese
TABLE1 Comparisonofthelatestsupercomputer(June2022)and a
humanbrain.
Frontiersupercomputer
(June2020)
Humanbrain
Speed1.102exaFLOPS~1exaFLOPS(estimate)
Power
requirements
21MW10
Œ
20W
Dimensions680m
2
(7,300sqft)1.3
Œ
1.4kg(2.9
Œ
3.1lb)
Cost$600millionNotapplicable

Cabling145km(90miles)850,000km(528,000miles)
ofaxonsand dendrites
Memory75TB/sread;35TB/swrite;
15billionIOPS

ashstorage
system,alongwith
the700PBOrionsite-wide
Lustre

lesystem
2.5PB(petabyte)
Storage58billiontransistors125trillionsynapses,which
canstore4.7bitsof

informationeach
TheHewlettPackardEnterpriseFrontier, orOLCF-5,istheworld
™
s

rstexascale
supercomputer,hostedattheOakRidgeLeadershipComputingFacility(OLCF)in

Tennessee.Itiscomparedherewith thehumanbrain.Forsourcessee(
6
Œ
11
).
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
03

organ oids ?Achievingthiswillrequiremajor advancesint he
interfacingofbraincellcultures
andcomputers.Weenvisionusing
biofeedbacktosystematic ally trainorganoidswithincreasingly
complexsensoryinputsan
doutputopportunities
Œ
interfacingthe
brainorganoidswithcomputers,se
nsors,andmachi
ne interfacesto
facilitatesupervisedandu nsupervisedlearning.Weu setheterm
ﬁ
OI
ﬂ
for this approachtostressitscomplementaritytoAI
Œ
where
computersaim to perform tasksdonebybrains,oftenbymodeling
ourunderstandingoflearning.However,whileAIaims tomake
c omputersmorebrain-like,OIresearchwillexplorehowa3 Dbrain
cellculturecanbemademorecomputer-like.
Themanypossibleapplicationsof thiswork includeanew
generationofbiologicalandhybrid(
biological-electronic) computing
technologies,together withadv
ancesinourunderstandingofthe
physiologyofcognition,learning,andmemory,andthe
pathophysiologicaleffectsof d
evelopmental anddegenerative
diseases,intoxication, andinfection
Œ
which inturnc ouldstimulate
drugdevelopmentandotherinterve
ntions.OIalsoh asthe potentialto
unlocknewneuromimeticAIalgorithms (withthepotentialto
overcomecurrent AIlimitations
)andaidthe developmentofnew
brain-computer-interfacetechnology.
Theconceptofbrain-machine interfacingemergedaround

ve
decadesago.Beforetheadventof morecomplexhumanneuronal
cultures andbrainorganoids,pioneeringworkonlearningand
memorywascar riedoutus in gpr imit iv eanimalssuch asthe
lamprey,showinglong-termpotentiation(
37
).This ledtobrain-
machineinteractionstudiese
stablishingbidirectional
communicationsbetweenthenervoussystemandexternaldevices
(
38
).Othersusedbrainslicesofdifferentspeciestostudythebasic
phenomenaoflearning onacellularlevel (
39
).Neuron cultures
werelatershowntoperform simplerobotic tasksordemonstrate
increasedplasticitywithin adelayedclosed-loopenvironment(
40
,
41
).Thecombinationof braincell culturesandcomputers hasalso
beenattempted: 2Dculturedratneuronsdisplayedevidence ofself-

organizedactivityinacomputationaltask(blindsourceseparation)
whensuppliedwithelectricalinformation(
42
).Adifferentstudy
showedthatthesecultureslearnedtorespond intheformofdistinct
electrophysiologicalpatternstolow-frequencyfocalstimuli(
43
,
44
).
Tothebestofourknowl edge,however,norel evantapproach using
brainorganoidsaslearningsystemsh
as beenreported.Previous research
hasdemonst rat edspontan eousel ectr ophysiologicalsign als an d
synchronousneuralnetworkactivityofdissociatedorganoids(
45
),
slicedorganoids(
46
),ordeveloping full organoids(
34
,
47
),and
advancedmanipulationof neuralcircuitswithinassembloids
(organoids mergingtwodistinct brai
nregions)wasrecentlypublished
(
48
).The onlystudyresemblingourvision isthe recentworkbyKagan
et al.(
29
),whiche mbed dedmonolayersofc ortical neu ronsinareal-time
closed-loopenvironment
via
electrophysiologicalstimulation and
recording.Thesecultures self-organi
zedtorapidlyalter their activityto
displaygoal-directedbehaviorinasimulatedgameenvironment.
Similarly, theEuropeanUnion-fundedNEU-CHiPprojectaimsto
demonstratethegrowthoflayerednetworksofbrainstemcellson
microchips(
49
).Inaddition,theHumanBrainProjectmodelssimilar
(butvirtual)input-brainoutputmachinemodels(
50
).
Obviously,termssuchas
ﬁ
cognition,
ﬂﬁ
intelligence,
ﬂﬁ
sentience,
ﬂ
an d
ﬁ
co n sciousn ess,
ﬂ
describin ghumancapabilities,can n otbe
directlytranslatedtosimplecellculturemodels;theyareusedhere
todescribetherealizationofbasicfunctionsunderlying thesehigher-
orderfunctionalities. Aworkshoptode

ne adequateterminologyfor
the

eldisin preparation.Please see the glossaryincluded,which
attemptstoprovidede

nitionsinthecontextofthismanuscript.
Inthisarticle,wepresentanarchitecture(
Figure1
)and
blueprintforanOIdevelopment andimplementationprogram
designedto:
†
Determinet h ebiofeedbackchar acteristicsofex isting
human brainorgan oidscagedin microe lectrodeshells,

potentiallyusing AItoanalyzerecordedresponsepatterns
toele ctricalandchemical(neurotran smittersan dtheir
correspondingreceptoragonistsandantagonists)stimuli.
†
Empiricallytest,re

ne,and,whereneeded,develop
neurocomputationaltheoriesthatelucidatethe basisof
in
vivo
biologicalintelligenceandallow us tointeractwithand
harness anOIsystem.
†
Furtherscaleupthebrainorganoidmodeltoincreasethe
quantity ofbiologicalmatter,thecomplexity ofbrain
organoids,thenumber ofelectrodes,algorithmsforreal-
timeinteractions withbrainorganoids,andtheconnected
inputsourcesandoutputdevices;andtodevelopbig-data
warehousingandmachinelearningmethodsto
accommodatetheresultingbrain-directedcomputing
capacity.
†
Explorehowthisprogramcouldimproveour understanding
ofthepathophysiologyofneurodevelopmentaland
neurodegenerativedisorderstowardinnovativeapproaches
totreatmentorprevention.
†
Establishacommunityandalarge-scaleprojecttorealize
OIcomputing,takingfullaccountofitsethicalimplications
anddevelopinga commonontology.
Tothelatterpoint,acommunity-formingworkshopwasheldin
February 2022(
51
),whichgaverisetotheBaltimoreDeclaration
TowardOI(
52
).Itprovidesas tatementofvisionforanOI
communitythathasledtothe
developmentofthe program
outlinedhere.
Prerequisitesforbiocomputingmodels
Cultureandbioengineeringtechnologies
toadvance3Dbrainorganoids
TheadventoftwobiologicaltechnologiesmakesourOI
approachpossible:thegroundbreakingwork toreprogram human
somatic cellsbacktostemcells[i.e.inducedpluripotent stemcells
(iPSC)](
53
); an dthemorerecentdevelopmentof3 Dbrain
organoidsfromiPSC.
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
04

Advancesin3Dorganoidculture
Thepastdecade hasseen arevolutioninbraincellcultures,
movingfromtraditionalmonolayerculturestomoreorgan-like,
organized3Dcultures
Œ
i.e.brainorganoids(
Figure2A
).These can
begeneratedeitherfromembryonicstemcellsorfromtheless

ethicallyproblematiciPSCtypicallyderivedfromskinsamples(
54
).
TheJohnsHopkinsCenterforAlternatives toAnimalTesting,
amongothers,hasproducedsuchbrainorganoidswithhighlevels
ofstandardizationandscalability(
32
)(
Figure2B
).Havinga
diameterbelow500
m
m,andcomprisingfewerthan100,000cells,
each organoidisroughly one3-millionththesizeofthehuman
brain(theoreticallyequatingto800MB ofmemory storage).Other
groupshavereportedbrainorganoidswithaveragediametersof3
Œ
5
mm andprolongedculturetimesexceeding1year(
34
Œ
36
,
55
Œ
59
).
Theseorganoidsshowvariousattri
butes thats houldimproveth eir
potentialforbiocomputing(
Figure2
). First,celldensityinthese3D
modelsissimilartothe
invivo
celldensity,a ndm uchhighertha n in
monolayercultures;theratioof cellstomediavolumeisalsomuch
highercomparedtomonolayers.Second,mostofthesebrainorganoids
showspontaneousele ctrophysiologica
lactivityandreactivitytoelectrical
stimulation(viae voked

eldpotentials)(
32
),con

rm ingthepresenceof
activesynapses.Trujilioetal.have
shownpatterningof cortexlayersand
oscillationwavescomparabletoelectroencephalograms(EEGs)from
humanpreterm babies
™
brains(
34
).
Third,axonsintheseorganoids showextensivemyelination.
Pamiesetal.werethe

rsttodevelopa3Dhumanbrainmodel
showingsigni

cantmyelination ofaxons(
32
).About 40% ofaxons
inthebrainorganoidsweremyelinated(
30
,
31
),whichapproaches
the 50%foundinthehuman brain(
60
,
61
).Myelinationhassince
been reproducedinotherbrainorganoids(
47
,
62
).Myelinreduces
theca pacitanceoftheaxonalmembraneandenables saltatory
conductionfromonenodeofRanviertothenext.Asmyelination

increaseselectricalconductivityapproximately100-fold,this
promisestoboost biologicalcomputingperformance,thoughits
functional impactinthismodelremains tobedemonstrated.
Finally,theseorganoidculturescan beenrichedwithvariouscell
typesinvolvedinbiologicalle arning,n amelyoligodendrocytes,
microglia, andastrocytes.Gliacellsareintegrallyimportantforthe
pruningofsynapsesinbiologicallearning(
63
Œ
65
)but havenotyet
beenreportedatphysiologicallyrelevantlevels in brainorganoid
models.Preliminarywork inourorganoidmodelhas shownthe
potentialforastroglia cellexpansiontophysiologicallyrelevantlevels
(
47
).Furthe rmore,recente vide nc
e thatoligodendrocytesand
astrocytessigni

cantlycontributetolearningplasticityand
FIGURE1
Architectureof anOIsystemforbiologicalcomputing.Atthecore ofOIisthe3Dbraincellculture(organoid)thatperformsthecomputation.The
learningpotentialoftheorganoidisoptimizedbycultureconditionsandenrichmentbycellsandgenescriticalforlearning(includingIEGs).The
scalability,viability,anddurabilityoftheorganoidare supportedbyintegratedmicro

uidicsystems.Varioustypes ofinputcanbeprovidedtothe
organoid,includingelectricalandchemical signals,syntheticsignalsfrommachinesensors,andnaturalsignalsfromconnectedsensoryorganoid
s
(e.g.retinal).Weanticipatehigh-resolutionoutputmeasurementbothbyelectrophysiological recordingsobtained
via
speciallydesigned2Dor3D
(shell)MEA,andpotentiallyfromimplantableprobes,andimaging of organoidstructural andfunctionalproperties.Theseoutputscanbeused
directlyforcomputationpurposesandasbiofeedbacktopromoteorganoidlearning.AIandmachinelearningare usedthroughouttoencodeand

decodesignalsandtodevelophybridbiocomputingsolutions,inconjunctionwithasuitablebig-datamanagementsystem.
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
05

memorysuggeststhattheseprocessesshouldbestudiedfrom a
neuron-to-gliaperspective,ra
ther thantheneuron-to-neuron
paradigmgenerallyused(
63
Œ
65
).Inaddition,optimizingthecell
cultureconditions toallowtheexpressionofimmediateearlygenes
(IEGs) isexpectedtofurtherboostthe le arn ingan dmemory
capac itiesofbrainorgan oidssin cetheseareke ytolearnin g
processesandareexpressedonlyinneuronsinvolvedinmemory
formation
Œ
asdetailedbelow.
Scalingupthese3Dorganoidsisa keyearlyaim.Wesetoutto
produce brain organoidswithabout10 millionneuralcells(
66
).
Existingdifferentiationprotocolsforscalingupthecultures,and
starting3Ddifferentiationdirectlyfrom iPSC(bypassingthe
inte rmediategene rationofne ur
oprogenitorcells),are v ery
promising (
67
,
68
).Thesedevelopmentsbene

tfromgeneral
progressinmicrophysiologicalsystems(MPS),wh ichinclude
organoids,andaimtoestablishorganarchitectureandfunctionality
FIGURE2
Advancesin3Dcellculturingprovidethefoundationforsystemsto exploreorganoidintelligence.
(A)
3Dneuralcellcultureshave importantadvantages
forbiologicallearning,comparedwithconventional2Dmonolayers
Œ
namelyafar greaterdensityofcells,enhancedsynaptogenesis,highlevelsof
myelination,andenrichmentbycelltypesessentialtolearning.
(B)
Brainorganoiddifferentiationovertimefrom4to15weeks,showingneurons
( mic ro tubul ea sso ciat edpr ote in2[ MA P2 ]; pi nk ),o li go den dr oc ytes( ol ig od endr oc yt et ra nsc ri pt io nfa cto r[ OLI G2] ;r ed) ,an dast ro cy te s( gl ial

brillaryacidic
protein[GFAP];green).NucleiarestainedwithHoechst33342(blue).ImagesweretakenwithanLCM880confocalmicroscopewith20x and63x
magni

cation.Scalebars are100
m
mand20
m
m,respectively.TheimagesshowthepresenceofMAP2-positive neuronsasearlyas 4weeks,while glial
cellsemergeat8weeksandthereisacontinuousincreaseinthenumberofastrocytesovertime.
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
06

such asOIasproposedhere. Notably,somecoauthorsareinvolvedin
spearheadingqualityassuranceguidanceforGoodCellCulture
Practice,expandingearlierguidance tostem cell-basedmodels,
MPS,organ-on-chipmodels(
69
),andestablishinganannualMPS
WorldSummitseries(
70
)andinternationalsociety.
Micro

uidicperfusionsystems
Whilebrainorganoidsm ayrecapitulatespatiotemporal
molecularsignatures,geneexpressionnetworks(
71
),certain
histoarchitectures(e.g.cortexpatterning), andneuronphenotypes
withinthehumanbrain,theydonotre

ect itsregional organization
andthe complexityofitsneuronalcircuitrytolevelsallowingfor
higher-orderbrainfunction(
35
,
72
,
73
).Partofthehumanbrain
™
s
complexitystemsfromitssizeandthevasculaturethatsupportsits
growth(
74
,
75
).Althoughbrainvasculaturemodels are under
development(
76
,
77
),mostbrainorganoidmodelssofararestill
avascularandrelyonpassivediffusiontodelivernutrients; the
averagescopeofdiffusionisapproximately300
m
mbeforestarving-
derivednecrosis occursatthecore(
78
)(
Figure3A
).Thus,thelack
ofaperfusablevasculatureisamajorlimitationforimproving
biologicalcomplexityand
invivo
-likefunctionality(
78
).
Micro

uidicsystemsthatsubstituteforvasculature
Œ
allowing
controlledperfusion ofoxygen,nutrients,andgrowthfactorsand
theremovalofwasteproducts
Œ
willbecriticaltothescalable
anddurableculturingofbrainorganoids(
Figure3B
)(
79
,
80
).These
willsupportthehomeostasisandviabilityoftheorganoids,allowing
amorephysiologic-likedifferentiationtowardamorecomplex,
sophisticated,and
ﬁ
invivo
-like
ﬂ
model.Flexible,s elf-folding
micro

uidicscanalreadydeliverchemicalswith3D
spatiotemporalcontrol(
81
),andrecentadvances in3Dprinting
withsacri

cialmaterialsofferthe potentialtocreateperfusable
scaffoldsfororganoids(
82
,
83
).
Thesemicro

uidicsystemswillalsosupportchemicalsignaling
toorganoids. Theimportanceofspatiotemporalchemical
patternstoencodeinformationiswellestablishedinneuroscience
andbehavioralscience(
84
Œ
86
).Signi

cantadvancesin
micropatterningandmicro

uidicsoverthepasttwodecadeshave
alreadyallowed2D chipstooffersign i

canttunabilityofthe
chemicalmicroenvironmentaroundneurons,andtree-like
micro

uidicgradientgeneratorshavebeen widelyusedtocreate
chemicalpatterns(
87
).Imp ortantly,3Dsp atiotemp oral
micro

uidicinterfaces(
88
)nowenablelocalizeddosingand
replicationofc hemicale nviron
mentswithneurotransmitters,
neuropeptides,andotherneurochemicals.A comprehensivelistof
theagonistsandantagonistsis available (
89
).
High-resolutionrecordingofcomplex
neuronalnetworks
3Dmicroelectrodearraysforbrain organoids
Robustandreproduciblesystemstorecordelectrophysiological
outputsfrombrainorganoidsarecriticaltodevelopingOIsystems
andwillneedtoaddressvariouschallengesinreading andwritingto
complexneural assemblies.Brain-machine interfacetechnologies
havebeeninprogressfor at leasttwodecades(
90
)butremain
primitive.Microelectrodearrays(MEAs) form theheartofmany
suchinterfaces sincetheycanbeusedtobothstimulateandrecord,
FIGURE3
3Dmicro

uidicdevices tosupportscalability andlong-termhomeostasis of brainorganoids.
(A)
Cellswithinbrainorganoidsrequireperfusionwith
oxygen,nutrients,andgrowthfactors,aswellastheremovalofwasteproducts, toprovideconditionsapproximatingphysiologichomeostasis.

Passivediffusionpenetratestoadepth of onlyaround300
m
m,andsonecrosisoccursatthecore of largerorganoidsowingtostarvation.This
preventsbrainorganoidsfrombeingscaledup tothesizeandcomplexityrequiredforOIresearchandlimitstheirdurability.
(B)
3Dmicro

uidic
systemsenablegreaterscalabilityanddurabilitybyprovidingcontrolledperfusionthroughoutlargerorganoids.Theyalsoenable3Dspatiotempo
ral
dosingofchemicalsforsignalingpurposes.
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
07

andofferunprecedentedparallelismandindividualaddressability.
However,mostarepredominantly ina2Dchip-basedformat,being
designedforusewithmonolayercellcultures (
91
).Thisrepresentsa
likelyproblemasbrainorganoidsarespherical3D structuresthat
makelimitedcontact witha2DMEAchip.Furthermore,most2D
electrodechipinterfacesarerigid,and amismatchinthe stiffnessof
therecording interfaceandcellsystemcompromisesperformance
(
92
,
93
).
Therefore,weandothersaredevelopingnovel3DMEA
interfacesspeci

callydesigned fororganoids(
93
Œ
96
)andinspired
bytheEEGcapsusedtorecordbrainelectricalpatternsfromthe
scalp. Organoidsare growninside

exible,ultra-soft-coated,self-
folding,andbuckledshells,coveredwithpatternednanostructures
andprobes(
92
,
93
,
97
Œ
99
)(
Figure4
).Thismodelallows
multichannelstimulationandrecordingspatiotemporallyacross
theentiresurfaceoftheorganoidwithunprecedentedresolution
and highsignal-to-noiseratio,resultingfromthe greatlyenhanced
recordingsurfaceareas(
92
,
93
).Afterthespontaneoussignalis
stabilized andsynchronized,theresponsetorepeatedchemical
stimulifromn eurotransmittergradients[glutamate,
g
-
Aminobutyricacid(GABA),dopamine,serotonin,acetylcholine]
and mainreceptorsagonists/antagonists[e.g.kainicacid,kynurenic
acid,
g
-Amino-
b
-hydroxybutyric a cid(GA BOB),b icuculline,
haloperidol,nicotin e,methylbromide(
89
)]ca n berecordedto
addressandmodulate thesynapticplasticity.
TheseshellMEAinterfacescanbeintegratedwiththe
aforementioned3Dmicro

uidicsystems,supportingthescalability
anddurabilityof thesystemandchemicalsignaling
via
spatial
patterningand gradients.Together,theycreate arobustplatform
togainaniterative,in-depthunderstandingoforganoidbehavior
andresponsestoarange ofhighlymodi

ableenvironmentaland
input stimuli,whichinturnwillallowustoexploretheircapacityto
recapitulatethemolecularmechanismsoflearning andmemory
formationandultimatelytheircomputationalpotential.
High-resolutionimplantable
electrophysiologydevices
WeconsiderthattheshellMEAs described abovestrikean
appropriatebalancebyprovidingcomprehensive,high-resolution
electrophysiolog icalrecordingswithminimaldis ruption tothe
organoid. However,futuresystemsmightpermitorganoidstobe
grownaroundimplantable electrodestofurtherenhancesignal
resolutionandtoaccesstheinsideoftheorganoid.Theef

ciencyof
suchsystems mustbebalanced bytheirinvasivenesssinceany
damageto neuronal networkscouldalterthebehaviorof
theorganoid.
Neuropixelsaresiliconprobesdevelopedforextracellular
recordinginan imals(mostlymiceandrats )(
100
).Theylend
themselvestodirect integrationwithbrainorganoids,thoughin
principle, Neuropixelscanalsobeintegratedintoshells.Theselarge
(10mm),dense(100sites/mm)implantableneuraldevicesallow
therecording ofhundredsofwell-resolvedsingleneuronsignal
traces.Theycanbecombinedwithlightsources,electrical
st imul ation,andphotometry,dramaticallyincreasingtheinpu t
andoutp utopp ortunitiesandthemap pingofactivityinthe
learningorganoid.Thesedevicesalsoappear uniquelycapableof
long-livedexposuretoneuraltissue.Chronicimplants inrats and
micefrequentlylastfor150daysormorewithlittledegradation in
recordedneuralactivity,indicatingsuitablecompatibilityand
stability(
100
,
101
).Recently,theKosiklaboratory(Universityof
CaliforniaSantaBarbara,CA, USA)usedsuchCMOSshank probes
inparallelwith2Dhigh-densityMEAstorecordintrinsicnetwork
activityinbrain organoids(
46
).
Mountingandinsertingsuchprobesintotheorganoidisa
complexcha llenge,a ndworkiso ngoingtodevelopanew
generationofsuitable(more

exible)probes.Iftheorganoidis
growninwellplates,mountingoftheprobe wouldbelikeskull
mountinginarodent.Ifthegrowthmediumneedstobeexchanged
periodically fororgan oidhea lthwithoutdisturbin gtheprobe-
organoidinterface,thenanunconventionalmeansforremoving
andaddingmediatothewellswouldneedtobedeveloped.The
minimumsizeoftheprobebase(4.2mm×1mm)allowssuf

cient
ﬁ
headroom
ﬂ
for this

uidicmachinery.Onceamicro

uidicgrowth
chamberisadopted,amembraneinterfaceto theprobeshank
would beneeded.Neuropixelsareroutinelyusedwitha Kwik-Sil
(WPI)siliconlayeroverthebrainwhilerecordingandsealing
chronic implants.Furtherinvestigationmayberequiredtoperfect
thisgeometry,butinterfacingwithalow-pressure

uidicchamber
doesnotpresentanyfundamentalproblem.Finally,a Neuropixels
2.0probe(
101
)hasfourshanks, each10mmlongwithacross-
sectionof 7 0
m
m×24
m
m. Fora1mmdiameterorganoid,
approximately500electrodeswouldcontactthecells, givingthe
capacitytorecord from384switch-selectablesitesatatime.The
probeelectrodeswould displace~1.5%ofthe currentorganoid
volume,likely anacceptableperturbation.Yieldsof200
Œ
600
ﬁ
units
ﬂ
aretypicalinrecordingsfromrodents,limitedbyactivity.The
probewouldbewithindetectiondistance of~14%ofthecellsina 1
mmdiameterorganoid.
Amongthechallengesfacingbrain-machineinterface
technologiesisthescaleofconnectivity.Corticalneuronseach
haveintheorderof10
4
inputsynapsesandconnecttoin the order
of10
3
cells,someacrossmanymillimeters
Œ
eveninsmallbrains
suchasthoseofmice.Itisnotyetcleariforganoidshavesimilaror
reducedsynapticcounts.Curre
ntbrain-machineinterfaces
havemanyunresolvedcellsperinput(reading)foreach
electrode (allwithin 20
Œ
80
m
m)andalargelyunknownnumber
ofcellsforoutput(writingorstimulation).Exceptforspecial
cases inthevisualcortex,thecellular understandingofwriting
remainsdif

cult,whilereadinghasenabledthecontrolof
prostheticrobots.
Howmighttractionbeachievedtobeginharnessingorganoid
computingpower?Weproposethattwopathsbeexplored.
All-optical
Anall-opticalpathfororganoidswouldallowcell-by-cell
excitationandwholeorganoidread ing(againcell-resolved ).
Whileoptical imagingisnotlikelyaterminal technologyfor
harnessingOI,itallowsexplorationofthesystembehavior,and
the kindsofcomputationthatcouldbeinitially(
102
)performed.
Therearerapidlydevelopingt
echnologiesforlarge-volume
imagingthat makethisattractive.Techniques suchas Bessel
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
08

holographycanimagevolumeswithhundredsof
m
mdiameterat
kHzrates, with anaccuratecellularresolutioniftheactivityis
relativelysparse(
102
).Directly writingwithopsinsisalsowell
established,andh olographicmethods areagainexploited(
103
),
but thecellwritera teissigni

cantlylowerthanthecellread
rate.Thesemet hods areimmediatelyavailableandwouldhelp
informthedesignofelectrophys
iologicalsystemsnecessaryto
progressOI.
FIGURE4
Interfacingorganoidswith3Dmicroelectrodearrays(MEAs)toallow electrophysiologicaloutputrecording.
(A)
Organoid-MEAinterfaceswere
inspiredbytheelectroencephalograph(EEG)usedtotakeelectrophysiologicalrecordingsfromthehumanbrain.
(B)
Organoidsare growninside

exible, ultrasoft-coated,self-folding,andbuckledshellscoveredwithpatternedmultielectrodenanostructuresandprobes.Theseinterfacesa
llow
ultra-high-resolution3Dspatiotemporalstimulationandrecordingofelectrophysiological patternsacrosstheentireorganoidsurface(see als
o
93
).
(C)
Bright

eldimageof brainorganoidcapturedinsidetheshell.
(D)
Confocalimageshowingthesideview(projectedconfocalstack)ofabrain
organoid(green;Fluo-4calciumdye) withadiameter around500
m
mencapsulatedintheelectrodes ofthe3Dshell(blue).
(E,F)
Threechannelsof
electrodesare distributedacrosstheshellwithrepresentativerasterplotshowingthespontaneouselectricalactivityof thebrainorganoid.
(G)
Overlaid spikewaveformfromchannels 1,2,and3.
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
09

High-throughputelectrophysiology
Electrophysiologyrecordingcapacityisimpededbythe
ﬁ
dark
matter
ﬂ
observationresultingfromthefactthatmostneuronsare
not

ringmostofthetime.Assuch,an electrophysiologychannel
sensitiveto readingandwritingindividuallocal neuronscanbe
inef

cient:eventhebest-performingprobes
ﬁ
see
ﬂ
<1%ofthe
neurons within theirdetectionrange (
104
).Itseemsunnecessary
toachieveasynapselevel ofinterpretabilityofthesesystemsifthe
baseprinciplesareelucidated,empiricallytested,andusedto
controlthe systemasawhole.Notably,bionic implantsfor
human shaveman agedtoco n veysigni

ca n tinformation with
relativelyfewinputelectrodes; e.g.thebioniceye(
105
)used24
electrodes,andcurrentcochlearimplantsusebetween10and22
(
106
,
107
).Therefore, differentresolutionsmayberequiredfor
inputvs.output.
AlthoughorganoidEEGand implantableneuraldevicesare
feasibletoinvestigatethescaleofrequiredinput/outputcontacts,
bothtechnologiesneedtobeexploredfurtherto assessthe
recordingpatternsandlearningpotentialofbrain organoids.
Memoryandlearning inorganoids:trainingusing
biofeedback,big data, andAI/machinelearning
U n derstan din gthecapacityofbrainorgan oidstolearnis
fundamentaltodeterminingwhethertheycanbeused
computationallybyharnessingtheadvantagesof biological
learning.Atthisstage,learningisidenti

edasanincreased
frequencytoshowandmemorizearesponsepatterntoa
stimulatorypattern.Weaimtousetheiterationsoftechnologies
describedabovetointerfaceorganoidsandcomputerstoinitiate
supervisedlearn in gsimulations(i.e.tr ain edst imulusr espon se
pattern s).Toac hievethisgoal,thebrainorgan oidsshouldbe
exposedt os patiotemporalpatternsofelectricalandchemical
stimulation,withtheassociatedrecordingsdelineating
relationships betweeninputsandoutputs.Afeedback loopis
requiredto traina learningsystem.Changesinthebrain
organoidarchitectureandfunctionality(synapticconnectionsand
electrophysiology)duetosuchtrainingcyclescanthen beanalyzed.
Thesetwofactorsaffectsynapticplasticity
Œ
themainmechanismof
memoryformationandlearning.Hence,therecordedresponsesto
electricalorchemicalstimulishoulddemonstrate whetherandhow
learningmayoccurintheorganoids.
Ultimately,robust,high-resolutionencodinganddecodingof
signalsgoingintoandoutofhumancorticaltissueisrequired.
Recentachievementsusingintracorticalmicrostimulation(ICMS)
and decodingofmotorand sensorycorticesusingMEAinhuman
subjects offerpromise(
108
,
109
), thoughfurtheradvancesinscale
andresolutionwillbenecessary.
AI analysisofresponses
Organoid-MEAswill generatemassiverecordingdatasets that
willthemselvesneedto beanalyzedbystatisticalandmachine
learningtechniques.Giventherecordingdensityandvolume, this
willnecessitate anovelbig-datainfrastructureandsupercomputing
capacitytailoredtothesophisticated needsofthisformofmodern
biologicaldata.
Fundamentally,thetwomajorchallengesforAIanalysisinthis
contextare:(a)howtodecodetheinputprovidedtoan organoid
(e.g.thegamePong)(
29
)torelatetochangeswithitsarchitecture
and/orfunctionality;and (b)howtorelatetheseorganoid changes
to certainoutputs(e.g.theimprovementinplayingPong). Inother
words,biologicalcomputingincludesOIas amediating
mechanisticprocess betweentheinputsandoutputs.To answer
thesetwochallenges, weforesee theuseof interdisciplinarytools
integratingmachinelearning,s
tatistics,signalprocessing,
informationtheory,andoptimization.Wealsobelieve thatthe
questionsraisedwill motivatenewmethodologicaldevelopmentsin
these

elds.
Speci

cally,webelievethefollowingthreepathsmustbe
exploredtorelateOIinputstooutputs:
1.Machinelearningandstatisticalalgorithmsareneededto
quan t ifyorgan oidfun ctionchan ges. Thisin volves: (a)
sensorintegrationto accelerateprocessingbasedon
unsupervisedlearninganddimensionreduction, suchas
principalcomponentanal
ysis (PCA),independent
componen tan alysis(ICA),an dautoencodersincluding
hierarchicalversions(
110
Œ
112
);(b)signal detectionusing
sequencingandtimeseries(e.g. state-space) models(
113
Œ
115
),whichare oftenusedinbrainimaginganalysis;(c)
patternrecognition toidentifythe realsignalpatternand
deconvoluteit fromthebackgroundnoises(
116
).
2.Algorithmsarealsoneededto quantifyorganoidarchitecture
changes.Challengesincludepinpointingtheexactpartsof
theorganoidthatrespondtotheinput[e.g.usingmixture
models(
117
)]andthenquantifyingthesechangesby
monitoringtheirphysicalappearances.Theapplicationof
multiscaleunsupervisedstructurelearningmethodstothe
recordedresponsescanidenti
fydiscrete,statistically
distinguishable,observer-unbiasedresponsephenotypes.
3. Modelsmustthenbetrainedtorelatethequanti

ed
organoidchangestotheoutputvariables
via
multivariate
causalmodels (
118
Œ
120
).OIwillrequirenovel
developmentsintegrating AI/machinelearningandboth
space-andtime-dependentcausalmodeling (
121
Œ
123
).
Clearly,inferringorestimatingtheconnectivityoforganoids
willbeacoreendeavor.Connectivity,inneuronalcircuits,isusually
dividedintostructural,functional,andeffectiveconnectivity(
124
).
Thedistinctionbetweenfunctional andeffectiveconnectivityis
particularlyprescienthere:functionalconnectivityreferstothe
statisticalcorrelationsbetweenneuronal

uctuationsindifferent
populations,whileeffectiveconnectivityreferstothecausaland
directedconnectivitybetweenpopulations.Thecorrespondingdata
analysistechniquescanbeparsedintofrontalconnectivitymethods
suchascoherenceanalysesandGrangercausality.These canbe
contrastedwithinferencesabout directed(effective)connectivity,
usuallyusingsomeformofdynamic causalmodeling(
125
).
Applyingthesestatisticalandcomputationalm ethodsand
modernbigandcomplex datatools,suchasthosefrom brain
imagingandcomputationalbiology,willallowustomapinputand
outputsfromorganoids
™
neurologicalconnections.Asanexampleof
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
10

arelevant technique,afundamentallydifferentapproachto neuron
behaviormapping wasdevelopedin
Drosophila
:optogenetic
activationof neuronsandtheapplicationofmultiscale
unsupervisedstructurelearningmethodstotherecordedresponses
toidentify discrete,statisticallydistinguishable,observer-unbiased
responsephenotypes(
126
).Thiscouldbeastartingpointfor
connectivity-andactivity-mappingstudiestofurtherinvestigatethe
mechanismsthroughwhichneurons mediatediversebehaviors.
However,withrespecttoitsap
plication tobrain organoid
recordings, weareenteringterraincognita.
Machinelearningandothermathematicalmodelsare
increasinglyappliedtocertainpartsoforganoidresearch(
127
Œ
129
).However,machinelearning,in thesenseofdeeplearningand
supervisedlearning,deservesfurthercomment.Thisis becauseit
presupposes thatsupervisedlearningisanappropriatetheoretical
formulationofself-organizationinorganoids,inthe sensethatthe
opportunitiesaffordedbyorganoidresearch transcendquestions
abouthowtoengineera particular behaviorthroughsupervised
learning(
130
). Theopportunitiesprobablyrequireamore generic
theoreticalframeworkwithinwhichtoformalizeself-organization
andactiveexchangebetweenanorganoidanditsexternalmilieu
(
131
,
132
).Practically,if onewantedtotrainanorganoidto dothis
orthat,itwould beimpossibletoimplementtheprocedures
forsupervisedlearninginmachinelearning(i.e.either
backpropagation of errorsorlocalenergy-basedschemes).
Currentdevelopmentsfavoringreinforcementlearning,where
self-o rganizatio nismetbyfeedba ckonfunctionality, lend
themselves tosuchproblems.Strategically,ifcorrect,thismeans
thatthe directionoftraveloforganoid researchmaybeeither
towardreinforcementmachinelearningormore alignedwithsome
ofthefo undationa lquestion sposedinn eurobiolog y(
133
)or,
indeed,the physics ofnonequilibriumself-organization(
134
,
135
).
Big-data infrastructures
Providingsuitableinfrastructureforthestorage,curation,and
processingofOIbigdataisascienti

cchallengeofitsown. Analytic
datasetsneedtobestoredinef

cientsharedmemorystructures;
appropriatetechnologywillbeneededwheremanipulations,such
asstandardmatrix ortensorcalculations,canbeobtainedwithout
partialorstreamingaccesstothefulldataset. Furthermore,afast,
robust,andscalable compu tationalanalytic andcuration
infrastructure forthe resultin
g datawillbeneeded.A likely
requirementwillbeef

cientdime nsion-reducingtr ansformsof
the 3Dsensora rraysapplicable
for streamingdata;e.g.by
ﬁ
scatteringtransform
ﬂ
(
136
),whichhasbeenparticularly
successfulinanalyzingaudiostreams(
137
).
Eachdeepbiologicalnetworkcomputessomefunction,
transforminginputsto outputsdependingonmanyvariables,
chiefamongthem:(1)theweightsandbiasesand(2)the
activationfunctions.InbothAIand OI,itisreasonablysafeto
assumethattheactivationfunctionsareessentially static;i.e. any
givennodeatanygiventimeis activatedonlyuponreachinga
certainthreshold.However,Sinapayenetal.(
138
)suggestthat
neuralnetworkscanautonomouslychangeactivitytoavoidexternal
stimulation.ThekeydifferencebetweenAIandOInetworksisthat
inOInetworks,theweightsandbiasesmaydynamicallychange
overtime
Œ
forexample,owingtogrowth and/ormaintaining
homeostaticequilibrium
Œ
however,withunclearchangesinthe
networkfunction .Indeed,vastlydifferentn euralnetwork sca n
implementapproximatelythesamefunction(
139
).Asimilar
resultiswellestablishe
dinbiologicalnetworks (
140
).We,
therefore,hypothesizethatalthoughthepreciseweights and
architectureoftheOImaybedynamic,thememoriesmaybe
stableovertime.
Theamountofdata andrespectivecuration,compression,
andprocessabilitywilldramaticallyincreasewithboosted
electrophysiologicalrecordingsfromOI systems.Additional
challengescomefr omspatiotemporalrecordingandthe
combinationofelectrophysiolo
gy and h igh-contentimaging.In
addition,thetrainingandexperimentaldatacreatedwillrequire
ef

cientframeworksforstoragea nd
analyses.This couldincludea
combin ationof
invivo
proto-neuralnetworksdevelopedinbrain
organoidsand
insilico
analog/digitalhybrid,a nd/or
neuromorphic computing(
41
,
90
,
141
,
142
).Transmedia
progressivelearningwillt hereforeexhibitt headvantagesof
bothbiologicalandmachinecomputingandlearning,while
mitiga tingthelimita tions ofeach.Themaina spect ofour
strategyforstorage istodevelopascheme resemblingthe Large
HadronColliderexper imentatCERN,wher es ophisticat ed
triggersareusedtodetecteventsinrealtimeandonlyevents
withapotentialdiscoveryvaluearekept
Œ
greatlydecimatingthe
datarate.Weenvisageasimila revent-drivenway ofa na lyzing the
data:wewillsenddiscretestimulitothebrainorganoids,lookfor
coordinatedresponsesinmanychannels,andstore onlythe
discreteeventsrelatedtotheseintervals.Wewilluseinsights
gainedthroughmulti pleversions ofexperiment reductionto
developasensorcorrelationmod
elandoptimaleventtriggers
thatoptimizethetrade-offsbetweendatareductionand
discoveryvalue.
Manylargeongoingeffortsaim tocreatedata-processingtools,
storagesolutions,andstanda
rdstohandlethescaleofdata
generatedbymodernneuroscienceexperiments,e. g.theUS
BRAINInitiative(
143
).Open-sourcecommunitysolutions,which
the OIcommunitycouldleverage,arebeingdevelopedforterabyte-
and evenpetabyte-scaledataacrossmultiple modalities.As high-
throughputMEAsrepresent the mostpromisinginitialtechnology
forinterfacingwithorganoids,solutionsfromtheinvasiveand
in
vitro
electrophysiologycommunitiescanlikelyserveasthebasisfor
theOIcommunity.Standardized community-processingpipelines
existforthisapplication,includingmachinelearningtools suchas
DataJointElements(
144
).Manyindividualtoolsandtechniquesfor
electrodearrayshavebeendevelopedforspikesorting(
145
)and
analysisoflocal

eldpotentials(
146
).Communitycloud-based
archivesareavailable forpublishingsuchelectrophysiological data
inanopenandaccessiblemanner,such astheOpenNeuroArchive
(
147
)andDANDI(
148
).These archivesarehostingan ever-
increasin gran geofdatafromvariedexperimentalparadigms.
Severalstandardsinitiatives couldbeleveragedtofacilitatereuse,
reana lysis,andmeta-analysis,suchastheBrain Imagin gD ata
Standard(BIDS)(
149
)orNeurodataWithoutBorders(NWB)
(
150
). Byleveraging thestandards,processingpipelines,storage,
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
11

anddisseminationtechniquesdeveloped by thelarger
electrophysiologycommunity,the OIcommunitycan rapidly
establisha robustandreproduciblebig-datainfrastructure.
Lookingtothefuture,additio
nalimagingmodalitiesmay
becomecriticalto providingfurtherinsightsintoorganoid
functionandlearning.Otherprocessingtools andarchivesexist
forrelevantmodalitiessuchas

uorescencemicroscopyandalso
otherformsofmicroscopy; forexample, theCaImAnpipelinefor
calciumimagingdata analysis(
151
)andtheBrainImagingLibrary
(
152
) forarchivingandstorage. Intheinvasive
invivo
neuroimagingcommunity,functional and structuralconnectivity
(orconnectomics)isalsobeingstudied withimprovedresolution
andlargervolumes(
153
,
154
).Cloud-basedprocessing pipelinesfor
derivingconnectivityareunderdevelopment(
155
),andtheBrain
ObservatoryStorageServiceandDatabase(BossDB)ecosystemhas
been developedtohostandarchivelargeconnectivitydatasetsatthe
neuron-synapse level (
156
).Manyemerginggraphanalysistools
enable improvedinsight,suchasst atisticalcharacterizationof
connectomics(
157
)andidenti

cationofrepeatedmotifs(
158
).In
time,multimodal dataset sandinfrastr ucturemayplayan
importantroleinthedevelopmentoftheOIcommunity.
Ultimately,theOIcommunityshouldseektobuildonthese
toolstoestablishstandardizedanalysisand storage infrastructures.
Opendatasharingcan be apowerfulapproachtogrowthe
communityandmaximizethereuseofexperimentaldata.
Establishingalarge-scale,standardizedsetofexperimentaldata
mayrapidlyimproveprocessingtools,provide theoreticalinsight,
andgeneratehypothesesforfutureexperiments.Aninteresting
modelapproachistheHumanConnectome Project(
159
),which
usedstandardizedapproaches
tohigh-resolution magnetic
reson anceimagingtoproduce agol d-stan darddataset forthe
emerging

eldofhumanconnectomics.A s imilardataand
infrastructureeffortfortheOIcommunitycouldprovide
invaluableinsights.
To summarize,a big-dataecosystemnecessarytostudy OI
willrequire:
†
Standardizationofexperim
entaldataandmetadata,
buildingonexistingstandardssuchasBIDSorNWB
†
Robust,repeatable, andstandardizedprocessingpipelines
thatscaletolargeelectrophysiologicaldatasets
†
Ef

cient,accessible,andopendatastorage,possibly
leveragingexistingcloudarchivessuchasOpenNeuroor
DANDI
†
Thepotentialdevelopmentofmultimodal OIdatasets
†
Theestablishmentofstandard,referencedatasetsforthe
community
Inthe foregoingdiscussion,wehaveanticipatedaneedforthe
collation,storage,anddi ssemination ofbigdata,underthe
assumptionthatorganoid researchwillrecapitulatedevelopments
inneuroscience(andinparticularimagingneuroscience).However,
thereisanalternativepath,whichre

ectsamovefrom
ﬁ
bigdata
ﬂ
to
ﬁ
smartdata.
ﬂ
Inother words,weneedonlyinformativedatathat
enablespeopletoanswerwell-posedquestions.Ineffect, thiswould
representapushbackagainstbigdataandareturntocarefully
designedexperimentsthat elicittherightkindofdata tomake
inferencesaboutthedynamics, plasticity, andfunctional
architecturesinbrainorganoids.Inshort,theexperiencesofthe
neurosciencecommunitymayusefullyinformthekindofresources

neededtorealizethefullpotentialoforganoidresearchoverthe
ensuingyears.
Advancingbiocomputingcomplexity
Optimizedalgorithmsfororganoid-
insilico
interactions
Realizing thepotential ofOI requires morethaninterfacinga
computer withanorganoid.InOI,theorganoidcantakeontherole
ofanembodiedagentthatinteractswith anenvironment through
theorganoid-
insilico
interface.Thiswillreq uireoptimized
algorithmsfororganoid-
insilico
interactionsaswell asresearch
intotheoreticalframeworksforlearningandadaptationsin
organoidsdrawingfromthetheoreticalneuroscienceliterature.
TheviabilityofOIisdepen denton optimizedalgorithmsfor
organoid-
insilico
interactions,inadditiontothefastdatastorage
andretrievaldescribedabove.
There aretwobroadenvironmentsinwhichOImayoperate:
open-looporclosed-loop:
†
Open-loopinvolvesfeedingi
nformationintocellsand
measuringthe response.Recentworkleveragingthis
approachhasfoundthatneuralsystemscanaltertheir
activitytoperformvarious tasks,includingcontext-
dependentencoding(
160
)andblind-source separation
(
42
), andt odisplayfeaturessuch asadaptiontoward
scale-free dynamics(
161
) orlong-termactivity-dependent
plasticity (
41
).
†
Closed-loopextendstheopen-loop environment to include
feedbacktothen euralsystemsabouttheresultofthe
systemactivit y.Examplesof this arelimitedowingto
technicald if

culties, buthigh-latency/low-temporal
resolutionanalysissuggeststhatundertheseconditions,
culturescandemonstrate changesinneuraldynamics(
41
)
andarbitrarylearning(
44
). Moreover, r eal-time
implementation shaverecen tlyres ultedingoal- directed
learningdisplayedthroughachangeinneuralculture
activitywhenappliedinlinewit hneurocomputational
theories(
29
).
Exploring,applying,andre

ningempiricallysupported
theoriesofwhatfundamentallydriveslearningintelligenceisa
criticalfactor.Sofar,numeroustheorieshave beenproposedto
explainhow,at thefundamentallevel,neuralsystemsprocess and
respondtoinformation.
The

rstbranchoftheoriesfocusesonhowneural systemsare
organized,bothstructurallyandfunctionally.Keynotionsinclude
neuralcriticality(
162
),neuralDarwinism(
163
), cellassemblyand
Hebbianplasticity(
164
),rule-basedlearning(
165
),andcoreideas
behindpopulationcodingapproaches(
166
,
167
).Generally,these
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
12

theoriesaimtoexplainhowtheincrediblycomplexorganization
withinthebrainresultsinitsultimatefunctioning.Thus,theyoffer
generally compatibleframeworksforanalyzingandinteractingwith
brainorganoids,providingthe opportunityforoptimizedinputand
decoding ofoutput.
A second
ﬁ
optimization
ﬂ
categoryoftheoriesgenerallyfocuses
onhowasystemoragentworkstomaintainhomeostasisina
dynamic environment.Broadly,thiscanbeachievedeither through
maximizingautilityorrewardorby minimizingsurpriseor
uncertainty (
165
,
168
).KeytheoriesincludetheBayesianbrain
hypothesis (
169
),ef

cient codingh ypothesis(
170
),value-
dependentl earning(
171
),optimalcontroltheory(
172
),and
learningby stimulat ionavoidance(
138
).Attemptshavebeen
madeto unifythesetheories, recentlybyexploringtheunderlying
co mpatibilities,mostn otably thro ughtheproposalofthefree
energyprinciple(
173
),wherethesystemor agentmayengagein
activeinferencetoconstructagenerativemodel oftheexternal
environ mentan dactin aman nertominimize t hedifferen ce
betweentheinternal modelandtheperceived externalworld.At
present,itisdif

culttoempiricallytest many ofthesetheories ina
controlledmanner because
invivo
organismspossesscompensatory
mechanismsthathamperthe interpretationofresults.OIoffersa
pathwayforhighlycontrolledex
perimentstoempirically test
thesetheories.
Inaddition toframeworksforlearninginneuralsystems,theOI
communitywillrequiremethodstoassessembodiedintelligence;
i.e.computationalapproachesto understandintelligentbehaviorin
organoidsforboth open-loopandclosed-loopenvironments.
Previously,
invitro
experimentshavedemonstratedtheabilityof
cellculturestocontrolboth physicalroboticsystemsandsimulated
videogames(
29
,
174
).ExperiencewithintheAIcommunity
suggeststhattheOIcommunitywilllikely bene

tfrom
standardizedtestingenvironmentsandconditions,accounting for
variabilityand constraintsininput/outputinterfacingintermsof

chan n elcountan dban dwidth.TheAI rein fo rcementlea rn in g
commun ityhasproducedahuge range of games,simulation
environments,andphysicalsystemsthat couldbeadaptedtoOI
evaluation.Ofparticular interest totheOIcommunitymaybethe

eldofcontinualorlifelonglearning(
175
,
176
),whereembodied
agentsareassessedinlearningthatoccursoverasequenceof
experiences(oftenreferredtoasa
ﬁ
lifetime
ﬂ
).Suchtesting
environmentsmayserve the O
Icommunitybyproviding
importantbenchmarks forunderstandingfunctionalactivityand
learninginorganoids.
Incorporatingcomplexbiological
inputsinOI
Previous sectionsdescribehowweintendtointerfaceorganoids
and computers.Combining organoidswithvarioustypesofmore
complexinputsandoutputstimulationandrecordinginterfaces(
177
,
178
)willallowustounderstandthepotentialforreal-timecontrols.
The consequencesof suchinterconnectionscan be explored,starting
withtwobrainorganoids,onewithcomplexinputandonewith
complexoutputconnections.Asensoryorgan,suchasaretinal
organoid,couldthenbeconnectedwithabrainorganoid.Eventually,
networksoforganoidswillbeinterconnectedtoimplementmore
complexOI.Theorganoidwillbeinterfacedwithelectricaland

uidic-sensingandsimpleoutputscontrollingmachinesthrough
biofeedbackon thecellularlevel;i.e.giving thebrainorganoid
controlbyfeedingbacktheresultsofitsinducedactions.
Byconnectingretinalandbrainorganoidswecandetermine
whethersignalscantransferbetweenthesedifferent neu ronal
organoidsand howthisexogenousbiologicalsignalingwill be
interpretedbythebrainorganoid
Œ
establishingtheinitialbaseline
oforganoid
Œ
organoid communication.Retinalorganoidsc ontaining
laminatedretinaswith outgrowth ofoutersegment-likestructuresand
synapticribbonshavebeendeveloped(
179
,
180
). Synapseformation
betwee ntwoorganoidsiscompl e xandwasdemonstra te drece ntlyin
assembloid s(
48
). Retinalandbrain organoidscanbeconnectedeither
throughelectrodesordirectly.Sincemethodstogenerate mature,
endogenous,light-sensingretinaarepr eliminaryandveryinef

cient,
engineeredphotosensitiveionchannels,whichareexpressedunder
thecontrolofaphotoreceptor-speci

cpromoter(
181
Œ
183
),can
substituteasaproxyforlight-reactivephotoreceptors.Optimization
ofretinalorganoid cultureconditionstopromotemorerobust
signalinghasrecentlybeenpublished(
184
).
Understandingandperhapsevenin

uencingtheconnectivity
ofretinalandbrainneuronswouldbe extremelyexciting.Although
weandothersareac tivelyinvestigatingwaystoestablishan d
modulatetheseconnections,wearestillquitefarawayfroma
syst emt hatcandemons trat erobust lymodifyingneuronal
connectionsinadirectedmanner.Ultimately,weaimtobuildon
thissimpli

edapproximationorrepresentationofvisualinpu t
towarda systemthatmorefullyapproximates vision.
Leveragingadvancesinthe molecularbasis
ofbiological learning
Advancesinthemolecularbiology ofsynapticplasticitywillbe
critical foroptimizingthecapacity oforganoidsystems forlearning
andOI.Growthconditionscannowbeoptimizedtoalloworganoid
neuronstooptimally expressgenesessentialfor learninginthe

humanbrain.
First,th eyneedtoexpressgenescodingfortheneurotransmitter
receptorsthatmediate synaptictransmission.Wehavealready
characterizedtheexpressiondynamicsofdifferentsubunitsoftheN-
methyl-D-aspartate(NMDA) glutam
atereceptorduringdifferentiation
(unpublishedobservation).Thelong-termorganoidmaturationand
agebasedongeneexpressionand swi
tchofthemainreceptorsubunits
wererecentlyextensivelycharacterized(
185
). Themachineryofthe
organoid
™
sbiochemistry,especiallyof
neurotransmitters,willbean
importantpartofunderstandingthesignalingcascadesandsynaptic
plasticitynecessaryforlearning;tothisend, athorough
characterizationofprotei
n e xpression iswarranted.
Secondly,itwillbeimportantfororganoidstoexpressIEGs.
IEGs mediatesynapticprocessesessentialtomemoryconsolidation
andarerapidlytranscribedin
adultneuronsastheyprocess
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
13

info rmation (
186
).Moreo ver,eviden ceindicatesthatIEGsare
requiredforcircuitscapableofgammafrequencyrhyt hmicity
(
187
), whichisassociatedwitha
ttentionandinformation
processing.UsingRNA-sequencingto compareorganoids(at
differentstagesofmaturationandgrownunderdifferentculture
conditions)withfetal,adolescent,andadult brainswillallowthe
identi

cationofgrowthconditionsthat optimizeexpressionof
theseessentialgenes.ItiscriticaltoensureIEGexpressionthat is
robu standdynamicallyresp onsivetoactivityevokedbya
pharmacologicalblockofGABA
A
inhibiti on(e.g.using
bicuculline).Dynamic,activity-dependentIEGexpression would
assurethepresenceofmolecularsubstratesnecessaryfor organoids
toestablishcircuitswithbalancedexcitatoryandinhibitoryneurons
andsynapses.Thecellcultureconditionsshouldbeoptimizedso
that 10
Œ
30%ofneuronsexpress IEGsinresponsetoinformational
inputs.Thislevelofsparsityistypical ofbrainregionsinvolvedin
learningandmemory(includingthehippocampusandneocortex)
andmay ensurethatmultipleensemblescanbecreatedto uniquely
encode differentstreamsofdata.Thiscontrastswiththeglobal
activationofIEGsthatmayoccurwithnon-informationalactivity,
suchas aseizure.IEG expressionand/orassociatedreporterscan
alsoprovideameanstoassesstheformationofensemblesof
neuronsthatarestably linkedtospeci

cinpu ts.Inthebrain,
suchensembles arethoughttorepresentmemoryengrams.EEG
datacanthenbecorrelatedwithdynamicactivityreporters(Ca
2+
or
voltage)andIEGexpressiondata.Ultimately,neuronalactivitycan
bestimulatedandrecordedoptogenetically,asrecentlydescribed
(
48
).Toourknowledge,IEGexpressionhasnot previouslybeen
utilizedasanendpointforoptimizingorganoidgrowthconditions.
Successfuluseofthisparameterwouldestablishabiologicalbasis
fo rOIan daddressco n cern sregardingtheun certaintyofthe
devel opmentalstate oforganoidsan dtheirpotentialutilityas
information-processingmemoryunits.
OI-ledadvancesinmedicalresearch
andinnovation
Inadditiontopioneeringtheuseofhumanbrainorganoidsfor
computingandlearning,OIresearchwillalsoallowthe exploration of
inter-individualneurodevelopm
entalandneurodegenerative
differencesbetweenstemcelldonors.Alzheimer
™
s diseaseandother
dementias couldrepresentoneparticularlyimportantpriorityfor
research.Globally, morethan55millionpeoplearelivingwith
dementia,andthisnumberisprojectedtoexceed150millionby
2050(
188
,
189
).Dementiaisamongthetop10leadingcausesof
death(
190
)andgloballycostsatleast$1 trillion annually(
191
,
192
).
ClinicaltrialsofnovelAlzheimer
™
sdiseasetherapieshaveshownvery
poorsuccessrates,inpartowing toprematuretran slationof
successfulresults inanimalmodelsthat mirroronlylimitedaspects
of thepathologyinhumans(
193
,
194
).TheadaptationofOIresearch
modelstoneurodegenerative diseaseswouldofferthe

rsthuman-
basedpreclinical modeltohelpusunderstandanddevelopeffective
treatmentsforthesedevastatingdiseases.
Inadditiontoneurodegenerativediseases,neurodevelopmental
disordersalsolendthemselvestoOI,giventhatthedifferentstagesof
braindevelopmentarere

ectedinthe bioengineeringofthesemodels
fromstemcells.Conditionssuchasautismaremajorconcernsowing
totheenormousincreaseinprevalence.IntheUS,autismspectrum
disorder(ASD)wasdiagnosedinthe1970sin1in10,000children,
butaccordingtotheCentersforDiseaseControl(CDC), in2021it
was1in44(
195
).Whilethedisorderhasheritableaspects,
environmentalin

uencesareanincreasin gfocus.Thebrain
organoidmodelhasshownpromiseforboth developmental
neurotoxicity(
196
,
197
)andgene×environment (
198
)studiesof
autism.Avaryingcombinationofcognitiveimpairments
characterizesthis complexspectrumofdiseases (
199
).Similarly,
le ukody st rophi esareadiversegroupofraregen eti cdisorders
affectingwhitematterandlinkedtocognitiveimpairment(
200
).
UsingOItoexplorethegeneticbasisofautismorleukodystrophies
appears torepresentan importantpathtounderstandingthese
disordersand toallowingscreeningofpotentialdrugsthatmight
boostunderdevelopedcognitivefunctions.
Schizophreniaaffectsaround1%ofthepopulationworldwide
andisoneofthetop10illnessescontributingtotheglobalburden
ofdisease(
201
).Schizophreniahasaprominentgeneticbasis,andit
hasbeensuggestedthatitmaybeneurodevelopmental inorigin
(
202
).Prenatalcomplicationsareanimportantcontributortothe
condition (
203
),while cognitivedysfunctionisahallmark(
204
),
withastrongsimilaritytoautism(
205
).HumaniPSClines,e.g.with
geneticbackgroundsassociatedwithdisorders,areavailableand
continuouslygrowing[e.g.SFARIbaseforautism(
206
)].Organoids
developedfromiPSCsfromindividuals withvariousconditions
could becompared againstcontrolsamplestohelp identify
differencesthatmayelucidatethepathogenesis,riskfactors,and
treatments.TheapplicationofanOIapproachusingthese celllines
would thusbeverypromisingto aidfurtherunderstandingand
characterizationoftheetiologyoft heneurodegeneration,

n eur odevelopmental, andpsychiatricdisorders. Thisen ablesa
multitudeof applications,fromde-risking(pediatric)drugsfor
adverseeffectsoncognitivedevelopment(
207
),theidenti

cationof
toxicantsan dillicitdrugswith long-termeffectsoncogn it iv e
capabilities,andtheoptimizationofleaddrugcandidatesacting
onrespectivepharmacologicaltargets.
The studyofmemory,learning,andcognition
Œ
andtheimpactof
neurodegenerationonthese functions
Œ
willrequire physiologically
relevantneuron-to-gliaratiosandhighlevelsofbiologicalcomplexity
andinterregionalcommunication. Besidesassembloids(
48
,
208
,
209
),
aspectsofventralanddorsalregionsin theabsenceofexternal
morphogensorgrowthfactorshavebeenrecapitulated(
210
Œ
212
),
highlightingan innateabilityof self-organization inbothcases.
Recently,Cederquistetal.(
213
)demonstratedthat achimeric
assembloidofanearlyorganoidandacluster ofsonichedgehog
(SHH)-secretingcells resultedindorsal-ventral andanterior-posterior
positionalaxes.However,organoidsdonothavepredictableanatomy
norde

nedtopography,andgenerallydonotre

ectthecharacteristic
developmentalasymmetry(
208
,
213
).Nonetheless,brai norganoids
doshowaremarkableself-organ ization alcapacity.Thismight
befurtherenhanced byfunctionaldemands,whichmaybe
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
14

harnessedwhenscalingupthesizeandinducingregional
polarization,therebyincreasingthebiologicalcomplexityofneural
n etworksan d int erregion alcon nect ion stobett erre

ectbrain
architectureandfunction(
48
,
208
Œ
213
). Bioprintingapproaches
mightalsohelphere.
Ethicsofbiologicalcomputing
withorganoids
Creatingahumanbrainmodelwithinputandoutputaswellas
learningcapabilitiesraisescomplex ethicalquestions.At12weeksof
fetaldevelopment,ahumanbrainhasaweightofapproximately3g,
avolumeof approximately3.5ml, and3×10
9
cellsintheneocortical
partofthefetaltelencephalon(
214
Œ
216
). Anadult mouse brain
weighsapproximately0.4g.Incomparison,currentbrainorganoids
have adiameterbelow500
m
minculture,withlessthan100,000
cells.Thematurationofthebrainorganoidisacceleratedbygrowth
factorssothatat10weeksofculture,organoidsshowsomefeatures
(suchasmyelination) thatstartinthefetusafter20weeksof
gestation(
217
).Furthermore,thestimulation withinformation
inpu tmightlea dtoverydifferentorgan oiddevel opment, an d
muchlongerculture periodswouldbe envisagedfortraining
organoids,togetherpossiblyaugmenting cognitivecapabilities.
Theethicalconcernsraisedbybrainorganoid researchhave
mainlyfocusedonquestionsaboutcreatingentitiesthatcould
potentiallyexhibitconsciousness(
45
).Coul dorgan oids
experiencepainand,ifso,wouldtheysuffer
Œ
evenin
rudimentary w ays?Theseconcernsw illmountduringthe
developmentofOI,astheorganoidsbecomestructurally more
complex,receiveinputs,
generateoutputs,and
Œ
atleast
theoretically
Œ
processinformationabouttheirenvironmentand
build aprimitivememory.Thiswill requiredeeperanalysisand
researchregardingthemorallysalientneurobiological featuresthat

contributetohumancapacities,includingconsciousness,andthe
implicationsforOIresearchandimplementationwhensomeorall
ofthese aremet.Articulatingthephysiologicalconditionsthatare
necessaryandsuf

cientforconsciousnessisone ofthemostdif

cult
puzzlesofneuroscience(
143
,
218
).Toassesswhetherorganoids
exhibitthe criteriaforconsciousnesswillrequiresomeconsensusto
bereachedaboutwhatthosecriteriaare(
219
). Workunderway to
uncover theneuralbasisofconsciousnesswillinformtheevaluation
oftheethicalissuesraisedbyOI.However,itwillalsobe important
todistinguish
ﬁ
consciousness
ﬂ
from
ﬁ
sentience,
ﬂ
formally
consideredas
ﬁ
awarenes stos timuli,
ﬂ
i.e. responsetosens ory
input(
220
,
221
).Suchuseofterminologycanbedebatedand
representsacriticalchallengefortheformingOIcommunity.We
usetheterm
ﬁ
sentience
ﬂ
initsmostbasicway,similarto thewayin
whichmanyaspectsofcognitionhavetobeunderstoodasvery
basiccellularmechanisms,nothuman-levelbrainfunctions.Even
recentproposals (
222
)fortheuseoftheperturbationalcomplexity
index(PCI)assumethemorecomplex ideaofphenomenological
consciousnesswhenthebehaviorcouldbeexplainedbysimpler
sentience(
174
).Notably,thesuggestedOIprogramdoesnotaimto
recreatehumanconsciousness,butratherfunctionalaspectsrelated
tolearning,cognition, andcomputing.
Nevertheless,asadvancesinthestructuralandfunctional
complexityofOIsystemsbegintorecapitulateaspectsofhuman
neurobiological(sub)-processes,suchaslearningandcognition,
researcherswill inevitablye
ncounterthe GreelyDilemma:a
situationwherebyincrementalsuccessesinmodellingaspects of
thehumanbrainwillraisethesamekind ofethical concernsthat
originally motivatedtheirdevelopment(
223
).Suf

cientadvancesin
OIwillraise questionsaboutthemoralstatus oftheseentitiesand
concernsfortheirwelfare.Frameworkshave beenproposedto
addresstheseethicalconcernsinresearchpractices(
224
,
225
)butit
remainsunknownwhethertheseproposalsadequatelyattendto
moralconcernsheld bythepublic.Forexample,harmreduction
policiesareoftenunsuccessfulin gainingpublicsupportwhenthe
underlyingattitudeisbasedonamoralconviction(
226
)with
implication sfo rpublicdisc ours e (
227
).Comprehensiveethi ca l
analysisofOIwillrequireinputfromdiversepublicsandrelevant
stakeholdergroups(
228
),inorderto(i)preventmisunderstandings
fromcreatingunintendedmoralappraisals,and(ii)andfostertrust,
con

dence,andinclusionthroughresponsiblepublicengagement.
Notably,moralattitudes towardOImaydependlesson
epistemologicalconcerns mentionedabove,suchastheroleof
speci

ccognitivecapacitiesinassessmentsofmoralstatus,and
moreonontological argumentsofwhatconstitutes ahumanbeing.
Perceptionsof(re)creating
‚
human-like
™
entitiesinthelabarelikely
toevokeconcernsaboutinfringing onhumandignitythatcould
re

ectsecularor theologicalbeliefsaboutthe
‚
essential
™
natureof
thehumanbeing(
229
,
230
).Ourapproachto embeddedethicsin
OIwillseektoidentifyandattend tothese ethicalconcernsby
informingfuturepublicengagementanddeliberationonOI.
Otherissuesanticipatedtorequireattentionincludeprivacy
concernson thepartof iPSCdonorsandaspectsof intellectual
property.Whatdoestheorganoidexhibitaboutthecelldonor?Is
thereamoralobligationtoinfo rmthedonorif,fo rexam ple,
somethingrelevanttotheirhealthisidenti

edduringresearch?
Dodonorshaverightsthatextendbeyondthedonation?
Incommonwithotherscienti

candbioengineeringaspectsof
OI,thisis trulyunchartedterritory.Theethicalconsiderations
andviewpoints canbeexpectedtoevolvewithanincreased
understandingofo rganoidsyste
ms.Itisthereforecriticalto
frametheethical considerationsattheonsetofthisresearchin
amannerthatencompassesallanticipatedissues,andwhich
continually re

ectsonprogressandnewlessons.Weproposeto
usean
ﬁ
embeddedethics
ﬂ
approachwherebyanethicsteamwill
identify,discuss,andanalyzeethicalissuesasthey ariseinthe
co urseofthiswork.Embeddedethicsisastandardapproachin
interdisciplinarye thicsresearch,
wherebyexpertethicistsjoin and
collaborate integrallyw ithres
earchanddevelopmentteamsto
con s ideran daddr es sethical iss ues
via
aniterativeandcontinuous
processastheresearchevolves(
231
).
Box1
offersa preliminary
frameworkofethicalconsiderationsinformedbydiscussionsat
the
ﬁ
Firstorganoidintelligence(OI)workshopto formanOI
communit y
ﬂ
workshop (22
Œ
24 February2022)(
51
).
Whiletheembeddedethics approachprovidesamechanismfor
investigatingthe philosophicalandscienti

cconditions relevant tothe
moralstatusofbrainorganoids,ithasnoinherentmechanismsfor
seeking,identifying,orincorporatingpublicvaluesinthedevelopment
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
15

ofOI.Itisimportanttounderstandpublicperceptions ofOI,andthis
cannotbedelegatedtoethicistsalone.Itneedstobeembeddedwithin
the

eldasathree-wayfeedbackloopinvolvingresearchers, ethicists,
and membersofthepublic,including stakeholderswhocould be
especiallyimpactedbyadvancesinOI(e.g.neurodiversityadvocates).
Thisfeedbackloopwillenablespeci

capplicationsofOIto be
articulatedbyresearchers,analyzedbyethicists basedontheoretical
principles,andevaluated by membersofthepublicwithdiversemoral
perspectives. Theviewsexpressedbythepublictheninformthework
ofbothscientists andethicists seekingtoadvanceOIinasocially
responsivemanner.Thiscallforpublicdialoguehasbeenechoedbya
NationalAcademyofSciencesreportonhumanneuralorganoids
(
232
),the recommendationson innovationinneurotechnologybythe
OrganisationforEconomicCo-operationandDevelopment(
233
),
andvariousneuroethicscommittees.Moreover,researchersinscience
communicationanddeliberativede
mocracyhavedemonstratedthat
deliberativetechniquesareoneofthemosteffective mechanismsfor
informingthepublicandmitigatingtheriskof polarization on
contentiousissues.F inally,publicengagementonOIwillnotonly
benecessarytopreventadversepublicreactionsbutwillalsomaximize
thefuture impactofthe

eldandserveasanexemplarof howto
embedsociet ywithinscience.
O frelevanceinthiscontext,coauthorJ Kco-chairedthe
neuroe thicssubc ommitteeforthe n ewstrategicplanfo rNIH
BRAIN2.0(
234
).The onlyprojectweknowofwithrelevant
parallel aspectsistheBrainstormProjectledbyInsoo Hyun at
Case Western University(
235
).Wewillbefurtheractivelypromoting
discussionsbetweenbiologists,ethicists,andphilosopherswhoare
interestedinbrainorganoidsandnavigating brainorganoidethicsin
research,aswedidbefore(
219
).Arecommendedwayforwardwould
include:(1)anagreementoncommonlyusedlanguage,(2)the need
forresearchontheneuralbasisfor consciousness(as above);and(3)
thedevelopmentofbestpracticeguidelinesthatconsidertheviewsof
allrelevantstakeholders.
Conclusion:anactionplan
for OIresearch
Wepresentacollaborative,iterativemultidisciplinaryprogram
aimingtoestablishOIasaformofgenuinebiologicalcomputing that
harnessesbrainorganoidsusingthe scienti

candbioengineering
approachesdescr ibed hereinanethicallyrespon sibleman n er
(
Figure5
).Ultimately,weaimtowardarevolutioninbiological
BOX1
Preliminaryframeworkofethicalconsiderationsinorganoidintelligenceresearch.Organoidintelligenceresearchentailsmanyimportant
ethicalaspectsthatwarrantaniterative,collaborativeethicalprocessasthe

eld develops,involvingallrelevantstakeholders.Hereweoffera
preliminary frameworkofissuesforconsideration.
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
16

computingthatcouldovercomemanyofthelimitationsof silicon-
basedcomputingandAIandhavesigni

cantimplications
worldwide.Speci

cally,we anticipateOI-basedbiocomputing
systemstoallowfasterdecision-making (including onmassive,
incomplete,andheterogenousdatasets),continuouslearning during
tasks,andgreater energyanddataef

ciency.Furthermore,the
developmentof
ﬁ
intelligence-in-a-dish
ﬂ
offer sunparalleled
opportunities toelucidatethebiological basis ofhumancognition,
learning,andmemory,togetherwithvariousdisordersassociated
withcognitivede

cits
Œ
potentiallyaidingtheidenti

cationofnovel
therapeuticapproachestoaddressmajorglobalunmetneeds.
Dataavailabilitystatement
Theoriginalcontributionspresentedinthestudyareincluded
intheartic le/supplementarymateri al.Furtherinquiriesca nbe
directedtothecorrespondingauthor.
Authorcontributions
Allauthorslistedhavemadeasubstantial,direct,andintellectual
contributiontotheworkandapproveditforpublication.
Acknowledgments
TheauthorsaremostgratefultoLeeBakerand colleaguesat
Fronti ersforthe professionaleditingof the manuscript.An early
versionofthismanuscriptwassharedwiththe participantsof the
ﬁ
Firstorganoidintelligence(OI)workshoptoformanO I
community
ﬂ
(22
Œ
24February2022)organizedbytheTransatlantic
ThinkTankforToxicology(t
4
)atthe JohnsHopkinsCenterfor
AlternativestoAnimalTesting,and

nancedbytheDoerenkamp-
ZbindenFoundation,Switzerland,theJohnsHopkinsWhitingSchool
ofEngineering,andFrontiers.Whilethep resentationsand
discussionsledtoa parallelreport(
51
),theyhave alsoshapedthis
FIGURE5
Organoidintelligence(OI)actionplanandresearchtrajectories.Ourprogramforeseesassemblingmultidisciplinaryteamsworkinginfourresear
ch
anddevelopment directions(or
ﬁ
trajectories
ﬂ
)employingthescienti

candbioengineering advancesdescribedtoestablishOIasagenuinebiological
computing

eldharnessingbrainorganoidsinaniterativeandethicallyresponsiblemanner.
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
17

articleandtheauthors aremos
tgrateful forthestimulating
discussions.TheworkwassupportedbyaJohnsHopkinsDiscovery
award(toTH)andaJohnsHopkinsSURPASSaward(toTHandEJ).
Con

ictofinterest
THisnamedinventoronapatentbyJohnsHopkinsUniversity
ontheproductionofbrainorganoids, whichislicensedto AxoSim,
NewOrleans,LA,UnitedStates,andreceivesroyaltyshares.TH
andLSconsultAxoSim. JS isnamedasinventoronapatentby the
UniversityofLuxembourgon
theproductionofmidbrain
organoids,whichislicensedtoOrganoTherapeuticsSARL,Esch-
sur-Alzette,Luxembourg.JSisalsoco-founder andshareholderof
OrganoTherapeuticsSARL.AMisaco-founderandhasequity
interestin TISMOO,acompanydedicatedtogeneticanalysisand
humanbrainorganogenesis,focusingontherapeuticapplications
customizedforautismspectrumdisordersand otherneurological
disorderswithgeneticorigins.Thetermsofthisarrangementhave
beenreviewedandapprovedbytheUniversityof California,San
Diego,in accordancewith itscon

ictofinterestpolicies.BKisan
inventoronpatentsfortechnologyrelatedtothispaperalong with
beingemployedatandholdingsharesinCorticalLabsPtyLtd,
Melbourne,Australia.Nospeci

cfundingorotherincentiveswere
providedforinvolvementinthispublication.
Theremainingauthorsdeclarethattheresearchwas conducted
intheabsenceofanycommercialor

nancialrelationshipsthat
couldbeconstruedasa potentialcon

ictofinterest.
Publisher
™
snote
Allclaimsexpressed inthis articlearesolelythoseoftheauthors
anddonotnecessarilyrepresentthoseoftheiraf

liated
organizations,orthoseofthepublisher,theeditorsandthe
reviewers.Anyproductthatmaybeevaluatedinthisarticle,or
claimthatmay bemadebyitsmanufacturer, isnotguaranteedor
endorsedbythepublisher.
References
1.HornyakT.
FujitsuSupercomputersimulates1secondofbrainactivity
.CNET
(2013).Availableat:
https://www.cnet.com/culture/fujitsu-supercomputer-simulates-
1-second-of-brain-activity/
.
2.Herculano-HouzelS.Theremarkable,yetnotextraordinary,human brain as a
scaled-upprimatebrainanditsassociatedcost.
ProcNatlAcad SciUSA
(2012)
109:10661
Œ
8.doi:
10.1073/pnas.1201895109
3.ReberP.Whatisthememorycapacityof thehumanbrain?
SciAm
(2010).
https://www.scienti

camerican.com/article/what-is-the-memory-capacity/
.
4.OrgerMB,dePolaviejaGG.Zebra

shbehavior:opportunitiesandchallenges.
AnnuRevNeurosci
(2017)40:125
Œ
47.doi:
10.1146/annurev-neuro-071714-033857
5.WebbPW.The swimmingenergeticsoftrout. II.oxygenconsumptionand
swimming ef

ciency.
JExp Biol
(1971)55:521
Œ
40.doi:
10.1242/jeb.55.2.521
6.RaichleME,GusnardDA.Appraisingthebrain
™
senergybudget.
Proc NatlAcad
SciUSA
(2002)99(16):10237
Œ
9.doi:
10.1073/pnas.172399499
7.DrubachD.Thebrainexplained.
Pearson
(1999)176.
8.HewlettPackardEnterprise.
HewlettPackardEnterprise ushersin newerawith
world
™
s

rstandfastestexascalesupercomputer
ﬁ
Frontier
ﬂ
fortheU.S.departmentof
energy
™
soakridgenationallaboratory
(2022).Available at:
https://www.hpe.com/us/en/
newsroom/press-release/2022/05/hewl ett-packard-ente rprise-ushers-in-new-era-wit h-

wor lds-

rst-and- fastest-exascale-supercompute r-frontier-for-the-us-department-of-
energys-oak-ridge-national-laboratory.html
.
9.VoraH,KathiriaP,AgrawalS,Patel U.Neuromorphiccomputing:reviewof
ar chit ectur e,issues, applicationsandresear chopportunit ies.In:
Singh
.Springer,
Singapore(2022).
10.LapedusM.Chipletsenterthe supercomputerrace.In:
Semiconductor
engineering
(2022).Availableat:
https://semiengineering.com/chiplets-enter-the-
supercomputer-race/
.
11.GraceK.
AsummaryofAIsurveys
.AIImpacts (2015).Availableat:
https://
aiimpacts.org/transmitting-

bers-in-the-brain-total-length-and-distribution-of-lengths/a
.
12.WuZ,LiuZ,LinJ,LinY,HanS. Lite transformer withlong-shortrange
attention.
arXiv:2004.11886
(2020).doi:
10.48550/arXiv.2004.11886
1 3. GiurfaM,ZhangS,JenettA,Menzel R,SrinivasanMV.Theconceptsof
ﬁ
sameness
ﬂ
and
ﬁ
difference
ﬂ
inan insect.
Nature
(2001)410:930
Œ
3.doi:
10.1038/35073582
14.FleuretF,LiT,DuboutC,WamplerEK,YantisS,GemanD.Comparing
machinesandhumans onavisualcategorizationtest.
ProcNatlAcadSciUSA
(2011)
108:17621
Œ
5.doi:
10.1073/pnas.1109168108
15.JunkyungK,MatthewR,ThomasS. Not-So-CLEVR:learningsame
Œ
different
relationsstrainsfeedforwardneural networks.
InterfaceFocus
(2018)8(20180011). doi:
10.1098/rsfs.2018.0011
16.BorowiecS.AlphaGoseals4-1 victoryovergograndmasterLeesedol.In:
The
guardian
(2016).Availableat:
https://www.theguardian.com/technology/2016/mar/15/
googles-alphago-seals-4-1-victory-over-grandmaster-lee-sedol
.
17.SilverD,HuangA, MaddisonCJ,GuezA,Sifre L,vandenDriesscheG,etal.
Masteringthegameofgowithdeep neuralnetworksandtreesearch.
Nature
(2016)
529:484
Œ
9.doi:
10.1038/nature16961
18.StrubellE,GaneshA, MccallumA.Energyandpolicyconsiderationsfordeep
learninginNLP.
arXiv:[csCL]
(2015)10:4.doi:
10.48550/arXiv.1906.02243
19.KnightW.Facebook
™
s headofAIsaysthe

eldwillsoon
ﬁ
hitthewall
ﬂ
.In:
Wired
(2019).Availableat:
https://www.wired.com/story/facebooks-ai-says-

eld-hit-wall/
.
20.ThompsonNC,GreenewaldK,LeeK,MansoGF.Thecomputationallimitsof
deeplearning.
arXiv:2007.05558
(2020).doi:
10.48550/arXiv.2007.05558
21.SmithB.
MicrosoftWillbecarbonneutralby2030
.Of

cialMicrosoftBlog
(2020).Availableat:
https://news.microsoft.co m/2020/01/16/microsoftannounces-it-
will-be-carbon-negative-by-2030/
.
22.Apple.
Applecommitstobe100percentcarbonneutralforitssupplychainand
products by2030
.Availableat:
https://www.apple.com/uk/newsroom/2020/07/apple-
commits-to-be -100-perce nt-
carbon-neutra l-for-its-sup
ply-chain-and-products-by-
2030/
.
23.MasanetE, ShehabiA,LeiN,SmithS,KoomeyJ. Recalibratingglobaldatacenter
energy-useestimates.
Science
(2020)367(6481):984
Œ
6.doi:
10.1126/science.aba3758
24.GrozingerL,AmosM, GorochowskiTE,CarbonellP, Oyarzu

nDA,StoofR.
Pathwaysto cellularsupremacyinbiocomputing.
NatCommun
(2019)10(1):5211
Œ
50.
doi:
10.1038/s41467-019-13232-z
25.SchmidtE.
FormerGoogleCEOEricSchmidtbelievesbiologyisthenext frontier
incomputing
.CNBC(2019).Availableat:
https://www.cnbc.com/2019/10/02/
ericschmidt-says-hes-eyeing-biology-for-the-next-computing-frontier.html
.
26.vanHooidjonkR.
Howcloseare wetoorganiccomputers?
(2019).Available at:
https://blog.richardvanhooijdonk.com/en/how-close-are-we-to-organic-computers/
.
27.LeeHH, KalhorR,Goela N.Terminator-freetemplate-independentenzymatic
DNA synthesisfordigitalinformationstorage.
NatCommun
(2019)10:2383.doi:
10.1038/s41467-019-10258-1
28.FuY,TsaiTH, MaoC,MunSK, Ressom HW,WangM, etal.
ﬁ
Biological
computing
ﬂ
.FengDD,editor.BiomedicalInformationTechnology(2020)81
Œ
104.
29.KaganBJ,KitchenAC,TranNT,HabibollahiF,Khajehnejad M,ParkerBJ,etal.
Invitro
neuronslearnandexhibitsentiencewhenembodiedinasimulatedgame-
world.
Neuron
(2022)110(23):3952
Œ
69.doi:
10.1016/j.neuron.2022.09.001
30.ChesnutM, Hartung T,HogbergHT,PamiesD.Humanoligodendrocytesand
myelin
invitro
toevaluatedevelopmentalneurotoxicity.
IntJMolSci
(2021) 22
(15):7929.doi:
10.3390/ijms22157929
31.ChesnutM,PaschoudH,RepondC, SmirnovaL,HartungT,ZurichMG,etal.
Human3D iPSC-derivedbrainmodeltostudychemical-inducedmyelindisruption.

Int JMolSci
(2021)22(17):9473.doi:
10.3390/ijms22179473
32.PamiesD,BarrerasP,BlockK,MakriG,Kumar A,WiersmaD,etal.Human
brainmicrophysiologicalsystemderivedfromiPSCtostudycentralnervoussystem
toxicity and disease.
ALTEX
(2017)34:362
Œ
76.doi:
10.14573/altex.1609122
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
18

33.AndersonWA,BosakA,HogbergHT,HartungT,MooreMJ.Advancesin3D
neuronalmicrophysiologicalsystems:
towardsafunctionalnervoussystemona
chip.
InVitroCellDevBiolAnim
(2021)57(2):1 91
Œ
206.doi:
10.1007/s11626-020-
00532-8
34.TrujilloCA,GaoR,NegraesPD, GuJ,BuchananJ,PreisslS,etal.Complex
oscillatorywavesemergingfromcorticalorganoidsmodel early humanbrainnetwork

development.
Cell StemCell
(2019)25(4):558
Œ
69.doi:
10.1016/j.stem.2019.08.002
35.Lancaster MA,RennerM,MartinCA,WenzelD,BicknellLS,HurlesME,et al.
Cerebralorganoidsmodelhumanbraindevelopment andmicrocephaly.
Nature
(2013)
501(7467):373
Œ
9.doi:
10.1038/nature12517
36.Pas


caAM,SloanSA,Clark eLE,Tian Y,Makinson CD,HuberN, etal.
Functionalcorticalneuronsandastrocytesfromhumanpluripotentstemcellsin3D

culture.
NatMethods
(2015)3(7):671
Œ
8.doi:
10.1038/nmeth.3415
37.Alford S,ZompaI,DubucR.Long-termpotentiationofglutamatergicpathways
inthelampreybr ainstem.
JNeurosci
(1995)15(11):7528
Œ
38. doi:
10.1523/
JNEUROSCI15-11-07528.1995
38.KositskyM,ChiappaloneM ,AlfordST,Mussa-IvaldiFA.Brain-machine
interactionsfor assessingthedynamicsofneural systems.
FrontNeurorobot
(2009)
3:1.2009. doi:
10.3389/neuro.12.001.2009
39.TeylerTJ.Useofbrainslicesto studylong-termpotentiationanddepressionas
examplesofsynapticplasticity.
Methods
(1999)18(2):109
Œ
16.doi:
10.1006/meth.
1999.0764
40.TessadoriJ,ChiappaloneM.Closed-loopneuro-roboticexperimentstotest
computationalpropertiesofneuronalnetworks.
JVisExp
(2015)97(52341).doi:
10.3791/52341
41.Bakkum DJ,ChaoZC,Potter SM.Spatio-temporalelectricalstimuli shape
behaviorofanembodiedcorticalnetworkinagoal-directedlearningtask.
JNeuralEng
(2008)5:310
Œ
23.doi:
10.1088/1741-2560/5/3/004
42.IsomuraT,KotaniK,JimboY.Culturedcorticalneuronscanperformblind
sourceseparationaccordingtothefree-energy principle.
PloSComputBiol
(2015)11
(12):e1004643.doi:
10.1371/journal.pcbi.1004643
43.MaromS,ShahafG.Development,learning andmemoryinlargerandom
networksofcorticalneurons:lessonsbeyondanatomy.
QRevBiophys
(2002)35(1):63
Œ
87.doi:
10.1017/S0033583501003742
44.Shahaf G,MaromS.Learninginnetworksofcortical neurons.
JNeurosci
(2001)
21(22):8782
Œ
8.doi:
10.1523/JNEUROSCI21-22-08782.2001
45.SawaiT,SakaguchiH,ThomasE, TakahashiJ,FujitaM. Theethicsofcerebral
organoidresearch: beingconsciousofconsciousness.
StemCellRep
(2019)13(3):440
Œ
7.
doi:
10.1016/j.stemcr.2019.08.003
46.SharfT, vanderMolenT, Guzman E,GlasauerSMK,LunaG,ChengZ,etal.
Intrinsicnetworkactivityinhumanbrainorganoids.
SSRNElectronicJ
(2021)73.doi:
10.2139/ssrn.3797268
47.Smits LM,MagniS,KinugawaK,GrzybK,LuginbuehlJ,Sabate-SolerS,etal.
Single-celltranscriptomicsrevealsmultipleneuronalcell typesinhumanmidbrain-
speci

corganoids.
CellTissueRes
(2020)382:463
Œ
76. doi:
10.1007/s00441-020-03249-y
48.MiuraY,LiM-Y, RevahO,Yoon S-J,NarazakiG,Pas


ca SP.Engineeringbrain
assembloidstointerrogatehumanneural circuits.
NatProtoc
(2022)17:15
Œ
35.doi:
10.1038/s41596-021-00632-z
49.NEUCHIP.EU.(2022).NEUCHIP.EU:BiologicalAI.Availableat:
https://
neuchip.eu
.
50.FaloticoE,V annucci L ,Ambr os anoA
,AlbaneseU,UlbrichS,TieckV,etal.
Connectingar ti

cialbrainstorobotsinacomprehensivesimulationframework:the
neuroroboticsplatform.
FrontNeurorobot
(2017)11(2).doi:
10.3389/
fnbot.2017.00002
51.MoralesPantojaIE, SmirnovaL,Muotri AR,WahlinKJ,KahnJ,BoydJL,etal.
First OrganoidIntelligence(OI)workshoptoformanOI community.
FrontArtifIntell
(2023)6:1116870. doi:
10.3389/frai.2023.1116870
52.HartungT,SmirnovaL,MoralesPantojaIE,Akwaboah A,AlamElDinD-M,
BerlinickeCA, etal. TheBaltimore declarationtowardtheexplorationoforganoid

intelligence.
FrontSci
(2023)1:1068159. doi:
10.3389/fsci2022.1068159
53.TakahashiK,TanabeK,OhnukiM,NaritaM,IchisakaT, TomodaK,etal.
Inductionofpluripotentstemcellsfromadulthuman

broblastsbyde

nedfactors.
CellNov
(2007)30(131):5.doi:
10.1016/j.cell.2007.11.019
54.EirakuM,WatanabeK,Mats uo-T akas aki M,KawadaM,Yonemur aS,
MatsumuraM,etal.Self-organizedformationofpolarizedcorticaltissuesfromESCs
anditsactivemanipulationbyextrinsicsignals.
CellStemCell
(2008)3(5):519
Œ
32.doi:
10.1016/j.stem.2008.09.002
55.MarianiJ,CoppolaG,ZhangP,AbyzovA,ProviniL,TomasiniL,etal.FOXG1-
dependentdysregulationofGABA/glutamate neurondifferentiationinautism

spectrumdisorders.
CellJul
(2015)16(162):2.doi:
10.1016/j.cell.2015.06.034
56.XiaoY,SunAX,CukurogluE,TranHD,GökeJ,TanZY,etal.Midbrain-like
organoidsfromhumanpluripotent stem cellscontainfunctionaldopaminergicand

neuromelanin-pr oducingneurons .
CellStem Cell
(2016)19:248
Œ
57.doi:
10.1016/
j.stem.2016.07.005
57.QuadratoG,NguyenT,MacoskoEZ,SherwoodJL,MinYangS,BergerDR,
etal.Celldiversityandnetworkdynamicsinphotosensitivehumanbrainorganoids.

Nature
(2017)545(7652):48
Œ
53.doi:
10.1038/nature22047
58.SloanSA,DarmanisS,HuberN, Khan TA,BireyF,CanedaC, etal.Human
astrocytematurationcapturedin 3Dcerebralcorticalspheroidsderivedfrom

pluripotentstemcells.
Neuron
(2017)95(4):779
Œ
90.doi:
10.1016/j.neuron.2017.07.035
59.Marton RM,MiuraY,SloanSA,LiQ,RevahO,LevyRJ, etal.Differentiation
andmaturationofoligodendrocytesinhumanthree-dimensionalneuralcultures.
Nat
Neurosci
(2019)22(3):484
Œ
91.doi:
10.1038/s41593-018-0316-9
60.WilliamsonJM,LyonsDA.Myelindynamics throughoutlife:anever-changing
landscape?
FrontCell
(2018)12(424):107
Œ
27.doi:
10.3389/fncel.2018.00424
61.Buyanova IS,ArsalidouM.Cerebralwhitematter myelinationand relationsto
age, gender,andcognition:aselectivereview.
FrontHumNeurosci
(2021)15:66203.
doi:
10.3389/fnhum.2021.662031
62.MonzelAS,SmitsLM,HemmerK,HachiS,MorenoEL,vanWuellenT, etal.A
novel approachtoderivehumanmidbrain-speci

corganoidsfromneuroepithelial
stemcells.
StemCell Rep
(2017)8(5):1144
Œ
54.doi:
10.1016/j.stemcr.2017.03.010
63.WiltonDK,Dissing-OlesenL,StevensB.Neuron-gliasignalinginsynapse
elimination.
Annu.RevNeuros ci
(2019)42:107
Œ
27. doi:
10 .1146/ annurev-neur o-
070918-050306
64.HuangAY,Woo J,SardarD,LozziB,BosquezHuertaNA,LinC-CJ,etal.
Region-speci

ctranscriptionalcontrolof astrocytefunctionove rseeslocal circuit
activities.
Neuron
(2020)106(6):992
Œ
1008.doi:
10.1016/j.neuron.2020.03.025
65.XinW,ChanJR.Myelinplasticity:sculptingcircuitsinlearning andmemory.
NatRevNeurosci
(2020)21(12):682
Œ
94.doi:
10.1038/s41583-020-00379-8
66.KellerD,EroeC,MarkramH.Celldensitiesinthemousebrain:asystematic
review.
FrontNeuroanat
(2018)12.doi:
10.3389/fnana.2018.00083
67.OhY,JangJ.Directeddifferentiationofpluripotentstemcellsbytranscription
factors.
MolCells
(2019)42(3):200
Œ
9.doi:
10.14348/molcells.2019.2439
68.BoussaadI, CrucianiG,BologninS,AntonyP,DordingCM,KwonYJ,etal.
Integrated,automatedmaint enance,expansionanddifferentiationof2D and3D

patient-derivedcellularmodels forhighthroughputdrugscreening.
SciRep
(2021)
11(1):1439.doi:
10.1038/s41598-021-81129-3
69.PamiesD,LeistM,CoeckeS,BoweG,AllenDG,Gstraunthaler G,etal.
Guidancedocumentongoodcellandtissueculturepractice2.0(GCCP2.0).
ALTEX
(2022)39:30
Œ
70.doi:
10.14573/altex.2111011
70.MPSWorld Summit.
2ndmicrophysiological systemsworldsummit
(2023).
Available at:
https://mpsworldsummit.com
.
71.PollenAA,BhaduriA,AndrewsMG,NowakowskiTJ,MeyersonOS, Mostajo-
RadjiMA,etal.Establishingcerebralorganoidsasmodels ofhuman-speci

cbrain
evolution.
Cell
(2019)76(4):743
Œ
56.doi:
10.1016/j.cell.2019.01.017
72 .QianX, S ong H, M ing GL.Brain organoids: advances,ap plicationsand
challenges.
Dev
(2019)146(8):dev166074.doi:
10.1242/dev.166074
73.BhaduriA,AndrewsMG,Mancia LeonW, Jung D,ShinD, AllenD, etal.Cell
stressincorticalorganoidsimpairsmolecularsubtypespeci

cation.
Nature
(2020)578
(7793):142
Œ
8.doi:
10.1038/s41586-020-1962-0
74.SansomSN,LiveseyFJ.Gradientsinthe brain:thecontrolofthedevelopmentof
form andfunctioninthecerebralcortex.
ColdSpringHarbPerspectBiol
(2009)1(2):1
Œ
17.doi:
10.1101/cshperspect.a002519
75.HofmanMA.Evolutionofthehuman brain:whenbiggerisbetter.
Front
Neuroanat
(2014)8(15):1
Œ
12.doi:
10.3389/fnana.2014.00015
76.CakirB,XiangY,TanakaY,KuralMH,ParentM,KangY-J, etal.Engineering
of humanbrainorganoidswithafunctionalvascular-like system.
NatMethods
(2019)
16:1169
Œ
75.doi:
10.1038/s41592-019-0586-5
77.MatsuiTK,TsuruY,HasegawaK, KuwakoKI.Vascularizationofhuman brain
organoids.
StemCells
(2021)39(8):1017
Œ
24.doi:
10.1002/stem.3368
78.ZhangS,Wan Z,KammRD.Vascularizedorganoidson achip: strategiesfor
engineeringorganoidswithfunctionalvasculature.
LabChip
(2021)1(3):473
Œ
88.doi:
10.1039/D0LC01186J
79.RothA,MPS-WSBerlin2019.Human microphysiological systems fordrug
development.
Science
(2021)375(6561):1304
Œ
6.doi:
10.1126/science.abc3734
80.M arxU,Akabane T,AnderssonTB,BakerE ,BeilmannM ,BekenS,etal.
Biology-inspiredmicrophysiologicalsy
stemstoadvancemedicinesforpatient
bene

tandanimalwelfare.
ALTEX
(2020)37(3):364
Œ
94.doi:
10. 14573/
altex.2 00 1 24 1
81.JamalM,ZarafsharAM,GraciasDH.Differentiallyphoto-crosslinkedpolymers
enableself-assemblingmicro

uidics.
NatCommun
(2011)2(1):527.doi:
10.1038/
ncomms1531
82.Miller JS,StevensKR,YangMT,BakerBM,NguyenDHT,CohenDM,et al.
Rapidcastingofpatter nedvascula rnetworksforperfus ableengineer edth ree-

dimensionaltissues.
NatMater
(2012)11(9):768
Œ
74.doi:
10.1038/nmat3357
83.GrigoryanB,PaulsenSJ,CorbettDC,SazerDW,FortinCL,ZaitaAJ,etal.
Multivascular networksandfunctionalintravasculartopologieswithinbiocompatible

hydrogels.
Science
(2019)364(6439):458
Œ
64.doi:
10.1126/science.aav9750
84.SabatiniBL,TianL.Imagingneurotransmitterandneuromodulatordynamics
invivo
withgeneticallyencoded indicators.
Neuron
(2020)108(1):17
Œ
32.doi:
10.1016/
j.neuron.2020.09.036
85.LiuC,GoelP,KaeserPS.Spatialandtemporal scalesofdopaminetransmission.
NatRevNeurosci
(2021)22(6):345
Œ
58.doi:
10.1038/s41583-021-00455-7
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
19

86.MeiJ,MullerE,RamaswamyS. Informingdeepneuralnetworksbymultiscale
principlesofneuromodulatorysystems.
TrendsNeurosci
(2022)45(3):237
Œ
50.doi:
10.1016/j.tins.2021.12.008
87.DertingerSKW,ChiuDT,JeonNL,WhitesidesGM.Generationofgradients
havingcomplex shapesusingmicro

uidicnetworks.
AnalChem
(2001)73(6):1240
Œ
6.
doi:
10.1021/ac001132d
88.BergerE,MagliaroC,PacziaN,MonzelA,AntonyP,LinsterC,etal.Milli

uidic
cultureimproveshumanmidbrainorganoidvitalityanddifferentiation.
LabChip
(2018)18:3172
Œ
83.doi:
10.1039/C8LC00206A
89.RomanoG.Neuronalreceptor agonistsandantagonists.
LabomeMaterMethods
(2019)9.doi:
10.13070/mm.en.9.2851
90.DeMarseTB,WagenaarDA,BlauAW,PotterSM.Theneurallycontrolled
animat:biologicalbrainsactingwithsimulatedbodies.
AutonRobots
(2001)11:305
Œ
10.
doi:
10.1023/A:1012407611130
91.ChenR, CanalesA, AnikeevaP.Neuralrecording andmodulationtechnologies.
NatRevMater
(2017)2:2.doi:
10.1038/natrevmats.2016.93
92.CoolsJ,JinQ ,YoonE,AlbaBurbanoD,LuoZ,CuypersD,et al.A
micropatternedmultielectrodeshellfor3Dspatiotemporalrecordingfromlivecells.

AdvSci(Weinh)
(2018)5:17007.doi:
10.1002/advs.201700731
93.HuangQ,TangB,RomeroJC,Yang Y,ElsayedSK,PahapaleG,etal.Shell
microelectrodearrays (MEAs)forbrain organoids.
SciAdv
(2022)8(33). doi:
10.1126/
sciadv.abq5031
94.ParkY,ChungTS,RogersJA. Threedimensionalbioelectronic interfacesto
small-scalebiologicalsystems.
CurrOpinBiotechnol
(2021)72:1
Œ
7.doi:
10.1016/
j.copbio.2021.07.023
95.ParkY,FranzCK,Ryu H,LuanH,CottonKY, KimJU, etal.Three-dimensional,
multifunctionalneuralinterfacesforcorticalspheroidsand engineered assembloids.
Sci
Adv
(2021)17:7.doi:
10.1126/sciadv.abf9153
96.KalmykovA,HuangC,BlileyJ,ShiwarskiD,TashmanJ,AbdullahA,etal.
Organon-e-chip: three-dime nsionalself
-rolledbiosensorarrayforelectrical
interrogationsofhumanelectrogenicspheroids.
SciAdv
(2019)23:5.
97.SongE, LiJ,WonSM,BaiW, RogersJA.Materialsfor

exiblebioelectronic
systemsaschronicneuralinterfaces.
NatMater
(2020)19(6):590
Œ
603.doi:
10.1038/
s41563-020-0679-7
98.ShiQ,LiuH,TangD,LiY, LiX,Xu F.Bioactuators basedonstimulus-
responsivehydrogelsandtheiremergingbiomedicalapplications.
NPGAsiaMater
(2019)11(1):64.doi:
10.1038/s41427-019-0165-3
9 9 .E frosAL,Delehanty JB,Huston AL, M edintzIL, BarbicM , HarrisTD.
Evaluatingthepotentialofusingquantumdotsformonitoringelectricalsignalsin
neurons.
NatNanotechnol
(2018)13(4):278
Œ
88.doi:
10.1038/s41565-018-0107-1
100.Jun JJ,SteinmetzNA,SiegleJH,DenmanDJ,BauzaM,BarbaritsB,etal.Fully
integratedsiliconprobesforhigh-densityrecordingofneuralactivity.
Nature
(2017)
551(7679):232
Œ
6.doi:
10.1038/nature24636
101.SteinmetzNA,AydinC,LebedevaA,OkunM,PachitariuM,BauzaM,etal.
Neuropixels 2 .0:aminiaturizedhigh-densityprobefo rstable,long-t ermbrain

recordings.
Science
(2021)372(6539).doi:
10.1126/science.abf4588
102. P
uppoF,Sadegh S,TrujilloCA,ThunemannM,CampbellEP,
VandenbergheM,etal.All-opticalelect
rophysiologyinhiPSC-derivedneurons
withsyntheticvoltagesensors.
FrontCell Ne urosci
(2021)15:671549. doi:
10.3389/
fncel.2021.671549
103.SunS, Zhang G,ChengZ,GanW,CuiM.Large-Scalefemtosecondholography
fornearsimultaneouso ptoge neticneuralmodulation.
OptExpress
(2019)27
(22):32228
Œ
34.doi:
10.1364/OE.27.032228
104.OvsepianSV.Thedarkmatterofthebrain.
BrainStructFunct
(2019)224
(3):973
Œ
83.doi:
10.1007/s00429-019-01835-7
105.RoyalVictorianEyeandEarHospital.
Firstimplantationofprototypebioniceye
with24electrodes:
ﬁ
AllofasuddenIcouldseealittle

ashoflight
ﬂ
.ScienceDaily (2012).
Availableat:
www.sciencedaily.com/releases/2012/08/120831065003.htm
.
106.PatrickJF,ClarkJM.Thenucleus22-channelcochlearimplantsystem.
Ear
Hear
(1991)12:3S
Œ
9S. doi:
10.1097/00003446-199108001-00002
107.AdvancedBionics.
AdvancedbionicsHiRes
Ž
bionicearsystem
.Availableat:
https://www.advancedbionics.com/us/en/po
rtals/professional-portal/products/ci-
internal-components.html
.
108.OsbornLE,ChristieBP,McMullenDP,NicklRW,ThompsonMC,PawarAS,
etal.Intracorticalmicrostimulation
ofsomatosensorycortexenablesobject
identi

catio nthrough perceivedsensations.In:
202143 rdAnnualInt ernat ional
ConferenceoftheIEEEEngineeringinMedicine&Biology Society (EMBC)
.IEEE
(2021)6259
Œ
62.A vailableat:(
https://jhu.pure.elsevier
.com/en/publications/
intracortical-microstimulation-of-somatosensory-cortex-enables-ob
).
109.McMullenDP,ThomasTM,FiferMS,CandreaDN,TenoreFV,NicklRW,
etal.Novelintraoperativeonlinefu
nctionalmappingofsomatosensory

nger
representationsfortargetedstimulatin
gelectrodeplacement:technicalnote.
J
Neurosurg
(2021),1
Œ
8.doi:
10.3171/2020.9.JNS202675
110.KingmaDP,WellingM.Auto-encodingvariationalbayes.
arXiv:1312.6114
(2014).doi:
10.48550/arXiv.1312.6114
111.KramerMA.Nonlinearprincipal component analysisusingautoassociative
neuralnetworks.
AIChEJ
(1991)37(2):233
Œ
43.doi:
10.1002/aic.690370209
112.DiCZ,CrainiceanuCM,CaffoBS,PunjabiNM.Multilevelfunctionalprincipal
componentanalysis.
AnnApplStat
(2009)3:3.doi:
10.1214/08-AOAS206SUPP
113.JewellS,Witten D.Exactspike traininference
via

0
optimization.
AnnAppl
Stat
(2018)12(4):2457
Œ
82.doi:
10.1214/18-AOAS1162
114.GaoC,HanF,ZhangCH.Onestimationofisotonicpiecewiseconstantsignals.
AnnStat
(2020)48(2):629
Œ
54.doi:
10.1214/18-AOS1792
115.ShenY,HanQ,HanF.Onaphasetransitioningeneralordersplineregression.
IEEE TransInfTheory
(2022)68(6):4043
Œ
69.doi:
10.1109/TIT.2022.3150253
116.FanJ.Ontheoptimalratesofconvergencefor nonparametricdeconvolution
problems.
AnnStat
(1991)19(3):1257
Œ
72.doi:
10.1214/aos/1176348248
117.MiaoZ,KongW,VinayakRK, SunW,HanF.Fisher-Pitmanpermutationtests
basedonnonparametricpoissonmixtureswithapplicationto singlecellgenomics.
J
AmericanStatAssociation
(2022).doi:
10.1080/01621459.2022.2120401
118.Che

nOY, CrainiceanuC,OgburnEL,CaffoBS,Wager TD,LindquistMA.
High-dimensionalmultivariatemediationwithapplication toneuroimag ingdata.

Biostatistics
(2018)19(2):121
Œ
36.doi:
10.1093/biostatistics/kxx027
119.ZhaoY,Lindquist MA,CaffoBS.Sparseprincipalcomponent basedhigh-
dimensionalmediationanalysis.
ComputStatDataAnal
(2020)142(10683):5.doi:
10.1016/j.csda.2019.106835
120.CaffoB,ChenS,StewartW,BollaK, YousemD,Davatzikos C,etal.Arebrain
vol umesbasedon magneticresonanceimagingmediatorsoftheassociationsof
cumulativeleaddosewithcognitivefunction?
AmJEpidemiol
(2008) 167(4):429
Œ
37.
doi:
10.1093/aje/kwm326
121.PearlJ.The limitationsofopaquelearningmachines.In:BrockmanJ,editor.
Possibleminds:Twenty-

vewaysoflookingatAI
,Penguinpress(2019)13
Œ
9.
122.PearlJ,MackenzieD.AICan
™
treasonwhy.
WallStreetJ
(2018).Available at:
https://www.wsj.com/articles/ai-cant-reason-why-1526657442
.
123.BresslerSL, SethAK. Wi ener-Grangercausality: awellestablished
methodology.
NeuroImage
(2011)58(2):323
Œ
9.doi:
10.1016/j.neuroimage.2010.02.059
124.Availableat:
http://www.scholarpedia.org/article/Brain\_connectivity
.
125.FristonKJ,HarrisonL,PennyW.Dynamiccausalmodelling.
NeuroImage
(2003)19(4):1273
Œ
302. doi:
10.1016/S1053-8119(03)00202-7
126.VogelsteinJT,ParkY,OhyamaT,KerrRA,TrumanJW,PriebeCE,etal.
Discoveryofbrainwideneural-behavioralmaps
via
multiscaleunsupervisedstructure
learning.
Science
(2014)344(6182):386
Œ
92.doi:
10.1126/science.1250298
127.PirP,leNovèreN.Mathematicalmodels ofpluripotentstemcells:atthedawn
ofpr edict iveregenerativemedicin e.
MethodsMolBiol
(201 6)1386:331
Œ
50. doi:
10.1007/978-1-4939-3283-2\_15
128.Shar peJ. Computermodelin gindevelopmentalbiology:growing to day,
essentialtomorrow.
Development
(2017)144(23):4214
Œ
25.doi:
10.1242/dev.151274
129.ZhengH,FengY,TangJ,MaS. Interfacingbrainorganoidswithprecision
medicineandmachinelearning.
CellRepPhysSci
(2022)3(7):100974.doi:
10.1016/
j.xcrp.2022.100974
130 .LibbyARG, BriersD,Haghig hiI,JoyDA, ConklinBR, BeltaC,et al.
Automated desig n of pluri potentstemcellself-organization.
CellSyst
(2019)9
(5):483
Œ
495.e10.doi:
10.1016/j.cels.2019.10.008
131.XavierdaSilveiradosSantosA, LiberaliP.Fromsingle cellstotissueself-
organization.
FEBSJ
(2019)286(8):1495
Œ
513.doi:
10.1111/febs.14694
132.Silva GA,MuotriAR,WhiteC.Understandingthehumanbrainusingbrain
organoids and astructure-functiontheory.
BioRxiv
(2020)19.doi:
10.1101/
2020.07.28.225631
133.Dresp-LangleyB.Seven propertiesofself-organizationinthehumanbrain.
Big
DataCognitComput
(2020)4(2):10. doi:
10.3390/bdcc4020010
134.GameCJA.Non-equilibriumthermodynamicsandthebrain.In:PribramKH,
editor.
Origins: Brainandself-organization
.PublisherTBC:Routledge,NewYork
(1994 ). p. 196.Availableat:
https://www.taylorfrancis.c om/books/mono/10 .4324 /
9781315789347/origins-karl-pribram
.
135.Grande-Garc
õ

a I.Theevolutionofbrainand mind:a non-equilibrium
thermodynamicsapproach.
LudusVitalis
(2007)XV(27):103
Œ
25.
136.Ande

nJ,MallatS.Deepscatteringspectrum.
IEEETransSignalProcess
(2014)
62:16:4114
Œ
28.doi:
10.1109/TSP.2014.2326991
137.Bauge

C,LagrangeM, Ande

n J, MallatS.Representingenvironmentalsounds
usingtheseparablescattering transform.In:
IEEE International conferenceonacoustics.
speechandsignalprocessing
(2013)8667
Œ
71.
138.SinapayenL,MasumoriA,IkegamiT.Learningbystimulationavoidance: a
principletocontrolspikingneuralnetworksdynamics.
PloSOne
(2017)12:2.doi:
10.1371/journal.pone.0170388
139.ZhuG,LiuY,WangY,BiX,BaudryM.Differentpatterns ofelectricalactivity
leadtolong-term potentiation byactivatingdifferentintracellular pathways.
JNeurosci
(2015)35(2):621
Œ
33.doi:
10.1523/JNEUROSCI2193-14.2015
140.DaurN,NadimF,B ucherD.Theco mplexity ofsmallcircuits: the
stomatogastricnervoussystem.
CurrOpinNeuroBiol
(2016)41:1
Œ
7.doi:
10.1016/
j.conb.2016.07.005
141.SchottdorfM.The reconstitutionofvisual corticalfeatureselectivity
invitro
.
Georg-August-UniversitaetGoettingen
(2017).Availableat:
https://ediss.uni-
goettingen.de/handle/11858/00-1735-0000-002E-E348-B?locale-attribute=en
.
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
20

142.SethAK,BayneT.Theoriesofconsciousness.
NatRevNeurosci
(2022)23
(7):439
Œ
52.doi:
10.1038/s41583-022-00587-4
143.InselTR,LandisSC,CollinsFS.TheNIHBRAINinitiative.
Science
(2013)340
(6133):687
Œ
8.doi:
10.1126/science.1239276
144.YatsenkoD,NguyenT,ShenS,GunalanK,TurnerCA,GuzmanR.DataJoint
elements:datawork

owsforneur ophysiology.
bioRxiv
(202 1)1 1. doi:
10.1101/
2021.03.30.437358
145.CarlsonD,CarinL.Continuingprogressofspikesortingintheeraofbigdata.
CurrOpinNeuroBiol
(2019)55:90
Œ
6.doi:
10.1016/j.conb.2019.02.007
146.UnakafovaVA,GailA.Comparingopen-sourcetoolboxesforprocessingand
analysisofspike andlocal

eldpotentialsdata.
FrontNeuroinform
(2019)13:57.doi:
10.3389/fninf.2019.00057
147.MarkiewiczCJ,GorgolewskiKJ,Feingold F,BlairR,HalchenkoYO,MillerE,
etal.TheOpenNeuroresourceforsharingofneurosciencedata.
Elife
(2021)10:e71774.
doi:
10.7554/eLife.71774
148.DANDI.
The DANDIarchive
.Availableat:
https://dandiarchive.org/
.
149.Gorgolewski KJ,AuerT, Calhoun VD,CraddockRC,DasS,DuffEP,etal.The
brainimagingdatastruct ure,aformatfororganizinganddescribingoutputsof

neuroimagingexperiments.
SciData
(2016)3(160044):1
Œ
9.doi:
10.1038/sdata.2016.44
150.RübelO,TrittA, LyR,Dichter BK, GhoshS,NiuL,etal.The neurodata
without bordersecosystemforneurophysiologicaldatascience.
Elife
(2022)11:e78362.
doi:
10.7554/eLife.78362
151.GiovannucciA,FriedrichJ, GunnP,KalfonJ, Brown BL,KoaySA,etal.
CaImAnanopensourcetool forscalablecalciumimagingdataanalysis.
Elife
(2019) 8.
doi:
10.7554/eLife.38173
152.Brain ImageLibrary.
Aboutthe brainimagelibrary
.Availableat:
https://www.
brainimagelibrary.org/about.html
.
153.LichtmanJW,P

ster H,ShavitN.Thebigdatachallengesofconnectomics.
NatNeurosci
(2014)17(11):1448
Œ
54.doi:
10.1038/nn.3837
154.WangZ,Sair HI,CrainiceanuC,LindquistM,BennettA,LandmanBA,etal.
Onstatistical testsoffunctionalconnectome

ngerprinting.
CanJStat
(2021)49:63
Œ
88.
doi:
10.1002/cjs.11591
155.Johnson EC,WiltM,RodriguezLM,Norman-TenazasR,RiveraC,Drenkow
N,etal.Toward ascalableframeworkforreproducibleprocessingofvolumetric,
nanoscaleneuroimagingdatasets.
Gigascience
(2020) 9:12. doi:
10.1093/gigascience/
giaa147
156.HiderRJr,Kleissas D,GionT,XenesD,MatelskyJ,PryorD,etal.Thebrain
observato rystorageserviceanddatabase(BossDB):acloud-nativeappr oach for

petascaleneurosciencediscovery.
FrontNeuroinform
(2022) 16(828787).doi:
10.3389/fninf.2022.828787
157.ChungJ,BridgefordE,ArroyoJ,PedigoBD,Saad-EldinA,GopalakrishnanV,
etal.Statisticalconnectomics.
Annu RevStatAppl
(2021)8:463
Œ
92.doi:
10.1146/
annurev-statistics-042720-023234
158.MatelskyJK, ReillyEP,JohnsonEC,StisoJ,BassettDS,WesterBA,et al.
DotMotif:anopen-sourcetoolforconnectomesubgraphisomorphismsearchand

graphqueries.
SciRep
(2021)11(1):1
Œ
14.doi:
10.1038/s41598-021-91025-5
159.vanEssenDC, SmithSM,Barch DM,BehrensTEJ,YacoubE,UgurbilK.The
WU-minnhumanconnectomeproject:anoverview.
NeuroImage
(2013)80:62
Œ
79.doi:
10.1016/j.neuroimage.2013.05.041
160.GeorgeJB, AbrahamGM,RashidZ,Amrutur B, SikdarSK.Randomneuronal
ensemblescaninherentlydocontextdependentcoarseconjunctiveencodingofinput

stimuluswithoutanyspeci

c training.
SciRep
(2018)8:1403.doi:
10.1038/s41598-018-
19462-3
161.ClawsonWP,WrightNC,WesselR,Shew WL.Adaptationtowardsscale-free
dynamicsimprovescorticalstimulusdiscriminationatthecostofreduced detection.

PloSComputBiol
(2017)13(5):e1005574.doi:
10.1371/journal.pcbi.1005574
162.BeggsJM,Plenz D.Neuronalavalanchesin neocorticalcircuits.
J Neurosci
(2003)3(23):11167
Œ
77.doi:
10.1523/JNEUROSCI23-35-11167.2003
163.EdelmanGM.NeuralDarwinism:selectionandreentrantsignalinginhigher
brainfunction.
Neuron
(1993)10:115
Œ
25.doi:
10.1016/0896-6273(93)90304-A
164.HebbDO.
Organization ofbehavior
.NewYork:Wileyonlinelibrary (1949).
165.KangassaloL, Spape

M,RavajaN,RuotsaloT. Informationgainmodulates
brainactivityevokedbyreading.
SciRep
(2020) 10:7671.doi:
10.1038/s41598-020-
63828-5
166.EbitzRB, HaydenBY.Thepopulation doctrineincognitive neuroscience.
Neuron
(2021)109:3055
Œ
68.doi:
10.1016/j.neuron.2021.07.011
167.EbitzRB,TuJC,HaydenBY.Ruleswarpfeatureencoding in decision-making
circuits.
PloSBiol
(2020)18:11.doi:
10.1371/journal.pbio.3000951
168.SchwartenbeckP,FitzGeraldT,MathysC,DolanR,Kronbichler M,FristonK.
Evidenceforsurpriseminimizationovervalue maximization inchoicebehavior.
Sci
Rep
(2015)5:16575.doi:
10.1038/srep16575
169.KnillDC,PougetA.TheBayesianbrain:therole ofuncertaintyinneural
codingandcomputation.
TrendsNeurosci
(2004)27(12):712
Œ
9.doi:
10.1016/
j.tins.2004.10.007
170.BarlowHB. Possibleprinciplesunderlyingthetransformationsofsensorymessages.
SensoryCommunication
(1961)1.doi:
10.7551/mitpress/9780262518420.003.0013
171.Friston KJ,TononiG,Reeke GN,SpornsO,EdelmanGM.Value-dependent
selectioninthebrain:simulationinasyntheticneural model.
Neuroscience
(1994)
59:229
Œ
43.doi:
10.1016/0306-4522(94)90592-4
172.M adhavM S ,CowanNJ.Thesynergybetweenneuroscienceand control
theory:thenervoussystemasinspira
tionf orhardcon trolchallenges.
AnnuRev
Cont rolRob otAutonSyst
(2020)3(1):243
Œ
67 .doi:
10.1146/annurev-control-060117-
10 4856
173.FristonKT.Thefree-energyprinciple:a uni

edbraintheory?
Nat RevNeurosci
(2010)11:127
Œ
38.doi:
10.1038/nrn2787
174.Kagan BJ,DucD,StevensI,GilbertF. Neuronsembodiedinavirtualworld:
evidencefororganoidethics?
AJOBNeurosci
(202 2)13 (2):114
Œ
7.doi:
10 .10 80 /
21507740.2022.2048731
175.KhetarpalK,RiemerM,RishI, PrecupD.Towardscontinualreinforcement
learning: areview andperspectives.
arXiv:2012.1349)v2
(2020)78.doi:
10.48550/
arXiv.2012.13490
176.ParisiGI,KemkerR,PartJL,KananC,WermterS.Continuallifelonglearning
withneuralnet works:a review.
NeuralNetw
(2019)13:54
Œ
71.doi:
10. 1016/
j.neunet.2019.01.012
177.LebedevMA,NicolelisMAL.Brainmachineinterface:frombasicscience to
neuroprothesesandneurorehabilitation.
PhysiolRev
(2017)97:767
Œ
837.doi:
10.1152/
physrev.00027.2016
178.BozhkovL.Deeplearningmodelsforbrainmachineinterfaces.
AnnMathArtif
Intell
(2019)90:1175
Œ
90.doi:
10.1007/s10472-019-09668-0
179.WahlinKJ,MaruottiJA,SripathiSR,BallJ,AngueyraJM,KimC,etal.
Photoreceptoroutersegment-likestructuresinlong-term3Dretinasfromhuman
pluripotentstemcells.
SciRep
(2017)7:1.doi:
10.1038/s41598-017-00774-9
180.KallmanA,CapowskiEE,WangJ,KaushikAM,JansenAD,Edwards KL,etal.
Investigatingconephotoreceptor developmentusingpatient-derivedNRLnullretinal

organoids.
CommunBiol
(2020)3(1):82. doi:
10.1038/s42003-020-0808-5
181.RostBR,Schneider-WarmeF,SchmitzD, HegemannP.Optogenetictoolsfor
subcellularapplicationsin neuroscience.
Neuron
(2017)96(3):572
Œ
603.doi:
10.1016/
j.neuron.2017.09.047
182.Garita-HernandezM, GuibbalL,ToualbiL,Routet F,Chaf

olA,WincklerC,
etal.Optogeneticlightsensorsin human retinalorganoids.
Front Neurosci
(2018)
12:789.doi:
10.3389/fnins.2018.00789
183.McGregorJE,GodatT,DhakalKR,ParkinsK,Strazzeri JM,BatemanBA, etal.
Optogeneticrestorationofretinalganglion cellactivityinthe living primate.
Nat
Commun
(2020)11(1):1703.doi:
10.1038/s41467-020-15317-6
184.CowanCS,RennerM,deGennaro M,Gross-ScherfB,GoldblumD,HouY,
etal.Celltypesofthehumanretinaanditsorganoidsatsingle-cellresolution.
Cell
(2020)182(6):1623
Œ
40.doi:
10.1016/j.cell.2020.08.013
185.GordonA,YoonSJ,TranSS,MakinsonCD, Park JY,AndersenJ,etal.Long-
termmaturationofhumancorticalorganoidsmatcheskeyearlypostnataltransitions.

NatNeurosci
(2021)24(3):331
Œ
42.doi:
10.1038/s41593-021-00802-y
186.GuzowskiJF,McNaughtonBL,BarnesCA,Worley PF.Environment-speci

c
expressionoftheimmediate-earlygenearcinhippocampalneuronalensembles.
Nat
Neurosci
(1999)2:1120
Œ
4.doi:
10.1038/16046
187.XiaoMF, RohSE,ZhouJ,ChienCC,LuceyBP,CraigMT,etal.Abiomarker-
authenticatedmodelofschizophreniaimplicatingNPTX2lossoffunction.
SciAdv
(2021)7(48).doi:
10.1126/sciadv.abf6935
188.WorldHealthOrganization.
Dementia
(2021).Availableat:
https://www.who.
int/news-room/fact-sheets/detail/dementia
.
189.NicholsE,SteinmetzJD,VollsetSE, Fukutaki K,ChalekJ,Abd-AllahF,etal.
Estimationoftheglobalprevalenceofdementiain2019and forecastedprevalencein

2050:ananalysisforthe globalburdenofdiseasestudy2019.
LancetPublicHealth
(2022)7(2):e105
Œ
25.doi:
10.1016/S2468-2667(21)00249-8
190.CentersforDiseaseControlandPrevention.
Leadingcausesofdeath
(2021).
Available at:
https://www.cdc.gov/nchs/fastats/leadingcauses-of-death.htm
.
191.XuJ,ZhangY,QiuC,ChengF.Globalandregionaleconomiccostsof
dementia:asystematicreview.
Lancet
(2017)390. doi:
10.1016/S0140-6736(17)33185-9
192.WorldHealthOrganization.
Globalstatusreportonthepublichealthresponse
todementia
.WHO Geneva:WorldHealthOrganization(2021).
193.PistollatoF,OhayonEL,LamA,LangleyGR,NovakTJ,PamiesD, etal.
Alzheimer Diseas eresear chinthe21 stcen tury: past andcur rentfailur es,new

perspectivesandfundingpriorities.
Oncotarget
(2016)7(26):38999
Œ
9016.doi:
10.18632/oncotarget.9175
194.DrummondE, WisniewskiT.Alzheimer
™
sdisease:experimentalmodelsand
reality.
Acta Neuropathol
(2017)133(2):155
Œ
75.doi:
10.1007/s00401-016-1662-x
195.MaennerMJ,ShawKA,BakianAV,BilderDA,DurkinMS,EslerA, etal.
Prevalenceandcharacteristicsofautismspectrumdisorderamongchildrenaged8

years
Œ
autism anddevelopmentaldisabilitiesmonitoringnetwork,11 sites,
unitedstates,2018.
MMWRSurveillSumm
(2021)70(11):1
Œ
16.doi:
10.15585/
mmwr.ss7011a1
196.ZhongX,HarrisG,SmirnovaL,Zufferey V,deCassiadaSilveiraE Sa

R,
BaldinoRussoF,etal.Antidepressantparoxetineexertsdevelopmentalneurotoxicityin

aniPSC-derived3Dhumanbrainmodel.
FrontCellNeurosci
(2020)14(25).doi:
10.3389/fncel.2020.00025
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
21

197.PamiesD,BlockK,LauP,GribaldoL,PardoCA,BarrerasP,etal.Rotenone
exertsdevelopmentalneurotoxicityina humanbrainspheroidmodel.
ToxicolAppl
Pharmacol
(2018)354:101
Œ
14.doi:
10.1016/j.taap.2018.02.003
198.ModafferiS,ZhongX,KleensangA, MurataY,FagianiF,PamiesD,etal.
Gene
Œ
environmentinteractionsindevelopmentalneurotoxicity:acasestudyof
synergybetweenchlorpyrifosandCHD8knockoutinhuman brainspheres.
Environ.
HealthPerspect
(2021)129(7):077001.doi:
10.1289/EHP8580
199.Fo

thi A

,SooryaL,Lo

rinczA.Theautismpalette:combinationsofimpairments
explaintheheterogeneityinASD.
FrontPsychiatry
(2020)11:503462.doi:
10.3389/
fpsyt.2020.503462
200.KehrerC,GroeschelS,Kustermann-KuhnB,BürgerF,Köhler W,Kohlschütter
A,etal.Languageand cognitioninchildrenwithmetachromaticleukodystrophy:onset

andnaturalcourseinanationwide cohort.
OrphanetJRareDis
(2014)9(1):18.doi:
10.1186/1750-1172-9-18
201.CharlsonFJ,FerrariAJ,SantomauroDF,DiminicS,S tockingsE ,S cottJG,
et al. Globalepidemiologyandburdenofschizophrenia:

ndings fromtheglobal
burdenofdiseasestudy2016.
Schizophr Bull
(2018)44(6):1195
Œ
20 3 .doi:
10.1093/
schbul/sby058
202.We inberge rDR.Implications ofnormalbrainde velopmentforthe
pathogenesisofschizophrenia.
ArchGenPsychiatry
(1987)44(7):660. doi:
10.1001/
archpsyc.1987.01800190080012
203.UrsiniG,PunziG,ChenQ,MarencoS,RobinsonJF,PorcelliA,etal.
Convergenceofplacentabiologyandgeneticriskforschizophrenia.
NatMed
(2018)
24(6):792
Œ
801.doi:
10.1038/s41591-018-0021-y
204.BowieCR,HarveyPD.Cognitivede

citsandfunctionaloutcomein
schizophrenia.
NeuropsychiatrDisTreat
(2006)2(4):531
Œ
6.doi:
10.2147/
nedt.2006.2.4.531
205.EackSM,BahorikAL,McKnightSAF,HogartySS,GreenwaldDP,NewhillCE,
etal. Commonalitiesinsocialandnon-socialcognitiveimpairmentsinadultswith

autism spectrumdisorderandschizophrenia.
SchizophrRes
(2013)148(1
Œ
3):24
Œ
8.doi:
10.1016/j.schres.2013.05.013
206.SimonsFoundationAutismResearchInitiative.
SFARIbase
.Available at:
https://www.sfari.org/resource/sfari-base/
.
207.BeilmannM,BoonenH,CzichA,Dear G,HewittP,MowT,etal.Optimizing
drugdiscoverybyinvestigativetoxicology:currentandfuturetrends.
ALTEX
(2019)36
(2):289
Œ
313.doi:
10.14573/altex.1808181
208.MiuraY,Pas


caSP.Polarizingbrainorganoids.
NatBiotechnol
(2019)37
(4):377
Œ
8.doi:
10.1038/s41587-019-0084-4
209.SloanSA,AndersenJ, Pas

caAM,Birey F,Pas


caSP.Generationandassembly
ofhuman brainregion
Œ
speci

cthree-dimensionalcultures.
NatProtoc
(2018) 13
(9):2062
Œ
85.doi:
10.1038/s41596-018-0032-7
210.LancasterMA,KnoblichJA.Generationofcerebralorganoidsfromhuman
pluripotentstemcells.
NatProtoc
(2014)9(10):2329
Œ
40.doi:
10.1038/nprot.2014.158
211.RennerM,LancasterMA,Bian S,ChoiH,KuT,PeerA,etal.Self-organized
developmentalpatterning anddifferentiation in cerebral organoids.
EMBOJ
(2017)36
(10):1316
Œ
29.doi:
10.15252/embj.201694700
212.KimH,XuR,PadmashriR,DunaevskyA,LiuY,DreyfusCF,etal.
Pluripotentstemcell-derive dcerebralorg
anoidsrevealhumanoligodendrogenesis
withdorsalandventralorigins.
StemCell Rep
(2019)14(12):5.doi:
10.1016/
j.stem cr.2019.04.011
213.CederquistGY,AsciollaJJ,TchieuJ,Walsh RM,CornacchiaD,ReshMD,etal.
Speci

cationofpositionalidentityinforebrainorganoids.
NatBiotechnol
(2019)37
(4):436
Œ
44.doi:
10.1038/s41587-019-0085-3
214.ArchieJG, CollinsJS,LebelRR.Quantitativestandardsforfetaland neonatal
autopsy.
AmJClinPathol
(2006) 126(2):256
Œ
65.doi:
10.1309/FK9D5WBA1UEPT5BB
215.HollandD,Chang L, Ernst TM,CurranM,BuchthalS,Alicata D,etal.
Structuralgrowthtrajectoriesandratesofchangeinthe

rst 3monthsof infantbrain
development.
JAMANeurol
(2014)71(10):1266
Œ
74.doi:
10.1001/jam aneurol.
2014.1638
216.S amuelsenGB,LarsenKB,BogdanovicN,LaursenH,GraemN,LarsenJF,
eta l.Thechangingnumberofcellsinthehuma nfetal forebrainandits

subdivisions:astereological a nalysis.
CerebCortex
(2003)13:115
Œ
22.doi:
10.1093/cercor/13.2.115
217.Jakovcevski I,FilipovicR,Mo Z,Ra
kicS,ZecevicN.Oligodendrocyte
developmentandtheonset ofmyelination inthehuman fetalbrain.
Front
Neuroanat
(2009)3:5.doi:
10.3389/neuro.05.005.2009
218.MelloniL,Mudrik L,PittsM,KochC.Makingthehardproblem of
consciousness easier.
Science
(2021)28(372):911
Œ
2.doi:
10.1126/science.abj3259
219.JeziorskiJ,BrandtR,EvansJH,CampanaW,Kalichman M,ThompsonE,etal.
Brainorganoids,consciousness,ethicsandmoralstatus.
SeminCellDevBiol
(2022)
S1084
Œ
9521(22).doi:
10.1016/j.semcdb.2022.03.020
220.AmericanPsychologicalAssociation.
APAdictionaryofpsychology website
(2023).Availableat:
https://dictionary.apa.org/
.
221.FristonK.Functional integrationandinferenceinthebrain.
ProgNeurobiol
(2002)68(2):113
Œ
43.doi:
10.1016/S0301-0082(02)00076-X
222.SawaiT,HayashiY,NiikawaT,ShepherdJ,Thomas E,LeeTL,etal.Mapping
theethicalissuesofbrain organoidresearchandapplication.
AJOBNeurosci
(2022)13
(2):81
Œ
94.doi:
10.1080/21507740.2021.1896603
223.GreelyHT.Humanbrainsurrogatesresearch:theonrushingethicaldilemma.
AmJBioeth
(2021)21(1):34
Œ
45.doi:
10.1080/15265161.2020.1845853
224.KoplinJJ,Savulescu J.Morallimitsofbrainorganoidresearch.
JLawMed
Ethics
(2019)47(4):760
Œ
7.doi:
10.1177/1073110519897789
225.BeauchampTL,DeGraziaD.
Principlesofanimalresearchethics
.Oxford:
Oxford UniversityPress(2020).
226.MacCounRJ.Moraloutrageandoppositionto harmreduction.
CriminalLaw
Philosophy
(2013)7(1):83
Œ
98.doi:
10.1007/s11572-012-9154-0
227.SkitkaLS,MorganGS.Thesoci ala
ndpoliticalimp licationsofmoral
conviction.
AdvancedPoliticalPsychol
(2014)35(S1):95
Œ
110.doi:
10.1111/pops.12166
228.BoydJL,SugarmanJ.Towardresponsiblepublicengagementinneuroethics.
AJOBNeurosci
(2022)13(2):103
Œ
6.doi:
10.1080/21507740.2022.2048736
229.HaselagerDR,BoersSN,JongsmaKR,VinkersCH,BroekmanML,
BredenoordAL.Breeding brains?patients'andlaymen' sperspectiveson cerebral
organoids.
RegenerMed
(2020)15(12):2351
Œ
60.doi:
10.2217/rme-2020-0108
230.NiemeläJ.Whatputsthe'yuck'intheyuckfactor?
Bioethics
(2011)25(5):267
Œ
79.doi:
10.1111/j.1467-8519.2010.01802.x
231.McLennanS, FiskeA,CeliLA,M,llerR,HarderJ,etal.Anembeddedethics
approachforAIdevelopment.
NatMachIntell
(2020)2:488
Œ
90. doi:
10.1038/s42256-
020-0214-1
232.NationalAcademyofSciences.
Theemerging

eldofhumanneuralorganoids,
transplants,andchimeras
.Washington,D.C: NationalAcademiesPress(2021).
233.Or ganis ationforEconomicCo-operationandDevelopment.
OECD
recommendationonresponsbileinnovationinneurotechnology
(2019).Availableat:
https://www.oecd. org/scien
ce/recommendation-on-responsible-innovation-in-
neurotechnology.htm
.
234.NgaiJ.BRAIN2.0:Transformingneuroscience.
Cell
(2022)185(1):4
Œ
8.doi:
10.1016/j.cell.2021.11.037
23 5.NationalInstitutesofHealthBRAINInitiative.
Thebrainstormproject:A
collaborativeapproachtofacilitatingtheneuroethicsofbioengineeredbrainmodeling

research
(2018).Availableat:
https://braininitiative.nih.gov/funded-awards/brainstorm-
project-collaborative-approach-facilitating-neuroethics-bioengineered-brain
.
236.
Oxford EnglishDi ctionary
.OxfordUniversit yPress(2020).Availableat:
https://www.oed.com
.
237.CangelosiA,Bongard J,FischerMH,Nol

S.Embodiedintelligence.In:
KacprzykJ,PedryczW,editors.
Springerhand bookofcomputational intelligence
.
Berlin, Heidelberg:Springer(2015).697
Œ
714.
238.
DictionarybyMerriam-Webster
.Available at:
https://www.merriam-webster.
com
.
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
22

Glossary
Biologicalcomputation
calculation(notnecessarilyasmathematicaloperations)carriedoutbya biologicalsystem.
Biologicalcomputing
taskstypicallydonebycomputerscarriedoutbybiologicalsystems.
Brainorganoid
inducedpluripotentstemcell(iPSC)-derived3Dneuralcultures,recapitulating aspectsofbraincellularcomposition,architecture,and
functionality.
Cognition
the humanmentalactionorprocessofacquiring knowledge and understandingthrough thought,experience,and the senses (
236
).
Cognition-in-a-dish
a basicability toprocessaninput and provide a measurablyoutput;a learnedadequateresponsetothe stimuliwhichisenabledbythe
presenceofthenecessarymolecularmachineryandphysiologicalfeaturessuchaslearningcircuitsoflong-termmemory.
Consciousness
the humanstate ofbeingawareofand responsivetoone
™
ssurroundings(
236
);a hypotheticalorganoid
™
sstate ofbeingresponsivetoand
ﬁ
awareof
ﬂ
theenvironment.
Embodiedintelligence
the computationalapproachtothe designand understandingofintelligentbehaviorinembodiedand situated agentsthrough the
considerationofthe strictcouplingbetweentheagentand itsenvironment (situatedness),mediatedbytheconstraintsoftheagent
™
sown
body,perceptualand motorsystem,and brain(embodiment)(
237
).
Intelligence
the humanability toacquireand applyknowledge andskills(
238
).
Intelligence-in-a-dish
visionofOI-implementingcellmodelstoperformcomputer functions(
238
)andtotestsubstances(e.g. fortoxicologicalor
pharmacologicalpurposes).
Learningandmemory
inthe contextofOI,learningisidenti

edasanincreasedfrequencytoshowand memorizea responsepatterntoa stimulatorypattern.
Organoid intelligence(OI)
describesanemerging

eldaimingtoexpandthe de

nitionofbiocomputingtoward brain-directedOIcomputing,i.e.toleveragetheself-
assembledmachineryof3Dhumanbraincellcultures(brainorganoids)tomemorizeand computeinputs.
Sentience
inhumans,the simplestormostprimitiveformofcognition,consistingofa consciousawareness ofstimuliwithoutassociationor
interpretation(
220
);forOI,basic responsiveness tosensoryinput,e.g.light,heat,etc.
Smirnovaetal.
10.3389/fsci.2023.1017235
Frontiersin
Science
frontiersin.org
23
