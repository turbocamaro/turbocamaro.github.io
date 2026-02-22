---
layout: categories
title: Build Sheet
permalink: /categories/
icon: fas fa-stream
order: 1
---
<div class="flex-grow-1">
  <ul class="list-group list-group-flush">
    {% for category in site.categories %}
      {% capture category_name %}{{ category | first }}{% endcapture %}
      
      <li class="list-group-item d-flex justify-content-between align-items-center">
        <a href="{{ site.baseurl }}/categories/{{ category_name | slugify }}/" class="ml-1">
          {% case category_name %}
            {% when "INTERIOR" %}
              <i class="fas fa-couch fa-fw mr-2"></i>
            {% when "EXTERIOR" %}
              <i class="fas fa-car fa-fw mr-2"></i>
            {% when "MECHANICAL" %}
              <i class="fas fa-tools fa-fw mr-2"></i>
            {% when "ENGINE" %}
              <i class="fas fa-engine fa-fw mr-2"></i>
            {% when "TURBOCHARGER" %}
              <i class="fas fa-wind fa-fw mr-2"></i>
            {% when "FUEL & TUNING" %}
              <i class="fas fa-gas-pump fa-fw mr-2"></i>
            {% else %}
              <i class="fas fa-folder-open fa-fw mr-2"></i>
          {% endcase %}
          {{ category_name }}
        </a>
        <span class="badge badge-pill badge-secondary">{{ category | last | size }}</span>
      </li>
    {% endfor %}
  </ul>
</div>
