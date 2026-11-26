---
layout: default
title: Hakkımızda
permalink: /hakkimizda/
---

<article class="markdown-body about-page">

  {% capture about %}{% include_relative about-content.md %}{% endcapture %}
  {{ about | markdownify }}

  <h2 id="iletisim" class="section-divider">İletişim</h2>
  {% capture contact %}{% include_relative contact.md %}{% endcapture %}
  {{ contact | split: '---' | last | markdownify }}

  <h2 id="uyelik" class="section-divider">Dernek Üyeliği</h2>
  {% capture membership %}{% include_relative membership.md %}{% endcapture %}
  {{ membership | split: '---' | last | markdownify }}

  <h2 id="yonetim" class="section-divider">Yönetim Kurulu</h2>
  {% capture board %}{% include_relative board.md %}{% endcapture %}
  {{ board | split: '---' | last | markdownify }}
</article>