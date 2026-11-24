---
layout: default
title: Hakkımızda
permalink: /hakkimizda/
---

<article class="markdown-body about-page">
  <h2 class="section-divider">CSD Hakkında</h2>

  {% capture about %}{% include_relative about-content.md %}{% endcapture %}
  {{ about | markdownify }}

<div class="intro">
  <p><a href="{{ '/tuzuk/' | relative_url }}">Dernek Tüzüğü &rsaquo;</a></p>
</div>
  <h2 class="section-divider">İletişim</h2>
  {% capture membership %}{% include_relative contact.md %}{% endcapture %}
  {{ membership | split: '---' | last | markdownify }}

  <h2 class="section-divider">Dernek Üyeliği</h2>
  {% capture membership %}{% include_relative membership.md %}{% endcapture %}
  {{ membership | split: '---' | last | markdownify }}

  <h2 class="section-divider">Yönetim Kurulu</h2>
  {% capture board %}{% include_relative board.md %}{% endcapture %}
  {{ board | split: '---' | last | markdownify }}

</article>