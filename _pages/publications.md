---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find a complete list of my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

{% assign publications_by_year = site.publications | group_by_exp:"post", "post.date | date: '%Y'" | sort: "name" | reverse %}

{% for year in publications_by_year %}
  <h2>{{ year.name }}</h2>
  {% for post in year.items %}
    {% include archive-single-pub.html %}
  {% endfor %}
{% endfor %}
