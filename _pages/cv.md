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
* B.S. in Sciences and Technologies, University Pierre et Marie Curie – Sorbonne University, 2014
* M.S. in Molecular and Cellular Biology, University Pierre et Marie Curie – Sorbonne University, 2016
* Ph.D in Life Science Complexity, University Pierre et Marie Curie – Sorbonne University, 2019

Work experience
======
* 2021- Current time: Postdoctoral Researcher & MSCA Fellow
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

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
