Advances in 3D organoid culture
The past decade has seen a revolution in brain cell cultures,
moving from traditional monolayer cultures to more organ-like,
organized 3D cultures –i.e. brain organoids ( Figure 2A ). These can
be generated either from embryonic stem cells or from the lessethically problematic iPSC typically derived from skin samples ( 54).
The Johns Hopkins Center for Alternatives to Animal Testing,
among others, has produced such brain organoids with high levels
of standardization and scalability ( 32)(Figure 2B ). Having a
diameter below 500 mm, and comprising fewer than 100,000 cells,
each organoid is roughly one 3-millionth the size of the human
brain (theoretically equating to 800 MB of memory storage). Other
groups have reported brain organoids with average diameters of 3 –5
mm and prolonged culture times exceeding 1 year ( 34–36,55–59).
These organoids show various attri butes that should improve their
potential for biocomputing ( Figure 2 ). First, cell density in these 3D
models is similar to the in vivo cell density, and much higher than in
monolayer cultures; the ratio of cells to media volume is also much
higher compared to monolayers. Second, most of these brain organoids
show spontaneous electrophysiologica l activity and reactivity to electrical
stimulation (via evoked ﬁeld potentials) ( 32), con ﬁrming the presence of
active synapses. Trujilio et al. have shown patterning of cortex layers andoscillation waves comparable to electroencephalograms (EEGs) from
human preterm babies ’brains ( 34).
Third, axons in these organoids show extensive myelination.
Pamies et al. were the ﬁrst to develop a 3D human brain model
showing signi ﬁcant myelination of axons ( 32). About 40% of axons
in the brain organoids were myelinated ( 30,31), which approaches
the 50% found in the human brain ( 60,61). Myelination has since
been reproduced in other brain organoids ( 47,62). Myelin reduces
the capacitance of the axonal membrane and enables saltatory
conduction from one node of Ranvier to the next. As myelinationincreases electrical conductivity approximately 100-fold, this
promises to boost biological computing performance, though its
functional impact in this model remains to be demonstrated.
Finally, these organoid cultures can be enriched with various cell
types involved in biological learning, namely oligodendrocytes,
microglia, and astrocytes. Glia cells are integrally important for the
pruning of synapses in biological learning ( 63–65) but have not yet
been reported at physiologically relevant levels in brain organoid
models. Preliminary work in our organoid model has shown the
potential for astroglia cell expansion to physiologically relevant levels
(
47). Furthermore, recent evidenc e that oligodendrocytes and
astrocytes signi ﬁcantly contribute to learning plasticity and
FIGURE 1
Architecture of an OI system for biological computing. At the core of OI is the 3D brain cell culture (organoid) that performs the computation. The
learning potential of the organoid is optimized by culture conditions and enrichment by cells and genes critical for learning (including IEGs). The
scalability, viability, and durability of the organoid are supported by integrated micro ﬂuidic systems. Various types of input can be provided to the
organoid, including electrical and chemical signals, synthetic signals from machine sensors, and natural signals from connected sensory organoid s
(e.g. retinal). We anticipate high-resolution output measurement both by electrophysiological recordings obtained viaspecially designed 2D or 3D
(shell) MEA, and potentially from implantable probes, and imaging of organoid structural and functional properties. These outputs can be used
directly for computation purposes and as biofeedback to promote organoid learning. AI and machine learning are used throughout to encode anddecode signals and to develop hybrid biocomputing solutions, in conjunction with a suitable big-data management system.Smirnova et al. 10.3389/fsci.2023.1017235
Frontiers in Science frontiersin.org 05

memory suggests that these processes should be studied from a
neuron-to-glia perspective, ra ther than the neuron-to-neuron
paradigm generally used ( 63–65). In addition, optimizing the cell
culture conditions to allow the expression of immediate early genes
(IEGs) is expected to further boost the learning and memory
capacities of brain organoids since these are key to learning
processes and are expressed only in neurons involved in memory
formation –as detailed below.Scaling up these 3D organoids is a key early aim. We set out to
produce brain organoids with about 10 million neural cells ( 66).
Existing differentiation protocols for scaling up the cultures, and
starting 3D differentiation directly from iPSC (bypassing the
intermediate generation of neur oprogenitor cells), are very
promising ( 67,68). These developments bene ﬁtf r o mg e n e r a l
progress in microphysiological systems (MPS), which include
organoids, and aim to establish organ architecture and functionality
FIGURE 2
Advances in 3D cell culturing provide the foundation for systems to explore organoid intelligence. (A)3D neural cell cultures have important advantages
for biological learning, compared with conventional 2D monolayers –namely a far greater density of cells, enhanced synaptogenesis, high levels of
myelination, and enrichment by cell types essential to learning. (B)Brain organoid differentiation over time from 4 to 15 weeks, showing neurons
(microtubule associated protein 2 [MAP2]; pink), oligodendrocytes (oligodendrocyte transcription factor [OLIG2]; red), and astrocytes (glial ﬁbrillary acidic
protein [GFAP]; green). Nuclei are stained with Hoechst 33342 (blue). Images were taken with an LCM 880 confocal microscope with 20x and 63x
magni ﬁcation. Scale bars are 100 mma n d2 0 mm, respectively. The images show the presence of MAP2-positive neurons as early as 4 weeks, while glial
cells emerge at 8 weeks and there is a continuous increase in the number of astrocytes over time.Smirnova et al. 10.3389/fsci.2023.1017235
Frontiers in Science frontiersin.org 06

such as OI as proposed here. Notably, some coauthors are involved in
spearheading quality assurance guidance for Good Cell Culture
Practice, expanding earlier guidance to stem cell-based models,
MPS, organ-on-chip models ( 69), and establishing an annual MPS
World Summit series ( 70) and international society.
Micro ﬂuidic perfusion systems
While brain organoids may recapitulate spatiotemporal
molecular signatures, gene expression networks ( 71), certain
histoarchitectures (e.g. cortex patterning), and neuron phenotypes
within the human brain, they do not re ﬂect its regional organization
and the complexity of its neuronal circuitry to levels allowing for
higher-order brain function ( 35,72,73). Part of the human brain ’s
complexity stems from its size and the vasculature that supports its
growth ( 74,75). Although brain vasculature models are under
development ( 76,77), most brain organoid models so far are still
avascular and rely on passive diffusion to deliver nutrients; the
average scope of diffusion is approximately 300 mm before starving-
derived necrosis occurs at the core ( 78)(Figure 3A ). Thus, the lack
of a perfusable vasculature is a major limitation for improving
biological complexity and in vivo -like functionality ( 78).
Micro ﬂuidic systems that substitute for vasculature –allowing
controlled perfusion of oxygen, nutrients, and growth factors and
the removal of waste products –will be critical to the scalable
and durable culturing of brain organoids ( Figure 3B )(79,80). These
will support the homeostasis and viability of the organoids, allowing
a more physiologic-like differentiation toward a more complex,
sophisticated, and “in vivo -like ”model. Flexible, self-folding
micro ﬂuidics can already deliver chemicals with 3Dspatiotemporal control ( 81), and recent advances in 3D printing
with sacri ﬁcial materials offer the potential to create perfusable
scaffolds for organoids ( 82,83).
These micro ﬂuidic systems will also support chemical signaling
to organoids. The importance of spatiotemporal chemical
patterns to encode information is well established in neuroscience
and behavioral science ( 84–86). Signi ﬁcant advances in
micropatterning and micro ﬂuidics over the past two decades have
already allowed 2D chips to offer signi ﬁcant tunability of the
chemical microenvironment around neurons, and tree-like
micro ﬂuidic gradient generators have been widely used to create
chemical patterns ( 87). Importantly, 3D spatiotemporal
micro ﬂuidic interfaces ( 88) now enable localized dosing and
replication of chemical environ ments with neurotransmitters,
neuropeptides, and other neurochemicals. A comprehensive list of
the agonists and antagonists is available ( 89).
High-resolution recording of complex
neuronal networks
3D microelectrode arrays for brain organoids
Robust and reproducible systems to record electrophysiological
outputs from brain organoids are critical to developing OI systems
and will need to address various challenges in reading and writing to
complex neural assemblies. Brain-machine interface technologies
have been in progress for at least two decades ( 90) but remain
primitive. Microelectrode arrays (MEAs) form the heart of many
such interfaces since they can be used to both stimulate and record,
FIGURE 3
3D micro ﬂuidic devices to support scalability and long-term homeostasis of brain organoids. (A)Cells within brain organoids require perfusion with
oxygen, nutrients, and growth factors, as well as the removal of waste products, to provide conditions approximating physiologic homeostasis.Passive diffusion penetrates to a depth of only around 300 mm, and so necrosis occurs at the core of larger organoids owing to starvation. This
prevents brain organoids from being scaled up to the size and complexity required for OI research and limits their durability. (B)3D micro ﬂuidic
systems enable greater scalability and durability by providing controlled perfusion throughout larger organoids. They also enable 3D spatiotempo ral
dosing of chemicals for signaling purposes.Smirnova et al. 10.3389/fsci.2023.1017235
Frontiers in Science frontiersin.org 07

and offer unprecedented parallelism and individual addressability.
However, most are predominantly in a 2D chip-based format, being
designed for use with monolayer cell cultures ( 91). This represents a
likely problem as brain organoids are spherical 3D structures that
make limited contact with a 2D MEA chip. Furthermore, most 2D
electrode chip interfaces are rigid, and a mismatch in the stiffness of
the recording interface and cell system compromises performance
(92,93).
Therefore, we and others are developing novel 3D MEA
interfaces speci ﬁcally designed for organoids ( 93–96) and inspired
by the EEG caps used to record brain electrical patterns from the
scalp. Organoids are grown inside ﬂexible, ultra-soft-coated, self-
folding, and buckled shells, covered with patterned nanostructures
and probes ( 92,93,97–99)(Figure 4 ). This model allows
multichannel stimulation and recording spatiotemporally across
the entire surface of the organoid with unprecedented resolution
and high signal-to-noise ratio, resulting from the greatly enhanced
recording surface areas ( 92,93). After the spontaneous signal is
stabilized and synchronized, the response to repeated chemical
stimuli from neurotransmitter gradients [glutamate, g-
Aminobutyric acid (GABA), dopamine, serotonin, acetylcholine]
and main receptors agonists/antagonists [e.g. kainic acid, kynurenic
acid, g-Amino- b-hydroxybutyric acid (GABOB), bicuculline,
haloperidol, nicotine, methylbromide ( 89)] can be recorded to
address and modulate the synaptic plasticity.
These shell MEA interfaces can be integrated with the
aforementioned 3D micro ﬂuidic systems, supporting the scalability
and durability of the system and chemical signaling viaspatial
patterning and gradients. Together, they create a robust platform
to gain an iterative, in-depth understanding of organoid behavior
and responses to a range of highly modi ﬁable environmental and
input stimuli, which in turn will allow us to explore their capacity to
recapitulate the molecular mechanisms of learning and memory
formation and ultimately their computational potential.
High-resolution implantable
electrophysiology devices
We consider that the shell MEAs described above strike an
appropriate balance by providing comprehensive, high-resolution
electrophysiological recordings with minimal disruption to the
organoid. However, future systems might permit organoids to be
grown around implantable electrodes to further enhance signal
resolution and to access the inside of the organoid. The ef ﬁciency of
such systems must be balanced by their invasiveness since any
damage to neuronal networks could alter the behavior of
the organoid.
Neuropixels are silicon probes developed for extracellular
recording in animals (mostly mice and rats) ( 100). They lend
themselves to direct integration with brain organoids, though in
principle, Neuropixels can also be integrated into shells. These large
(10 mm), dense (100 sites/mm) implantable neural devices allow
the recording of hundreds of well-resolved single neuron signal
traces. They can be combined with light sources, electrical
stimulation, and photometry, dramatically increasing the input
and output opportunities and the mapping of activity in thelearning organoid. These devices also appear uniquely capable of
long-lived exposure to neural tissue. Chronic implants in rats and
mice frequently last for 150 days or more with little degradation in
recorded neural activity, indicating suitable compatibility and
stability ( 100,101). Recently, the Kosik laboratory (University of
California Santa Barbara, CA, USA) used such CMOS shank probes
in parallel with 2D high-density MEAs to record intrinsic network
activity in brain organoids ( 46).
Mounting and inserting such probes into the organoid is a
complex challenge, and work is ongoing to develop a new
generation of suitable (more ﬂexible) probes. If the organoid is
grown in well plates, mounting of the probe would be like skull
mounting in a rodent. If the growth medium needs to be exchanged
periodically for organoid health without disturbing the probe-
organoid interface, then an unconventional means for removing
and adding media to the wells would need to be developed. The
minimum size of the probe base (4.2 mm × 1 mm) allows suf ﬁcient
“headroom ”for this ﬂuidic machinery. Once a micro ﬂuidic growth
chamber is adopted, a membrane interface to the probe shank
would be needed. Neuropixels are routinely used with a Kwik-Sil
(WPI) silicon layer over the brain while recording and sealing
chronic implants. Further investigation may be required to perfect
this geometry, but interfacing with a low-pressure ﬂuidic chamber
does not present any fundamental problem. Finally, a Neuropixels
2.0 probe ( 101) has four shanks, each 10 mm long with a cross-
section of 70 mm×2 4 mm. For a 1 mm diameter organoid,
approximately 500 electrodes would contact the cells, giving the
capacity to record from 384 switch-selectable sites at a time. The
probe electrodes would displace ~1.5% of the current organoid
volume, likely an acceptable perturbation. Yields of 200 –600 “units ”
are typical in recordings from rodents, limited by activity. The
probe would be within detection distance of ~14% of the cells in a 1
mm diameter organoid.
Among the challenges facing brain-machine interface
technologies is the scale of connectivity. Cortical neurons each
have in the order of 104input synapses and connect to in the order
of 103cells, some across many millimeters –even in small brains
such as those of mice. It is not yet clear if organoids have similar or
reduced synaptic counts. Curre nt brain-machine interfaces
have many unresolved cells per input (reading) for each
electrode (all within 20 –80mm) and a largely unknown number
of cells for output (writing or stimulation). Except for special
cases in the visual cortex, the cellular understanding of writing
remains dif ﬁcult, while reading has enabled the control of
prosthetic robots.
How might traction be achieved to begin harnessing organoid
computing power? We propose that two paths be explored.
All-optical
An all-optical path for organoids would allow cell-by-cell
excitation and whole organoid reading (again cell-resolved).
While optical imaging is not likely a terminal technology for
harnessing OI, it allows exploration of the system behavior, and
the kinds of computation that could be initially ( 102) performed.
There are rapidly developing t echnologies for large-volume
imaging that make this attractive. Techniques such as BesselSmirnova et al. 10.3389/fsci.2023.1017235
Frontiers in Science frontiersin.org 08

holography can image volumes with hundreds of mmd i a m e t e ra t
kHz rates, with an accurate cellular resolution if the activity is
relatively sparse ( 102). Directly writing with opsins is also well
established, and holographic methods are again exploited ( 103),but the cell write rate is signi ﬁcantly lower than the cell read
rate. These methods are immediately available and would help
inform the design of electrophys iological systems necessary to
progress OI.
FIGURE 4
Interfacing organoids with 3D microelectrode arrays (MEAs) to allow electrophysiological output recording. (A)Organoid-MEA interfaces were
inspired by the electroencephalograph (EEG) used to take electrophysiological recordings from the human brain. (B)Organoids are grown inside
ﬂexible, ultrasoft-coated, self-folding, and buckled shells covered with patterned multielectrode nanostructures and probes. These interfaces a llow
ultra-high-resolution 3D spatiotemporal stimulation and recording of electrophysiological patterns across the entire organoid surface (see als o93).
(C)Bright ﬁeld image of brain organoid captured inside the shell. (D)Confocal image showing the side view (projected confocal stack) of a brain
organoid (green; Fluo-4 calcium dye) with a diameter around 500 mm encapsulated in the electrodes of the 3D shell (blue). (E, F) Three channels of
electrodes are distributed across the shell with representative raster plot showing the spontaneous electrical activity of the brain organoid. (G)
Overlaid spike waveform from channels 1, 2, and 3.Smirnova et al. 10.3389/fsci.2023.1017235
Frontiers in Science frontiersin.org 09

High-throughput electrophysiology
Electrophysiology recording capacity is impeded by the “dark
matter ”observation resulting from the fact that most neurons are
notﬁring most of the time. As such, an electrophysiology channel
sensitive to reading and writing individual local neurons can be
inefﬁcient: even the best-performing probes “see”<1% of the
neurons within their detection range ( 104). It seems unnecessary
to achieve a synapse level of interpretability of these systems if the
base principles are elucidated, empirically tested, and used to
control the system as a whole. Notably, bionic implants for
humans have managed to convey signi ﬁcant information with
relatively few input electrodes; e.g. the bionic eye ( 105) used 24
electrodes, and current cochlear implants use between 10 and 22
(106,107). Therefore, different resolutions may be required for
input vs. output.
Although organoid EEG and implantable neural devices are
feasible to investigate the scale of required input/output contacts,
both technologies need to be explored further to assess the
recording patterns and learning potential of brain organoids.
Memory and learning in organoids: training using
biofeedback, big data, and AI/machine learning
Understanding the capacity of brain organoids to learn is
fundamental to determining whether they can be used
computationally by harnessing the advantages of biological
l e a r n i n g .A tt h i ss t a g e ,l e a r n i n gi si d e n t i ﬁed as an increased
frequency to show and memorize a response pattern to a
stimulatory pattern. We aim to use the iterations of technologies
described above to interface organoids and computers to initiate
supervised learning simulations (i.e. trained stimulus response
patterns). To achieve this goal, the brain organoids should be
exposed to spatiotemporal patterns of electrical and chemical
stimulation, with the associated recordings delineating
relationships between inputs and outputs. A feedback loop is
required to train a learning system. Changes in the brain
organoid architecture and functionality (synaptic connections and
electrophysiology) due to such training cycles can then be analyzed.
These two factors affect synaptic plasticity –the main mechanism of
memory formation and learning. Hence, the recorded responses to
electrical or chemical stimuli should demonstrate whether and how
learning may occur in the organoids.
Ultimately, robust, high-resolution encoding and decoding of
signals going into and out of human cortical tissue is required.
Recent achievements using intracortical microstimulation (ICMS)
and decoding of motor and sensory cortices using MEA in human
subjects offer promise ( 108,109), though further advances in scale
and resolution will be necessary.
AI analysis of responses
Organoid-MEAs will generate massive recording datasets that
will themselves need to be analyzed by statistical and machine
learning techniques. Given the recording density and volume, this
will necessitate a novel big-data infrastructure and supercomputing
capacity tailored to the sophisticated needs of this form of modern
biological data.Fundamentally, the two major challenges for AI analysis in this
context are : (a) how to decode the input provided to an organoid
(e.g. the game Pong) ( 29) to relate to changes with its architecture
and/or functionality; and (b) how to relate these organoid changes
to certain outputs (e.g. the improvement in playing Pong). In other
words, biological computing includes OI as a mediating
mechanistic process between the inputs and outputs. To answer
these two challenges, we foresee the use of interdisciplinary tools
integrating machine learning, s tatistics, signal processing,
information theory, and optimization. We also believe that the
questions raised will motivate new methodological developments in
these ﬁelds.
Speci ﬁcally, we believe the following three paths must be
explored to relate OI inputs to outputs:
1. Machine learning and statistical algorithms are needed to
quantify organoid function changes. This involves: (a)
sensor integration to accelerate processing based on
unsupervised learning and dimension reduction, such as
principal component anal ysis (PCA), independent
component analysis (ICA), and autoencoders including
hierarchical versions ( 110 –112); (b) signal detection using
sequencing and time series (e.g. state-space) models ( 113 –
115), which are often used in brain imaging analysis; (c)
pattern recognition to identify the real signal pattern and
deconvolute it from the background noises ( 116).
2. Algorithms are also needed to quantify organoid architecture
changes. Challenges include pinpointing the exact parts of
the organoid that respond to the input [e.g. using mixture
models ( 117)] and then quantifying these changes by
monitoring their physical appearances. The application of
multiscale unsupervised structure learning methods to the
recorded responses can identi fy discrete, statistically
distinguishable, observer-unbiased response phenotypes.
3. Models must then be trained to relate the quanti ﬁed
organoid changes to the output variables viamultivariate
causal models ( 118 –120). OI will require novel
developments integrating AI/machine learning and both
space- and time-dependent causal modeling ( 121 –123).
Clearly, inferring or estimating the connectivity of organoids
will be a core endeavor. Connectivity, in neuronal circuits, is usually
divided into structural, functional, and effective connectivity ( 124).
The distinction between functional and effective connectivity is
particularly prescient here: functional connectivity refers to the
statistical correlations between neuronal ﬂuctuations in different
populations, while effective connectivity refers to the causal and
directed connectivity between populations. The corresponding data
analysis techniques can be parsed into frontal connectivity methods
such as coherence analyses and Granger causality. These can be
contrasted with inferences about directed (effective) connectivity,
usually using some form of dynamic causal modeling ( 125).
Applying these statistical and computational methods and
modern big and complex data tools, such as those from brain
imaging and computational biology, will allow us to map input and
outputs from organoids ’neurological connections. As an example ofSmirnova et al. 10.3389/fsci.2023.1017235
Frontiers in Science frontiersin.org 10