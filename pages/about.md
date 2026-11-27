---
layout: default
title: Hakkımızda
permalink: /hakkimizda/
---

<article class="markdown-body about-page">
  <h1>Hakkımızda</h1>

  {% capture about %}{% include_relative about-content.md %}{% endcapture %}
  {{ about | markdownify }}

  <h2 id="iletisim">İletişim</h2>
  {% capture contact %}{% include_relative contact.md %}{% endcapture %}
  {{ contact | split: '---' | last | markdownify }}

  <h2 id="yonetim">Yönetim Kurulu</h2>
  {% capture board %}{% include_relative board.md %}{% endcapture %}
  {{ board | split: '---' | last | markdownify }}
</article>