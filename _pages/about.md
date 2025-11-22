---
permalink: /
title: "Welcome to my personal website!"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a MSCA Postdoc researcher in Cork, Ireland. I work at [APC Microbiome](https://www.ucc.ie/en/apc/) as part of the Andrey Shkoporov Group.

## 🔬 Research Interests

I am a computational microbiologist. I am interested in the study of ancient microbiome in dental calculus and paleofeces, but more precisly the viral part of these microbiomes. I study these by analysing sequence data (proteins, genomes) at different scales. I try to be able to detect viruses (eukaryote viruses and bacteriophages) in ancient samples to be able to compare with modern ones and so understood how change in the human population could have impact these communities.

[Read more about my research](/research/){: .btn .btn--modern-primary}

## 🔥 Recent Publications

<div class="publications">
  <ul>
    {% assign recent_pubs = site.publications | sort: 'date' | reverse %}
    {% for post in recent_pubs limit:3 %}
      {% include archive-single-cv.html %}
    {% endfor %}
  </ul>
</div>

[See all publications](/publications/){: .btn .btn--modern-info}

