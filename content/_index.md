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
        content: September 4-5, 2024<br>Kyoto, Japan
        align: center
        background:
          image:
            filename: slide1.jpg
            filters:
              brightness: 0.7
          position: top
    design:
      slide_height: '20rem'
      is_fullscreen: false
      loop: false

  - block: markdown
    content:
      title: Overview
      text: |
        Building on the success of the predecessors in [New Delhi (2010)](https://ap-sys.org/apsys2010), [Shanghai (2011)](https://ap-sys.org/apsys2011), Seoul (2012), Singapore (2013), Beijing (2014), [Tokyo (2015)](https://ap-sys.org/apsys2015), [Hong Kong (2016)](https://ap-sys.org/apsys2016), [Mumbai (2017)](https://ap-sys.org/apsys2017), [Jeju Island (2018)](https://ap-sys.org/apsys2018), Hangzhou (2019), [Virtual (Tsukuba) (2020)](https://ap-sys.org/apsys2020), [Virtual (Hongkong) (2021)](https://ap-sys.org/apsys2021), [Virtual (Singapore) (2022)](https://ap-sys.org/apsys2022), and [Seoul (2023)](https://ap-sys.org/apsys2023), APSys 2024 will continue to be a lively forum for systems researchers and practitioners across the world to meet, interact, and collaborate with their peers from the Asia/Pacific region. The 2024 ACM APSys will be held in Kyoto, Japan on September 4-5, 2024. We take a broad view of computer systems, and solicit papers on topics such as:

        <div class="row">
        <div class="col-md">
        <ul>
        <li>Operating systems
        <li>Virtualization
        <li>File and storage systems
        <li>Networked systems
        <li>Mobile, embedded, and IoT systems
        <li>Cloud computing and data centers
        <li>Edge computing
        <li>Big data systems
        <li>Distributed systems
        </ul>
        </div>
        <div class="col-md">
        <ul>
        <li>Green and sustainable computing
        <li>Debugging, testing, verification
        <li>Measurement, monitoring, and modeling
        <li>Reliability, scalability, and fault tolerance
        <li>Security and privacy
        <li>Systems for machine learning, machine learning for systems
        <li>Hardware and software interaction
        <li>Experience with deployed systems
        <li>Blockchain and cryptocurrency systems
        </ul>
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
      title: Important Dates
      text: |
        <h4><i class="fa-solid fa-calendar-days"></i> April 25, 2024 (AoE)</h4>
        Abstract due
        <h4><i class="fa-solid fa-calendar-days"></i> May 2, 2024 (AoE)</h4>
        Submission due
        <h4><i class="fa-solid fa-calendar-days"></i> July 1, 2024</h4>
        Notification to authors
        <h4><i class="fa-solid fa-calendar-days"></i> July 30, 2024</h4>
        Camera-ready due
---