---
layout: archive
title: "Community Engagement & Service"
permalink: /community/
author_profile: true
---

{% include base_path %}

<style>
.logo-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 40px;
  justify-content: flex-start; /* Align left */
  margin-bottom: 30px;
}

.logo-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 150px;
  text-align: center;
}

.logo-item {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 3px solid #f0f0f0;
  background-color: white;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  margin-bottom: 15px;
}

.logo-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 12px rgba(0,0,0,0.15);
  border-color: #ddd;
}

.logo-item img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  padding: 15px;
}

.logo-title {
  font-size: 0.9em;
  line-height: 1.3;
  color: #333;
}
</style>

## Scientific Community 

<div class="logo-grid">
  {% for society in site.data.community.scientific_societies %}
  <div class="logo-wrapper">
    {% if society.url %}
    <a href="{{ society.url }}" class="logo-item">
      <img src="{{ society.logo }}" alt="{{ society.name }} Logo">
    </a>
    {% else %}
    <div class="logo-item">
      <img src="{{ society.logo }}" alt="{{ society.name }} Logo">
    </div>
    {% endif %}
    <div class="logo-title"><strong>{{ society.name }}</strong><br>{{ society.role }}<br>({{ society.dates }})</div>
  </div>
  {% endfor %}
</div>

## General Public 

<div class="logo-grid">
  {% for society in site.data.community.public_societies %}
  <div class="logo-wrapper">
    {% if society.url %}
    <a href="{{ society.url }}" class="logo-item">
      <img src="{{ society.logo }}" alt="{{ society.name }} Logo">
    </a>
    {% else %}
    <div class="logo-item">
      <img src="{{ society.logo }}" alt="{{ society.name }} Logo">
    </div>
    {% endif %}
    <div class="logo-title"><strong>{{ society.name }}</strong><br>{{ society.role }}<br>({{ society.dates }})</div>
  </div>
  {% endfor %}
</div>
  
## Organization of conferences

<div class="logo-grid">
  {% for conf in site.data.community.conferences %}
  <div class="logo-wrapper">
    {% if conf.url %}
    <a href="{{ conf.url }}" class="logo-item">
      <img src="{{ conf.logo }}" alt="{{ conf.name }} Logo">
    </a>
    {% else %}
    <div class="logo-item">
      <img src="{{ conf.logo }}" alt="{{ conf.name }} Logo">
    </div>
    {% endif %}
    <div class="logo-title"><strong>{{ conf.name }}</strong><br>{{ conf.dates }}<br>{{ conf.location }}</div>
  </div>
  {% endfor %}
</div>

## General Public Events

<div class="logo-grid">
  {% for event in site.data.community.public_events %}
  <div class="logo-wrapper">
    {% if event.url %}
    <a href="{{ event.url }}" class="logo-item">
      <img src="{{ event.logo }}" alt="{{ event.name }} Logo">
    </a>
    {% else %}
    <div class="logo-item">
      <img src="{{ event.logo }}" alt="{{ event.name }} Logo">
    </div>
    {% endif %}
    <div class="logo-title"><strong>{{ event.name }}</strong><br>{{ event.dates }}<br>{{ event.location }}</div>
  </div>
  {% endfor %}
</div>
