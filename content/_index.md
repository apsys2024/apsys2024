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
      slide_height: '20rem'
      is_fullscreen: false
      loop: true
      interval: 4000

  - block: markdown
    content:
      title: Overview
      text: |
        Building on the success of the predecessors in [New Delhi (2010)](https://ap-sys.org/apsys2010), [Shanghai (2011)](https://ap-sys.org/apsys2011), Seoul (2012), Singapore (2013), Beijing (2014), [Tokyo (2015)](https://ap-sys.org/apsys2015), [Hong Kong (2016)](https://ap-sys.org/apsys2016), [Mumbai (2017)](https://ap-sys.org/apsys2017), [Jeju Island (2018)](https://ap-sys.org/apsys2018), Hangzhou (2019), [Virtual (Tsukuba) (2020)](https://ap-sys.org/apsys2020), [Virtual (Hongkong) (2021)](https://ap-sys.org/apsys2021), [Virtual (Singapore) (2022)](https://ap-sys.org/apsys2022), and [Seoul (2023)](https://ap-sys.org/apsys2023), APSys 2024 will continue to be a lively forum for systems researchers and practitioners across the world to meet, interact, and collaborate with their peers from the Asia/Pacific region. The 2024 ACM APSys will be held in Kyoto, Japan on September 4-5, 2024.
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
      text: |
        <div class="text-center">
        <h3>Platinum Sponsor</h3>
        (To appear)

        <h3>Gold Sponsor</h3>
        <div class="row">
        <div class="col-md">
        {{< figure src="logos/AntResearch-logo.svg" link="https://www.antgroup.com/en" class="p-3 bg-white" img_class="mx-auto d-block" width="300" >}}
        <a href="https://www.westerndigital.com/">Western Digital</a><br>
        </div>
        </div>

        <div class="row">
        <div class="col-md">
        (To appear)<br>
        (To appear)
        </div>
        </div>

        <h3>Bronze Sponsor</h3>
        {{< figure src="logos/igel_logo_100219.png" link="https://www.igel.co.jp/en/" img_class="mx-auto d-block" width="120">}}
        </div>


  - block: markdown
    content:
      title: Organization
      text: |
        {{< figure src="logos/sigops.png" link="https://www.sigops.org/" img_class="mx-auto d-block" width="200">}}

  - block: markdown
    content:
      title: Important Dates
      text: |
        <div class="row text-center" style="width: fit-content;">
        <div class="col-md-6">
        <h4><i class="fa-solid fa-calendar-days"></i> April 25, 2024 (AoE)</h4>
        <h5><s>Abstract due</s></h5>
        </div>

        <div class="col-md-6">
        <h4><i class="fa-solid fa-calendar-days"></i> May 2, 2024 (AoE)</h4>
        <h5><s>Submission due</s></h5>
        </div>

        <div class="col-md-6">
        <h4><i class="fa-solid fa-calendar-days"></i> July 1, 2024</h4>
        <h5>Notification to authors</h5>
        </div>

        <div class="col-md-6">
        <h4><i class="fa-solid fa-calendar-days"></i> July 30, 2024</h4>
        <h5>Camera-ready due</h5>
        </div>
---
