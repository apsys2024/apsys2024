---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:

  - block: slider
    content:
      slides:
      - title: 15th ACM SIGOPS Asia-Pacific Workshop on Systems<br>(APSys 2024)
        content: |
          September 4-5, 2024<br>
          Kyoto, Japan
        align: center
        background:
          image:
            filename: slide1.jpg
            filters:
              brightness: 0.7
            credit: "Image credit: Kiyomizu-dera"
          position: top
      - title: 15th ACM SIGOPS Asia-Pacific Workshop on Systems<br>(APSys 2024)
        content: September 4-5, 2024<br>Kyoto, Japan
        align: center
        background:
          image:
            filename: slide2.jpg
            filters:
              brightness: 0.7
          position: top
      - title: 15th ACM SIGOPS Asia-Pacific Workshop on Systems<br>(APSys 2024)
        content: September 4-5, 2024<br>Kyoto, Japan
        align: center
        background:
          image:
            filename: slide4.jpg
            filters:
              brightness: 0.7
          position: top
      - title: 15th ACM SIGOPS Asia-Pacific Workshop on Systems<br>(APSys 2024)
        content: September 4-5, 2024<br>Kyoto, Japan
        align: center
        background:
          image:
            filename: slide6.jpg
            filters:
              brightness: 0.7
            credit: "Image credit: Hotel Okura"
          position: top
      - title: 15th ACM SIGOPS Asia-Pacific Workshop on Systems<br>(APSys 2024)
        content: September 4-5, 2024<br>Kyoto, Japan
        align: center
        background:
          image:
            filename: slide7.jpg
            filters:
              brightness: 0.7
          position: top
    design:
      slide_height: '16rem'
      is_fullscreen: false
      loop: true
      interval: 4000

  - block: markdown
    content:
      title: Overview
      text: |
        Building on the success of its [predecessors](/past/), the 15th ACM SIGOPS Asia-Pacific Workshop on Systems (APSys 2024) will continue to be a lively forum for systems researchers and practitioners across the world to meet, interact, and collaborate with their peers from the Asia/Pacific region. APSys 2024 will be held in Kyoto, Japan on September 4-5, 2024.

        APSys 2024 will feature [20 paper presentations](/program/) on memory, kernel, migration, networking, AI, edge & cloud, and concurrency, as well as [29 poster presentations](/posters/). In addition, [11 companies](/sponsors/) generously sponsor APSys 2024!
        <!--
        APSys takes a broad view of systems, including but no limited to: operating systems, virtualization, file and storage systems, networked systems, mobile systems, embedded and IoT systems, cloud computing and data centers, edge computing, big data systems, distributed systems, green and sustainable computing, debugging/testing/verification, measurement/monitoring/modeling, reliability/scalability/fault tolerance, security and privacy, systems for machine learning, machine learning for systems, hardware and software interaction, experience with deployed systems, and blockchain and cryptocurrency systems.
        -->

        <div class="row">
        <div class="col">
        {{< cta cta_text="Survey" cta_link="https://forms.office.com/r/96ecU0uNKj" cta_new_tab="false" >}}
        </div>
        </div>
    design:
      columns: '1'

  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: news
    design:
      columns: '1'
      view: list

  - block: markdown
    content:
      title: Sponsors
      text: |
        <div class="text-center mb-3 bg-white">

        <h3 class="gradient-platinum p-2 rounded">Platinum</h3>

        <div class="row align-items-center">
        <div class="col-md">
        {{< figure src="ibm.png" link="https://research.ibm.com/" img_class="mx-auto d-block" max_width="300px" >}}
        </div>
        </div>

        <h3 class="gradient-gold p-2 mb-4 rounded">Gold</h3>

        <div class="row align-items-center">
        <div class="col-md-4 p-4">
        {{< figure src="AntResearch-logo.svg" link="https://www.antresearch.com/" img_class="mx-auto d-block" max_width="220px">}}
        </div>

        <div class="col-md-4 p-4">
        {{< figure src="WDC.Logo.11-PrimaryWordmarkHero.Color-RGB.WW.052622.svg" link="https://www.westerndigital.com/" img_class="mx-auto d-block" max_width="220px" >}}
        </div>

        <div class="col-md-4 p-4">
        {{< figure src="BlackBerry QNX Horizontal.png" link="https://blackberry.qnx.com/en" img_class="mx-auto d-block" max_width="280px" >}}
        </div>
        </div>

        <div class="row align-items-center">
        <div class="col-md-4 p-4">
        {{< figure src="sakura-1-1-basic-rgb-whiteback.svg" link="https://www.sakura.ad.jp/corporate/en/" img_class="mx-auto d-block" max_width="250px" >}}
        </div>
        <div class="col-md-4 p-4">
        {{< figure src="TIS_yoko_color_RGB+.png" link="https://www.tis.com/" img_class="mx-auto d-block" max_width="200px" >}}
        </div>
        <div class="col-md-4 p-4">
        {{< figure src="HW_POS_RGB_Horizontal-300ppi.png" link="https://www.huawei.com/" img_class="mx-auto d-block" max_width="220px" >}}
        </div>
        </div>

        <h3 class="gradient-bronze p-2 rounded">Bronze</h3>

        <div class="row align-items-center">
        <div class="col-md-3 p-4">
        {{< figure src="igel_logo_100219.png" link="https://www.igel.co.jp/en/" img_class="mx-auto d-block" max_width="80px">}}
        </div>
        <div class="col-md-3 p-4">
        {{< figure src="LY.png" link="https://www.lycorp.co.jp/en/" img_class="mx-auto d-block" max_width="70px">}}
        </div>
        <div class="col-md-3 p-4">
        {{< figure src="softether_banner.png" link="https://www.softether.org/" img_class="mx-auto d-block" max_width="160px">}}
        </div>
        <div class="col-md-3 p-4">
        {{< figure src="fixstars-full-color-light.png" link="https://www.fixstars.com/en" img_class="mx-auto d-block" max_width="160px">}}
        </div>
        </div>

        </div>

  - block: markdown
    content:
      title: Organization
      text: |
        <div class="text-center mb-3 bg-white">
        {{< figure src="sigops.png" link="https://www.sigops.org/" img_class="mx-auto d-block" width="200">}}
        </div>

# - block: markdown
#   content:
#     title: Important Dates
#     text: |
#       <div class="row text-center" style="width: fit-content;">
#       <div class="col-md-6">
#       <h4><i class="fa-solid fa-calendar-days"></i> April 25, 2024 (AoE)</h4>
#       <h5><s>Abstract due</s></h5>
#       </div>

#       <div class="col-md-6">
#       <h4><i class="fa-solid fa-calendar-days"></i> May 2, 2024 (AoE)</h4>
#       <h5><s>Submission due</s></h5>
#       </div>

#       <div class="col-md-6">
#       <h4><i class="fa-solid fa-calendar-days"></i> July 1, 2024</h4>
#       <h5><s>Notification to authors</s></h5>
#       </div>

#       <div class="col-md-6">
#       <h4><i class="fa-solid fa-calendar-days"></i> July 30, 2024</h4>
#       <h5><s>Camera-ready due</s></h5>
#       </div>
---
