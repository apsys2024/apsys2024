---
---
# Program

<style>
div.program h3 {
    border: solid 1px blue;
    border-left: solid 8px blue;
    padding: 0.2rem;
    padding-left: 0.5rem;
    margin-bottom: 1.5rem;
    color: black;
    background: #eef;
}
div.program h3.break {
    border: solid 1px gray;
    border-left: solid 8px gray;
    color: black;
    background: #eee;
}
</style>
<div class="program">

{{% callout info %}}
25 minutes per presentation
{{% /callout %}}

## Wednesday, September 4th

### 09:00-09:15 Opening remarks

### 09:15-10:15 Keynote

{{< figure src="dan_ports.jpg" width="720px" height="720px" img_class="avatar avatar-circle float-left" >}}

#### The Future of Cloud Networking is Systems

<p style="font-size: medium;">Dr. Dan R. K. Ports (Principal Researcher at Microsoft Research)</p>

##### Abstract:

As cloud platforms evolve, the boundaries between networking and systems are increasingly blurred. Cloud networking not only asks us to solve a challenging systems problem -- providing an efficient, reliable, and secure virtual infrastructure -- but offers us opportunities to rethink our approach to classic challenges in distributed systems. This keynote will explore the potential of systems/networking co-design through the lens of a cloud-scale hardware-accelerated load balancing platform.
Specifically, I will discuss how programmable networking technology, including programmable switches and smart NICs, enables these load balancers to achieve dramatically higher efficiency than existing software solutions while simultaneously offering increased flexibility for custom, application-specific load balancing logic. Looking to the future, I'll describe three opportunities that this design offers for redefining the architecture of distributed systems with new load-balancing, migration, and snapshotting algorithms, paving the way to a new generation of high-performance, resilient, and scalable cloud services.

##### Bio:

<i>
Dan R. K. Ports is a Principal Researcher in the Systems Research Group at Microsoft Research, where he leads the Prometheus project -- a long-term collaboration between MSR, academic research groups, hardware vendors, and product groups. Specializing in distributed systems and networking, Dan works across the entire systems stack, focusing on leveraging emerging datacenter technologies like programmable networks. Recent efforts within the Prometheus project have emphasized enhancing the performance, flexibility, and applications of cloud-scale load balancers. He earned his Ph.D. from MIT in 2012 and previously served on the faculty at the University of Washington. Dan's contributions to the field have been recognized with best paper awards at NSDI and OSDI.
</i>

<h3 class="break">10:15-10:45 Break</h3>

### 10:45-12:00 Session 1: Memory Madness

###### Session Chair: Frank Bellosa (Karlsruhe Institute of Technology)

#### (1) Virtual Memory Revisited for Tiered Memory
Oliver Giersch (Brandenburgische Technische Universität Cottbus-Senftenberg); Dustin Nguyen (Friedrich-Alexander-Universität Erlangen-Nürnberg); Jörg Nolte;Brandenburgische Technische Universität Cottbus-Senftenberg; Wolfgang Schröder-Preikschat (Friedrich-Alexander-Universität Erlangen-Nürnberg)

#### (2) Persistent Memory I/O-Aware Task Placement for Mitigating Resource Contention
Hyunwoo Ahn, Jongseok Kim, Euiseong Seo (Sungkyunkwan University)

#### (3) Polar: A Managed Runtime with Hotness-Segregated Heap for Far Memory
Dat Nguyen, Khanh Nguyen (Texas A&M University)

<h3 class="break">12:00-13:15 Lunch (on your own)</h3>

{{% callout info %}}
Bringing your own food and drink into the venue room is not permitted.
{{% /callout %}}

### 13:15-14:30 Session 2: Kernel Kraziness

###### Session Chair: Kenichi Yasukata (IIJ Research Laboratory)

#### (4) Chaos: Function Granularity Runtime Address Layout Space Randomization for Kernel Module
Zihao Chang, Jihan Lin (State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences; Zhongguancun Laboratory); Haifeng Sun (Peking University); Runkuan Li (Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences; Zhongguancun Laboratory); Ying Wang (State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences); Bin Hu (Institute of Computing Technology, Chinese Academy of Sciences; Zhongguancun Laboratory); Xiaofang Zhao (Institute of Computing Technology, Chinese Academy of Sciences; Zhongguancun Laboratory; Institute of Intelligent Computing Technology, Suzhou, CAS; University of Chinese Academy of Sciences, Nanjing); Dejun Jiang, Sun Ninghui, Sa Wang (State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences; Zhongguancun Laboratory)

#### (5) Framekernel: A Safe and Efficient Kernel Architecture via Rust-based Intra-kernel Privilege Separation
Yuke Peng (Southern University of Science and Technology(SUSTech)); Hongliang Tian (Ant Group); Jinyi Xian, Shuai Zhou (Southern University of Science and Technology(SUSTech)); Shoumeng Yan (Ant Group); Yinqian Zhang (Southern University of Science and Technology(SUSTech))

#### (6) Developing Process Scheduling Policies in User Space with Common OS Features
Kenichi Yasukata (IIJ Research Laboratory); Kenta Ishiguro (Keio University)

<h3 class="break">14:30-15:00 Break</h3>

### 15:00-16:15 Session 3: Migration Mayhem

###### Session Chair: Kenta Ishiguro (Keio University)

#### (7) SmartNIC-enabled Live Migration for Storage Optimized VMs
Jiechen Zhao (Microsoft Research/University of Toronto); Ran Shu, Lei Qu, Ziyue Yang (Microsoft Research); Natalie Enright Jerger (University of Toronto); Derek Chiou (University of Texas at Austin/Microsoft); Peng Cheng, Yongqiang Xiong (Microsoft Research)

#### (8) Designing and Implementing Live Migration Support for Arm-based Confidential VMs
Fang-Jie Yang, Jian-Lin Li (National Taiwan University); Kaiwen Xue (Carnegie Mellon University); Shih-Wei Li (National Taiwan University)

#### (9) Towards Efficient End-to-End Encryption for Container Checkpointing Systems
Radostin Stoyanov (University of Oxford); Adrian Reber, Daiki Ueno (Red Hat); Michał Cłapiński, Andrei Vagin (Google); Rodrigo Bruno (INESC-ID, Instituto Superior Técnico, Universidade de Lisboa)

### 16:15-17:15 Poster session

#### [Accepted Posters](/posters/)

### 18:00- Banquet


## Thursday, September 5th

### 09:00-10:15 Session 4: Network Netsense

###### Session Chair: KyoungSoo Park (Seoul National University)

#### (10) NotNets: Accelerating Microservices by Bypassing the Network
Peter Alvaro (U. C. Santa Cruz); Matthew Adiletta (Intel Corporation); David Cheng (Yale University); Adrian Cockcroft (OrionX); Frank Hady, Ramesh Illikkal (Intel Corporation); Esteban Ramos (U. C. Santa Cruz); Robert Soulé (Yale University)

#### (11) FHA: Flow-level High Availability on Programmable Network Hardware for Cloud Provider
Ying Chu (USTC & Microsoft Research); Ziyuan Liu (Beihang University & Microsoft Research); Riff Jiang, Ze Gan, Junhua Zhai, Guohan Lu (Microsoft); Zhixiong Niu, Yongqiang Xiong (Microsoft Research)

#### (12) Split gRPC: An Isolation Architecture for RPC Software Stacks
Esteban Ramos (U. C. Santa Cruz); Robert Soulé (Yale University); Peter Alvaro (U. C. Santa Cruz); Pietro Bressana (Intel Corporation); Edmund Chen, Uri Cummings (Unaffiliated); Rui Li (Intel Corporation); James Tsai (Intel Labs); Rajit Manohar (Yale University)

<h3 class="break">10:15-10:45 Break</h3>

### 10:45-12:00 Session 5: AI Antics

###### Session Chair: Hiroshi Yamada (Tokyo University of Agriculture and Technology)

#### (13) Towards a Flexible and High-Fidelity Approach to Distributed DNN Training Emulation
Banruo Liu (Tsinghua University); Mubarak Ojewale (KAUST); Yuhan Ding (Tsinghua University); Marco Canini (KAUST)

#### (14) SERAPH: A Performance-Cost Aware Tuner for Training Reinforcement Learning Model on Serverless Computing
Jinbo Han, Xingda Wei, Rong Chen, Haibo Chen (Shanghai Jiao Tong University)

#### (15) BMoss: Reconfigurable hardware accelerator for scalable plagiarism detection
Esmerald Aliaj, Alberto Krone-Martins, Sang-Woo Jun (University of California, Irvine)

<h3 class="break">12:00-13:15 Lunch (on your own)</h3>

{{% callout info %}}
Bringing your own food and drink into the venue room is not permitted.
{{% /callout %}}

### 13:15-14:30 Session 6: Edge and Cloud Capers

###### Session Chair: TBD

#### (16) Toward an Edge-Friendly Distributed Object Store for Serverless Functions
Liting Hu (UC Santa Cruz); Xin Chen (Georgia Institute of Technology); Manoj Prabhakar Paidiparthy (Virginia Tech)

#### (17) Hora: High Assurance Periodic Availability Guarantee for Life-Critical Applications on Smartphones
Dylan Zueck, Nathaniel Atallah, Ian Do (University of California, Irvine); Zhihao (Zephyr) Yao (New Jersey Institute of Technology); Ardalan Amiri Sani (University of California, Irvine)

#### (18) Faster FUSE Filesystems with Efficient Data Transfers
Giorgos Kappes, Stergios V. Anastasiadis (University of Ioannina)

<h3 class="break">14:30-15:00 Break</h3>

### 15:00-15:50 Session 7: Concurrency Chaos

###### Session Chair: TBD

#### (19) WoundDie: Concurrency Control Protocol with Lightweight Priority Control
Kodai Doki (Keio University); Takashi Hoshino (Cybozu Labs, Inc.); Hideyuki Kawashima (Keio University)

#### (20) ONIONDISK: A Log-Structured Write-Optimal Virtual Block Device
Shiyu Wang, Zhihao Zhang, Yiming Zhang (Xiamen University)

### 15:50-16:00 Closing remarks

</div>
