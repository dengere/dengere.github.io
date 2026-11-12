# CSD — Jekyll website

A lightweight semantic HTML5 website for C ve Sistem Programcıları Derneği on GitHub Pages. It uses a small, responsive, GitHub-inspired stylesheet without JavaScript, external fonts, or UI frameworks. Source names and front matter are English; visitor-facing content is Turkish.

## Local development

Install Ruby and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve
```

Build production output with `JEKYLL_ENV=production bundle exec jekyll build`. GitHub Pages can build this source using its standard Jekyll deployment. No custom plugin or backend is required. The configured test origin is `https://dengere.github.io`. Change `url` only when the destination changes. Set `baseurl` if deploying beneath a repository subpath.

## Structure

| Path | Purpose |
|---|---|
| `pages/` | Static pages and collection listing pages |
| `_courses/` | One Markdown file per course |
| `_announcements/` | One Markdown file per announcement, including seminars |
| `_resources/` | One Markdown file per resource |
| `_layouts/` | Shared default, page, listing and detail layouts |
| `_includes/` | Shared footer, item (card) and Turkish date formatting |
| `_data/labels.yml` | Turkish display labels for English type values |

All three collections have `output: true`: Jekyll generates detail pages automatically. Listings and homepage use the same collection source files; do not create duplicate records. Public URLs use Turkish paths through collection permalinks and page front matter.

The homepage strictly follows this order:
1. Association full name and short identity narrative
2. Upcoming courses (up to 4 items and link to full listing)
3. Announcements (up to 4 items and link to full listing)
4. Resources (up to 4 items and link to full listing)
5. Contact and necessary footer links (in `footer.html`)

Primary navigation is in the shared site header; additional organization and contact links are in the footer.

## Add a course

Create `_courses/example-course.md`:

```yaml
---
title: "Eğitim başlığı"
summary: "Eğitimin tek cümlelik açıklaması."
type: course
instructor: "Doğrulanmış eğitmen adı"
start_date: "2027-02-01"
format: online
schedule: "Doğrulanmış program"
status: upcoming
featured: true
order: 1
sample: false
---
Eğitimin detayları buraya yazılır.
```

Omit unknown fields. Missing start dates show “Tarih duyurulacak”; missing formats show “Duyurulacak”. `format` accepts `online` or `in_person`. `status` accepts `upcoming` or `archived`.

The homepage shows up to four `featured: true`, `status: upcoming` courses, ascending by `order`. Unique order numbers are recommended. Move completed courses to `archived`; the choice is editorial, not based on the build machine's current date.

## Add an announcement

Create `_announcements/example-announcement.md`:

```yaml
---
title: "Duyuru başlığı"
summary: "Kısa açıklama."
type: seminar
date: "2026-11-10"
event_date: "2026-12-01"
format: online
featured: true
sample: false
---
Duyurunun tam metni.
```

Types: `seminar`, `online_meeting`, `news`, `achievement`, `memorial`. Publication `date` and optional `event_date` are separate. Omit event fields for non-events. The homepage shows up to four featured announcements by descending publication date. Do not set a future publication date until publication is intended.

## Add a resource

Create `_resources/example-resource.md`:

```yaml
---
title: "Kaynak başlığı"
summary: "Tek cümlelik açıklama."
type: article
author: "Doğrulanmış yazar"
access: free
external_url: "https://example.org/verified-resource"
featured: true
order: 1
sample: false
---
Kaynağın açıklaması.
```

Types: `book`, `article`, `notes`, `video`. Access: `free` or `paid`; omit when unknown. Items link to local detail pages. A verified `external_url` appears there separately. Never add placeholder external URLs to production records. The homepage shows up to four featured resources ordered by `order`.

## Styling, HTML5 and Accessibility

The site uses a local stylesheet (`assets/css/style.css`) for a restrained, responsive layout inspired by GitHub's default interface. It follows the system light/dark preference and uses the platform's standard sans-serif fonts without external font requests.

- Headings use `h1`, `h2`, `h3`.
- Major page segments use `section` and `article`.
- Text content uses standard `p` paragraphs and `time` for dates.
- Listings and meta information use semantic `ul`, `ol`, `li`, and `dl`, `dt`, `dd`.
- Links use plain `a` tags, with visible keyboard focus.
- Layout classes are used only to style shared page regions and listing cards; templates contain no inline styles.
- No JavaScript, search/filter bars, or interactive dropdown menus are used.
- Navigation links are organized in the shared header and footer.

## Content provenance and remaining work

Existing records were migrated from the test repository and explicitly marked `sample: true`. Their dates, instructors and descriptions are unverified, not real registration announcements. Their former sample/unverified external URLs were removed rather than exposed as working resources. Archive source remains in Git history.

The about text and contact details derive from https://csystem.org/hakkimizda/ (reviewed 10 November 2026). Confirm contact details before publication. Board, membership and charter pages explicitly state that approved content is pending.
