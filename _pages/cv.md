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
  
Grants & Awards
======
* **2021**: Marie Skłodowska-Curie Actions (MSCA) Postdoctoral Fellowship
  * Project: ARCHAIC - Diversity of bacteriophages in the ancient human microbiome
  * Grant Agreement ID: [101111040](https://cordis.europa.eu/project/id/101111040)

Scientific outreach activities
======
* Organization of conferences:
  * 2019: [Alphy meeting](https://lbbe-dmz.univ-lyon1.fr/alphy-legacy/lbbe-dmz.univ-lyon1.fr/spip_alphy/spip349d.html?article70) (MNHN - Paris, France)
  * 2019: [Boris Ephrussi Day](https://sites.google.com/site/journeeborisephrussi/) (Ecole Normale Supérieure - Paris, France)
  * 2018: [YRLS](http://yr2i.org/wp-content/uploads/2018/02/poster_YRLS_2018_VFinale2-copie.jpg) (Ecole Normale Supérieure - Paris, France)
  * 2018: [Boris Ephrussi Day](https://sites.google.com/site/journeeborisephrussi/) (Sorbonne University - Campus Jussieu - Paris, France)
  * 2017: [Boris Ephrussi Day](https://sites.google.com/site/journeeborisephrussi/) (Institut Pasteur - Paris, France)

Publications
======
  <div class="publications">
  <ul>
    {% assign reversed_pubs = site.publications | reverse %}
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
