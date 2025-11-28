---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D in Life Science Complexity, University Pierre et Marie Curie – Sorbonne University, 2019
* M.S. in Molecular and Cellular Biology, University Pierre et Marie Curie – Sorbonne University, 2016
* B.S. in Sciences and Technologies, University Pierre et Marie Curie – Sorbonne University, 2014

Work experience
======
* 2021-2025: Postdoctoral Researcher & MSCA Fellow
  * University College Cork
  * Topic: Diversity of bacteriophages in the ancien human microbiomes
  * Supervision: Andrey Shkoporov, Colin Hill & Christina Warinner
  
* 2020-2021: Postdoctoral Researcher 
  * University of Florida
  * Topic: Study of enzyme of unknown function related to the vitamin B6
  * Supervision: Valerie de Crecy Lagard
  
* 2016-2019: PhD Student
  * Institut Pasteur - Sorbonne University
  * Topic: Understanding event of evolution of the Type IV Filament super family
  * Supervision: Eduardo Rocha & Sophie Abby

Supervising Experience
======
* 2023-2024: 
  * Undergraduate student from Applied University of Science Leiden
  * Project: Rapid co-evolution of bacteria and bacteriophages in the human gut microbiome
  * Co-supervision with Andrey Shkoporov

* 2022: 
  * MSc bioinformatic student from University College Cork
  * Project: Comparison of different viruses’ detection software
  * Co-supervision with Andrey Shkoporov

* 2022: 
  * Undergraduate student from Applied University of Science Leiden
  * Project: Characterization of patterns of diversity and conservation among structural proteins of crAss-like phages
  * Co-supervision with Andrey Shkoporov
  
Grants & Awards
======
* 2021: Marie Skłodowska-Curie Actions (MSCA) Postdoctoral Fellowship
  * Project: ARCHAIC - Diversity of bacteriophages in the ancient human microbiome
  * Grant Agreement ID: [101111040](https://cordis.europa.eu/project/id/101111040)

Publications
======
  <div class="publications">
  <ul>
    {% assign reversed_pubs = site.publications | where_exp: "item", "item.publication_type != 'thesis'" | reverse %}
    {% for post in reversed_pubs %}
      {% include archive-single-cv.html last_item=forloop.last %}
    {% endfor %}
  </ul>
  </div>
  
Talks
======
  <div class="publications">
  <ul>
    {% assign reversed_talks = site.talks | reverse %}
    {% for post in reversed_talks %}
      {% include archive-single-talk-cv.html last_item=forloop.last %}
    {% endfor %}
  </ul>
  </div>
  
Teaching
======
  <div class="publications">
  <ul>
    {% assign reversed_teaching = site.teaching | reverse %}
    {% for post in reversed_teaching %}
      {% include archive-single-teaching-cv.html last_item=forloop.last %}
    {% endfor %}
  </ul>
  </div>
