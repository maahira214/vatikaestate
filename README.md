# Vatika Estate — Website

A static website built from scratch with plain HTML, CSS and JavaScript. It has no WordPress and no plugins.

## View locally
```
python -m http.server 5500
```
Open http://localhost:5500

## Pages
| File | Page |
|---|---|
| index.html | Home |
| about.html | About Us |
| projects.html | All projects (ongoing + 8 completed, each with its own `#anchor`) |
| vatika-luxora.html | Vatika Luxora project detail |
| gallery.html | Gallery with filters + lightbox |
| contact.html | Contact + Schedule a visit form + map |
| privacy-policy.html / terms.html | Legal pages |
| 404.html | Not-found page |

## Editing content
All pages are generated from `_build/build.py`, so the header, footer, forms and contact details are written once.
Edit that file, then run:
```
python _build/build.py
```
Styles: `assets/css/style.css` · Scripts: `assets/js/main.js` (the `CONFIG` block at the top holds the lead email, phone and brochure path).

## Lead forms (IMPORTANT: one-time activation)
All forms (popup, Enquire Now, Get Brochure, Request a Visit, Contact, Luxora sidebar) send leads to
**vatikaestate2020@gmail.com** through FormSubmit (https://formsubmit.co). You don't need a server or any code.

1. After the site is live, submit any form once yourself.
2. FormSubmit sends an **activation email** to vatikaestate2020@gmail.com. Click **Activate Form**.
3. Every lead after that lands in the inbox as a formatted table (name, phone, email, project, visit date, page).

The brochure (`assets/docs/vatika-luxora-brochure.pdf`) is not linked anywhere on the site. Visitors can download it only after they submit a lead form.

## Deploying to Hostinger
Upload everything **except** `_build/`, `.claude/`, `README.md` and `Website-Changes-Checklist.md` to `public_html`.
Remove the old WordPress files first. Keep a backup.
`.htaccess` adds 301 redirects from the old WordPress URLs (`/about-us/`, `/contact/`, `/all-projects/vatika-luxora-ongoing/`, …),
so existing Google rankings carry over. It also sets caching and security headers.
After going live, submit `sitemap.xml` in Google Search Console.
