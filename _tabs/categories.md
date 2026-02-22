---
layout: categories
title: Build Sheet
permalink: /categories/
icon: fas fa-stream
order: 1
---
<div class="flex-grow-1">
  <ul class="list-group list-group-flush">
    {% assign sorted_categories = site.categories | sort %}
    {% for category in sorted_categories %}
      {% capture category_name %}{{ category | first }}{% endcapture %}
      {% assign slug = category_name | downcase %}
      
      <li class="list-group-item d-flex justify-content-between align-items-center">
        <a href="{{ site.baseurl }}/categories/{{ category_name | slugify }}/" class="ml-1">
          {% if slug contains "engine" %}
            <i class="fas fa-cogs fa-fw mr-2"></i>
          {% elif slug contains "interior" %}
            <i class="fas fa-couch fa-fw mr-2"></i>
          {% elif slug contains "exterior" %}
            <i class="fas fa-car fa-fw mr-2"></i>
          {% elif slug contains "mechanical" %}
            <i class="fas fa-wrench fa-fw mr-2"></i>
          {% elif slug contains "turbo" %}
            <i class="fas fa-wind fa-fw mr-2"></i>
          {% elif slug contains "fuel" %}
            <i class="fas fa-gas-pump fa-fw mr-2"></i>
          {% else %}
            <i class="fas fa-folder-open fa-fw mr-2"></i>
          {% endif %}
          {{ category_name }}
        </a>
        <span class="badge badge-pill badge-secondary">{{ category | last | size }}</span>
      </li>
    {% endfor %}
  </ul>
</div>
