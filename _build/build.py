"""
Vatika Estate static site builder.

Generates every .html page in the site root from the shared layout below, so the
header, footer, lead form, popup and contact details stay identical everywhere.

    python _build/build.py

Edit content here (or the CONTACT constants) and re-run. No dependencies.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = "https://vatikaestate.co.in"

# ---------------------------------------------------------------- contact data
PHONE_DISPLAY = "+91 83569 01661"
PHONE_TEL = "+918356901661"
WA_NUMBER = "918356901661"
WA_LINK = f"https://wa.me/{WA_NUMBER}?text=Hi%20Vatika%20Estate%2C%20I%27m%20interested%20in%20your%20agricultural%20land%20projects."
EMAIL_INFO = "info@vatikaestate.co.in"
EMAIL_SALES = "sales@vatikaestate.co.in"
ADDRESS = "Office No. 1203, 12th Floor, Centrum IT Park, Plot No. C-8, Wagle Estate Road (near Satkar Hotel), Thane West, Maharashtra"
FACEBOOK = "https://www.facebook.com/vatikaestate.co"
INSTAGRAM = "https://www.instagram.com/vatikaestate/"
LINKEDIN = "https://in.linkedin.com/company/vatika-estate"
MAP_EMBED = "https://www.google.com/maps?q=Centrum+IT+Park,+Wagle+Estate,+Thane+West,+Maharashtra&output=embed"
MAP_LINK = "https://www.google.com/maps/search/?api=1&query=Centrum+IT+Park+Wagle+Estate+Thane+West"

COMPLETED = [
    ("vatika-farm", "Vatika Farm"),
    ("vatika-hills", "Vatika Hills"),
    ("vatika-greens", "Vatika Greens"),
    ("vatika-aangan-1", "Vatika Aangan-1"),
    ("vatika-aangan-2", "Vatika Aangan-2"),
    ("gokul-vatika", "Gokul Vatika"),
    ("vatika-estate", "Vatika Estate"),
    ("vatika-roots", "Vatika Roots"),
]
LUXORA = "Vatika Luxora (Ongoing)"

# ---------------------------------------------------------------- images
IMG = {
    "farmhouse-kitchen-garden-vatika-estate": (600, 900),
    "farmhouse-plot-shahapur-vatika-estate": (736, 1113),
    "organic-farming-plot-kasara": (600, 804),
    "weekend-home-kasara-hills": (577, 1024),
    "second-home-farmhouse-garden-vatika": (736, 736),
    "land-buying-consultation-vatika-estate": (736, 736),
    "fruit-orchard-agricultural-land-shahapur": (735, 985),
    "green-paddy-fields-agricultural-land": (736, 736),
    "vatika-luxora-plot-layout-plan": (1080, 768),
    "sunrise-farmland-shahapur": (736, 920),
    "rice-crop-fertile-soil-kasara": (736, 736),
    "agricultural-land-kasara-vatika-luxora": (736, 736),
    "farmland-sunset-view-shahapur": (736, 736),
    "aerial-view-farmhouse-plots-vatika": (735, 985),
    "homestead-farmhouse-vegetable-garden": (600, 803),
    "orchard-pathway-farmhouse-kasara": (736, 1104),
}


def img(name, alt, sizes="(max-width: 680px) 100vw, 50vw", cls="", eager=False):
    w, h = IMG[name]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="assets/img/{name}.webp" srcset="assets/img/{name}-sm.webp 560w, assets/img/{name}.webp {w}w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{alt}" {load} decoding="async">')


def icon(name, cls=""):
    fill = " icon--fill" if name in ("fb", "li") else ""
    extra = f" {cls}" if cls else ""
    return f'<svg class="icon{fill}{extra}" aria-hidden="true" focusable="false"><use href="#i-{name}"></use></svg>'


SPRITE = """<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="i-arrow-left" viewBox="0 0 24 24"><path d="M19 12H5M11 6l-6 6 6 6"/></symbol>
<symbol id="i-chev" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h10"/></symbol>
<symbol id="i-close" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></symbol>
<symbol id="i-leaf" viewBox="0 0 24 24"><path d="M5 21c0-9 5-15 15-16-1 10-7 15-15 16z"/><path d="M5 21 13 13"/></symbol>
<symbol id="i-road" viewBox="0 0 24 24"><path d="M8 3 4 21M16 3l4 18M12 4v3M12 10.5v3M12 17v3"/></symbol>
<symbol id="i-water" viewBox="0 0 24 24"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/><path d="M9 14a3 3 0 0 0 3 3"/></symbol>
<symbol id="i-tree" viewBox="0 0 24 24"><circle cx="12" cy="9" r="6"/><path d="M12 15v7M9 22h6M12 11l-2.5-2.5M12 13l3-3"/></symbol>
<symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/></symbol>
<symbol id="i-trend" viewBox="0 0 24 24"><path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/></symbol>
<symbol id="i-calendar" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></symbol>
<symbol id="i-download" viewBox="0 0 24 24"><path d="M12 3v12M7 10l5 5 5-5M5 21h14"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></symbol>
<symbol id="i-home" viewBox="0 0 24 24"><path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/></symbol>
<symbol id="i-fence" viewBox="0 0 24 24"><path d="M5 21V7l2-3 2 3v14M15 21V7l2-3 2 3v14M3 10h18M3 16h18"/></symbol>
<symbol id="i-gate" viewBox="0 0 24 24"><path d="M3 21V6M21 21V6M3 6c3-3 15-3 18 0M7 9v12M12 8v13M17 9v12"/></symbol>
<symbol id="i-bolt" viewBox="0 0 24 24"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></symbol>
<symbol id="i-ruler" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="10" rx="1.5"/><path d="M6 7v4M10 7v3M14 7v4M18 7v3"/></symbol>
<symbol id="i-train" viewBox="0 0 24 24"><rect x="5" y="3" width="14" height="14" rx="3"/><path d="M5 11h14M9 21l-2-4M15 21l2-4"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></symbol>
<symbol id="i-file" viewBox="0 0 24 24"><path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></symbol>
<symbol id="i-users" viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/></symbol>
<symbol id="i-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></symbol>
<symbol id="i-sprout" viewBox="0 0 24 24"><path d="M12 21v-9"/><path d="M12 12C12 8 9 5 4 5c0 4 3 7 8 7z"/><path d="M12 14c0-4 3-7 8-7 0 4-3 7-8 7z"/></symbol>
<symbol id="i-rupee" viewBox="0 0 24 24"><path d="M6 4h12M6 9h12M9 4c6 0 6 10 0 10H6l8 7"/></symbol>
<symbol id="i-map" viewBox="0 0 24 24"><path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/></symbol>
<symbol id="i-key" viewBox="0 0 24 24"><circle cx="8" cy="15" r="4"/><path d="m11 12 9-9M17 6l2 2M15 8l2 2"/></symbol>
<symbol id="i-up" viewBox="0 0 24 24"><path d="M12 19V5M6 11l6-6 6 6"/></symbol>
<symbol id="i-zoom" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4M11 8v6M8 11h6"/></symbol>
<symbol id="i-ig" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></symbol>
<symbol id="i-fb" viewBox="0 0 24 24"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.5V10H7v4h2.5v8h4v-8h3l.5-4h-3.5V8.6c0-.4.2-.6.5-.6z"/></symbol>
<symbol id="i-li" viewBox="0 0 24 24"><rect x="3" y="9" width="4" height="12"/><circle cx="5" cy="5" r="2.2"/><path d="M10 9h3.8v1.7c.6-1 1.9-2 3.9-2 3.3 0 4.3 2 4.3 5.4V21h-4v-6.2c0-1.6-.4-2.7-1.9-2.7-1.6 0-2.1 1.2-2.1 2.8V21h-4z"/></symbol>
<symbol id="i-wa" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M3.6 20.4l1.2-4.1A8.6 8.6 0 1 1 8 19.3z"/><path fill="currentColor" stroke="none" d="M9.1 7.6c.2-.4.5-.5.8-.5h.6c.2 0 .4.1.5.4l.8 1.9c.1.2 0 .5-.1.6l-.6.8c-.1.1-.1.3 0 .5.6 1.1 1.6 2.1 2.7 2.7.2.1.4.1.5-.1l.7-.8c.2-.2.4-.2.6-.1l1.9.9c.2.1.3.3.3.5v.5c0 .4-.2.8-.6 1.1-.6.4-1.4.6-2.2.4-2.6-.6-4.9-2.9-5.6-5.4-.2-.9 0-1.6.5-2.3z"/></symbol>
</svg>"""


# ---------------------------------------------------------------- shared parts
def social_links():
    return (f'<div class="social">'
            f'<a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Vatika Estate on Facebook">{icon("fb")}</a>'
            f'<a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Vatika Estate on Instagram">{icon("ig")}</a>'
            f'<a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="Vatika Estate on LinkedIn">{icon("li")}</a>'
            f'</div>')


def nav_link(href, label, key, active):
    cur = ' aria-current="page"' if key == active else ""
    return f'<li><a href="{href}"{cur}>{label}</a></li>'


def header(active):
    completed_links = "".join(f'<li><a href="projects.html#{s}">{n}</a></li>' for s, n in COMPLETED)
    drawer_completed = "".join(f'<a href="projects.html#{s}">{n}</a>' for s, n in COMPLETED)
    proj_active = " is-active" if active in ("projects", "luxora") else ""
    return f"""
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="Vatika Estate — Home">
      <img src="assets/img/vatika-estate-logo.webp" width="360" height="334" alt="Vatika Estate logo">
    </a>
    <nav aria-label="Main navigation">
      <ul class="nav">
        {nav_link("index.html", "Home", "home", active)}
        {nav_link("about.html", "About Us", "about", active)}
        <li class="has-dropdown{proj_active}">
          <button type="button" data-dropdown-toggle aria-expanded="false" aria-haspopup="true">Projects {icon("chev", "chev")}</button>
          <div class="dropdown">
            <div>
              <p class="dropdown__title">Ongoing Project</p>
              <a class="dropdown__feature" href="vatika-luxora.html">
                {img("agricultural-land-kasara-vatika-luxora", "Vatika Luxora agricultural plots in Kasara", "260px")}
                <span>Vatika Luxora<small>Dhakane, Kasara · Ongoing project</small></span>
              </a>
            </div>
            <div>
              <p class="dropdown__title">Completed Projects</p>
              <ul class="dropdown__list">{completed_links}</ul>
              <div class="dropdown__all"><a class="link-arrow" href="projects.html">View all projects {icon("arrow")}</a></div>
            </div>
          </div>
        </li>
        {nav_link("gallery.html", "Gallery", "gallery", active)}
        {nav_link("contact.html", "Contact Us", "contact", active)}
      </ul>
    </nav>
    <div class="header-actions">
      <a class="btn btn--outline header-call" href="tel:{PHONE_TEL}" aria-label="Call Vatika Estate">{icon("phone")} Call Us</a>
      <button class="btn btn--primary" type="button" data-enquire="enquiry">Enquire Now {icon("arrow", "icon--arrow")}</button>
      <button class="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-drawer">{icon("menu")}</button>
    </div>
  </div>
</header>

<div class="drawer" id="mobile-drawer" aria-hidden="true" aria-label="Mobile menu">
  <div class="drawer__head">
    <a href="index.html"><img src="assets/img/vatika-estate-logo.webp" width="360" height="334" alt="Vatika Estate logo"></a>
    <button class="drawer__close" type="button" aria-label="Close menu">{icon("close")}</button>
  </div>
  <ul class="drawer__nav">
    {nav_link("index.html", "Home", "home", active)}
    {nav_link("about.html", "About Us", "about", active)}
    <li>
      <button type="button" data-sub-toggle aria-expanded="false">Projects {icon("chev", "chev")}</button>
      <div class="drawer__sub"><div>
        <p>Ongoing</p>
        <a href="vatika-luxora.html">Vatika Luxora</a>
        <p>Completed</p>
        {drawer_completed}
        <a href="projects.html"><strong>View all projects →</strong></a>
      </div></div>
    </li>
    {nav_link("gallery.html", "Gallery", "gallery", active)}
    {nav_link("contact.html", "Contact Us", "contact", active)}
  </ul>
  <div class="drawer__cta">
    <button class="btn btn--primary btn--block" type="button" data-enquire="enquiry">Enquire Now {icon("arrow", "icon--arrow")}</button>
  </div>
</div>
<div class="drawer-overlay"></div>
"""


def lead_form(prefix, default_type="Enquiry", in_modal=True, submit_label="Submit Enquiry"):
    date_attr = "data-visit-only" if in_modal else ""
    date_label = "Preferred visit date" if in_modal else "Preferred visit date (optional)"
    msg_rows = "3" if in_modal else "4"
    return f"""
<form class="lead-form" data-lead-form novalidate>
  <input type="hidden" name="form_type" value="{default_type}">
  <div class="hp" aria-hidden="true"><label>Leave this empty<input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>
  <div class="form-grid">
    <div class="field full field--name">
      <label for="{prefix}-name">Full name <span class="req">*</span></label>
      <input id="{prefix}-name" name="name" type="text" autocomplete="name" placeholder="Your full name" required>
      <span class="field__error" role="alert"></span>
    </div>
    <div class="field">
      <label for="{prefix}-phone">Mobile number <span class="req">*</span></label>
      <div class="phone-input"><span>+91</span><input id="{prefix}-phone" name="phone" type="tel" inputmode="numeric" autocomplete="tel-national" placeholder="10-digit mobile" maxlength="14" required></div>
      <span class="field__error" role="alert"></span>
    </div>
    <div class="field optional-field">
      <label for="{prefix}-email">Email</label>
      <input id="{prefix}-email" name="email" type="email" autocomplete="email" placeholder="you@example.com">
      <span class="field__error" role="alert"></span>
    </div>
    <div class="field full optional-field field--project">
      <label for="{prefix}-project">Interested in</label>
      <select id="{prefix}-project" name="project">
        <option value="{LUXORA}">Vatika Luxora (Ongoing)</option>
        <option value="Completed project (resale / information)">Completed projects</option>
        <option value="General enquiry">General enquiry</option>
      </select>
    </div>
    <div class="field full" {date_attr}>
      <label for="{prefix}-date">{date_label}</label>
      <input id="{prefix}-date" name="preferred_date" type="date">
      <span class="field__error" role="alert"></span>
    </div>
    <div class="field full optional-field">
      <label for="{prefix}-message">Message</label>
      <textarea id="{prefix}-message" name="message" rows="{msg_rows}" placeholder="Plot size, budget or any questions (optional)"></textarea>
    </div>
    <label class="check full optional-field">
      <input type="checkbox" name="consent" required checked>
      <span>I agree to be contacted by Vatika Estate via call, SMS, email or WhatsApp. See our <a href="privacy-policy.html" target="_blank">Privacy Policy</a>.</span>
    </label>
  </div>
  <button class="btn btn--primary btn--block" type="submit" style="margin-top:18px"><span class="btn__label">{submit_label}</span></button>
  <div class="form-alert form-alert--error" role="alert"></div>
  <p class="form-note">{icon("shield")} Your details are safe with us. No spam.</p>
  <p class="consent-mini">By submitting, you agree to be contacted as per our <a href="privacy-policy.html" target="_blank">Privacy Policy</a>.</p>
</form>
<div class="form-success" role="status" aria-live="polite">
  <div class="form-success__icon">{icon("check")}</div>
  <h3>Thank you, <span data-lead-name></span>!</h3>
  <p>We've received your details. A Vatika Estate land advisor will call you shortly. Your brochure is ready to download.</p>
  <div class="btn-row">
    <button class="btn btn--primary" type="button" data-brochure-download>{icon("download")} Download Brochure</button>
    <a class="btn btn--wa" href="{WA_LINK}" target="_blank" rel="noopener">{icon("wa")} WhatsApp Us</a>
  </div>
</div>"""


def modal():
    return f"""
<div class="modal" id="lead-modal" aria-hidden="true" data-mode="enquiry">
  <div class="modal__backdrop" data-modal-close></div>
  <div class="modal__dialog" role="dialog" aria-modal="true" aria-labelledby="lead-modal-title">
    <button class="modal__close" type="button" data-modal-close aria-label="Close form">{icon("close")}</button>
    <aside class="modal__aside">
      {img("aerial-view-farmhouse-plots-vatika", "", "360px")}
      <span class="pill pill--live">Ongoing project</span>
      <h3>Vatika Luxora, Kasara</h3>
      <ul>
        <li>{icon("check")} 22 acres of premium farmland</li>
        <li>{icon("check")} 71 plots of 11 guntas each</li>
        <li>{icon("check")} Farming licence included</li>
        <li>{icon("check")} 12 km from Kasara station</li>
      </ul>
    </aside>
    <div class="modal__main">
      <h2 id="lead-modal-title" data-hide-on-success>Enquire Now</h2>
      <p id="lead-modal-text" data-hide-on-success>Share your details and our land advisor will call you back shortly.</p>
      {lead_form("m")}
    </div>
  </div>
</div>"""


def footer():
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html"><img src="assets/img/vatika-estate-logo-light.webp" width="360" height="334" alt="Vatika Estate" loading="lazy"></a>
        <p>Vatika Estate is a real estate company focused on agricultural land for sale in Shahapur &amp; Kasara — peaceful locations with good connectivity, natural surroundings and strong investment potential.</p>
        {social_links()}
      </div>
      <div>
        <h3>Quick Links</h3>
        <ul class="footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About Us</a></li>
          <li><a href="projects.html">Projects</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="contact.html">Contact Us</a></li>
          <li><a href="privacy-policy.html">Privacy Policy</a></li>
        </ul>
      </div>
      <div>
        <h3>Our Projects</h3>
        <ul class="footer-links">
          <li><a href="vatika-luxora.html">Vatika Luxora (Ongoing)</a></li>
          <li><a href="projects.html#vatika-farm">Vatika Farm</a></li>
          <li><a href="projects.html#vatika-hills">Vatika Hills</a></li>
          <li><a href="projects.html#vatika-greens">Vatika Greens</a></li>
          <li><a href="projects.html#gokul-vatika">Gokul Vatika</a></li>
          <li><a href="projects.html#completed">All completed projects</a></li>
        </ul>
      </div>
      <div>
        <h3>Get In Touch</h3>
        <ul class="footer-contact">
          <li>{icon("pin")}<span>{ADDRESS}</span></li>
          <li>{icon("phone")}<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li>{icon("wa")}<a href="{WA_LINK}" target="_blank" rel="noopener">WhatsApp: {PHONE_DISPLAY}</a></li>
          <li>{icon("mail")}<span><a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a><br><a href="mailto:{EMAIL_SALES}">{EMAIL_SALES}</a></span></li>
        </ul>
      </div>
    </div>
    <p class="footer-disclaimer">Disclaimer: Images shown are for representational purposes only. Prices, plot availability and specifications are subject to change without notice. This website does not constitute an offer or contract.</p>
  </div>
  <div class="footer-bottom">
    <div class="container">
      <p>Copyright © 2026 Vatika Estate, All rights reserved.</p>
      <p>Marketed By: <strong>Indo Asian Buildcon Private Limited</strong></p>
      <div class="footer-legal">
        <a href="privacy-policy.html">Privacy Policy</a>
        <a href="terms.html">Terms of Service</a>
        <a href="privacy-policy.html#cookies">Cookies</a>
      </div>
    </div>
  </div>
</footer>

<div class="float-actions">
  <a class="float-btn float-call" href="tel:{PHONE_TEL}" aria-label="Call Vatika Estate">{icon("phone")}</a>
  <a class="float-btn float-wa" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{icon("wa")}<span class="float-wa__tip">Chat on WhatsApp</span></a>
</div>
<button class="to-top" type="button" aria-label="Back to top">{icon("up")}</button>

<div class="lightbox" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Image viewer">
  <span class="lightbox__count"></span>
  <button class="lightbox__btn lightbox__close" type="button" aria-label="Close">{icon("close")}</button>
  <button class="lightbox__btn lightbox__prev" type="button" aria-label="Previous image">{icon("arrow-left")}</button>
  <figure><img src="data:image/gif;base64,R0lGODlhAQABAAAAACw=" alt=""><figcaption></figcaption></figure>
  <button class="lightbox__btn lightbox__next" type="button" aria-label="Next image">{icon("arrow")}</button>
</div>
"""


ORG_LD = {
    "@context": "https://schema.org",
    "@type": "RealEstateAgent",
    "name": "Vatika Estate",
    "url": SITE_URL + "/",
    "logo": SITE_URL + "/assets/img/favicon-512.png",
    "image": SITE_URL + "/assets/img/vatika-estate-og-image.jpg",
    "description": "Premium agricultural land and farm plots for sale in Shahapur & Kasara, Maharashtra.",
    "telephone": PHONE_TEL,
    "email": EMAIL_INFO,
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Office No. 1203, 12th Floor, Centrum IT Park, Plot No. C-8, Wagle Estate Road",
        "addressLocality": "Thane West",
        "addressRegion": "Maharashtra",
        "addressCountry": "IN",
    },
    "areaServed": ["Shahapur", "Kasara", "Thane", "Mumbai"],
    "sameAs": [FACEBOOK, INSTAGRAM, LINKEDIN],
}


def asset_version(rel):
    """Short content hash so browsers always fetch the latest CSS/JS after a rebuild."""
    import hashlib
    with open(os.path.join(ROOT, rel), "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()[:8]


def page(filename, title, description, active, body, ld=None, no_popup=False, hero_preload=None, base=None):
    canonical = SITE_URL + "/" + ("" if filename == "index.html" else filename)
    lds = [ORG_LD] + (ld or [])
    ld_html = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    preload = (f'<link rel="preload" as="image" href="assets/img/{hero_preload}.webp" '
               f'imagesrcset="assets/img/{hero_preload}-sm.webp 560w, assets/img/{hero_preload}.webp 1200w" imagesizes="(max-width: 1024px) 100vw, 50vw">') if hero_preload else ""
    base_tag = f'<base href="{base}">' if base else ""
    np = " data-no-popup" if no_popup else ""
    robots = "noindex, follow" if filename == "404.html" else "index, follow, max-image-preview:large"
    html = f"""<!doctype html>
<html lang="en-IN" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{base_tag}
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#102a1c">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Vatika Estate">
<meta property="og:locale" content="en_IN">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/img/vatika-estate-og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE_URL}/assets/img/vatika-estate-og-image.jpg">
<link rel="icon" type="image/png" sizes="48x48" href="assets/img/favicon-48.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={asset_version("assets/css/style.css")}">
{preload}
{ld_html}
</head>
<body{np}>
{SPRITE}
{header(active)}
<main id="main">
{body}
</main>
{footer()}
{modal()}
<script src="assets/js/main.js?v={asset_version("assets/js/main.js")}" defer></script>
</body>
</html>
"""
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("built", filename)


def page_hero(title, text, crumb, image, alt):
    return f"""
<section class="page-hero">
  <div class="page-hero__bg">{img(image, alt, "100vw", eager=True)}</div>
  <div class="container">
    <h1>{title}</h1>
    <p>{text}</p>
  </div>
</section>"""


def breadcrumb_ld(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE_URL + "/" + u}
            for i, (n, u) in enumerate(items)
        ],
    }


# ---------------------------------------------------------------- reusable sections
FEATURES = [
    ("sun", "Peaceful Location", "Enjoy a calm and serene environment away from city life."),
    ("road", "Road Connectivity", "Convenient access to major roads and nearby locations."),
    ("water", "Water Availability", "Reliable water access for agricultural and land-use needs."),
    ("tree", "Natural Surroundings", "Experience the beauty of greenery and nature."),
    ("shield", "Legally Verified Plot", "Transparent and properly verified property documentation."),
    ("trend", "Investment Potential", "A valuable opportunity for long-term land investment."),
]


def features_grid():
    cards = "".join(
        f'<article class="feature reveal reveal-delay-{i % 3}"><div class="feature__icon">{icon(ic)}</div><h3>{t}</h3><p>{d}</p></article>'
        for i, (ic, t, d) in enumerate(FEATURES))
    return f'<div class="features">{cards}</div>'


def completed_grid(dark=False):
    cards = "".join(f"""
<article class="project-card reveal" id="{s}">
  <div class="project-card__icon">{icon("leaf")}</div>
  <span class="pill pill--done">{icon("check")} Completed</span>
  <h3>{n}</h3>
</article>""" for s, n in COMPLETED)
    return f'<div class="project-grid">{cards}</div>'


def luxora_card():
    return f"""
<article class="project-hero reveal">
  <div class="project-hero__media">
    {img("agricultural-land-kasara-vatika-luxora", "Green agricultural land at Vatika Luxora, Kasara", "(max-width: 1024px) 100vw, 55vw")}
  </div>
  <div class="project-hero__body">
    <span class="pill pill--live" style="align-self:flex-start;margin-bottom:14px">Ongoing Project</span>
    <h3 class="h-lg">Vatika Luxora</h3>
    <p class="project-hero__loc">{icon("pin")} Village Dhakane, Taluka Shahapur, District Thane (near Kasara)</p>
    <div class="specs">
      <div class="spec">{icon("map")}<div><strong>22 Acres</strong><span>Premium farmland</span></div></div>
      <div class="spec">{icon("ruler")}<div><strong>71 Plots</strong><span>11 guntas each</span></div></div>
      <div class="spec">{icon("file")}<div><strong>Farming Licence</strong><span>Included for owners</span></div></div>
      <div class="spec">{icon("train")}<div><strong>12 km</strong><span>From Kasara station</span></div></div>
    </div>
    <div class="btn-row">
      <a class="btn btn--dark" href="vatika-luxora.html">View Details {icon("arrow", "icon--arrow")}</a>
      <button class="btn btn--outline" type="button" data-enquire="brochure" data-project="{LUXORA}">{icon("download")} Get Brochure</button>
    </div>
  </div>
</article>"""


def cta_band():
    return f"""
<section class="section--tight" style="padding-top:0;padding-bottom:100px">
  <div class="container">
    <div class="cta-band reveal">
      <div class="cta-band__body">
        <span class="eyebrow">{icon("file")} Brochure</span>
        <h2 class="h-lg">Get the Vatika Luxora brochure</h2>
        <p>Share your details to receive the complete Vatika Luxora project brochure.</p>
        <div class="btn-row">
          <button class="btn btn--gold" type="button" data-enquire="brochure" data-project="{LUXORA}">{icon("download")} Get Brochure</button>
          <a class="btn btn--outline-light" href="tel:{PHONE_TEL}">{icon("phone")} Call Us</a>
        </div>
      </div>
      <div class="cta-band__media">{img("second-home-farmhouse-garden-vatika", "Farmhouse with garden on agricultural land", "(max-width: 1024px) 100vw, 40vw")}</div>
    </div>
  </div>
</section>"""


# ================================================================= PAGES
def build_home():
    # Hero slides — wording taken from the original website's three hero slides.
    slides = [
        ("Own Your Piece of <em>Nature</em>",
         "Discover premium agricultural land in peaceful locations—perfect for investment, farming, and a nature-connected lifestyle.",
         "aerial-view-farmhouse-plots-vatika", "Aerial view of farmhouse plots with garden and pond"),
        ("Invest in Agricultural Land. <em>Invest in Your Future.</em>",
         "Explore carefully selected agricultural land with natural surroundings, peaceful locations, and long-term growth potential.",
         "orchard-pathway-farmhouse-kasara", "Orchard pathway leading to a farmhouse near Kasara"),
        ("Find Your Perfect Land in <em>Shahapur</em>",
         "Own beautiful agricultural land surrounded by nature and enjoy the perfect blend of peaceful living and smart investment.",
         "fruit-orchard-agricultural-land-shahapur", "Fruit orchard on agricultural land in Shahapur"),
    ]
    slide_html = ""
    for i, (t, p, _, _) in enumerate(slides):
        tag = "h1" if i == 0 else "p"
        cls = "is-active" if i == 0 else ""
        slide_html += f"""
        <div class="hero__slide {cls}">
          <span class="eyebrow">{icon("leaf")} Vatika Estate</span>
          <{tag} class="hero__title">{t}</{tag}>
          <p class="hero__text">{p}</p>
          <div class="btn-row">
            <button class="btn btn--primary" type="button" data-enquire="enquiry">Enquire Now {icon("arrow", "icon--arrow")}</button>
            <a class="btn btn--outline" href="projects.html">View Projects</a>
          </div>
        </div>"""
    imgs_html = "".join(
        img(n, a, "(max-width: 1024px) 100vw, 46vw", cls="is-active" if i == 0 else "", eager=(i == 0))
        for i, (_, _, n, a) in enumerate(slides))

    amenities = [
        ("sun", "Peaceful natural environment", "sunrise-farmland-shahapur", "Sunrise over farmland in Shahapur"),
        ("road", "Convenient road connectivity", "aerial-view-farmhouse-plots-vatika", "Internal roads between farmhouse plots"),
        ("water", "Water availability", "rice-crop-fertile-soil-kasara", "Healthy rice crop on fertile soil in Kasara"),
        ("shield", "Clear & Verified Plots", "vatika-luxora-plot-layout-plan", "Vatika Luxora plot layout plan"),
        ("sprout", "Suitable for agricultural use", "green-paddy-fields-agricultural-land", "Green paddy fields on agricultural land"),
        ("trend", "Excellent long-term potential", "farmland-sunset-view-shahapur", "Sunset view over farmland in Shahapur"),
    ]
    amen_html = "".join(f"""
      <article class="amenity">
        <div class="amenity__img">{img(n, a, "(max-width: 680px) 82vw, (max-width: 1180px) 33vw, 25vw")}</div>
        <div class="amenity__body"><span class="amenity__icon">{icon(ic)}</span><h3>{t}</h3></div>
      </article>""" for ic, t, n, a in amenities)

    body = f"""
<section class="hero" data-hero aria-roledescription="carousel" aria-label="Highlights">
  <div class="container">
    <div class="hero__grid">
      <div>
        <div class="hero__slides">{slide_html}</div>
        <div class="hero__controls">
          <button class="round-btn" type="button" data-hero-prev aria-label="Previous slide">{icon("arrow-left")}</button>
          <div class="hero__dots"></div>
          <button class="round-btn" type="button" data-hero-next aria-label="Next slide">{icon("arrow")}</button>
        </div>
      </div>
      <div class="hero__visual">
        <div class="hero__frame">{imgs_html}</div>
      </div>
    </div>
  </div>
</section>

<section class="stats" aria-label="Vatika Estate in numbers">
  <div class="container">
    <div class="stats__grid stats__grid--3">
      <div class="stat"><strong><span data-count="16.55">16.55</span> Lacs<sup>+</sup></strong><span>Sq.ft sale</span></div>
      <div class="stat"><strong><span data-count="1">1</span><sup>+</sup></strong><span>Onboard Project</span></div>
      <div class="stat"><strong><span data-count="100">100</span><sup>+</sup></strong><span>Satisfied customers</span></div>
    </div>
  </div>
</section>

<section class="section" id="about-sec">
  <div class="container split">
    <div class="about-media reveal">
      <figure>{img("farmhouse-plot-shahapur-vatika-estate", "Farmhouse plot with fruit trees in Shahapur", "(max-width: 1024px) 55vw, 30vw")}</figure>
      <figure>{img("weekend-home-kasara-hills", "Weekend home in the misty hills near Kasara", "(max-width: 1024px) 40vw, 22vw")}</figure>
    </div>
    <div class="reveal reveal-delay-1">
      <h2 class="h-lg">About Us</h2>
      <p class="lead">Vatika Estate offers premium agricultural land in Shahapur &amp; Kasara for those looking to invest in nature and secure their future. We provide carefully selected land options with clear documentation, peaceful surroundings, and excellent long-term investment potential.</p>
      <div class="btn-row" style="margin-top:28px">
        <a class="btn btn--dark" href="about.html">Learn More {icon("arrow", "icon--arrow")}</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="featured">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>
        <span class="eyebrow">{icon("home")} Projects</span>
        <h2 class="h-lg">Discover Modern Living At Vatika Estate.</h2>
        <p>Where nature, fresh surroundings, and your own agriculture plot come together. A perfect escape from the city, designed for relaxation, family time, and a better tomorrow.</p>
      </div>
      <a class="btn btn--outline" href="projects.html">All Properties {icon("arrow", "icon--arrow")}</a>
    </div>
    {luxora_card()}
  </div>
</section>

<section class="section section--sand">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>
        <span class="eyebrow">{icon("sprout")} Agricultural Land</span>
        <h2 class="h-lg">Project Highlights</h2>
        <p>Experience the beauty of nature with carefully selected agricultural land in Shahapur. Our land opportunities are suitable for farming, investment, and buyers looking for a peaceful space away from the city.</p>
      </div>
      <div class="carousel__nav" data-carousel>
        <button class="round-btn" type="button" data-carousel-prev aria-label="Previous highlights">{icon("arrow-left")}</button>
        <button class="round-btn" type="button" data-carousel-next aria-label="Next highlights">{icon("arrow")}</button>
      </div>
    </div>
    <div class="carousel"><div class="carousel__track">{amen_html}</div></div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <div class="media-card">
        {img("homestead-farmhouse-vegetable-garden", "Homestead farmhouse with a vegetable garden", "(max-width: 1024px) 100vw, 50vw")}
      </div>
    </div>
    <div class="reveal reveal-delay-1">
      <span class="eyebrow">{icon("trend")} Investment</span>
      <h2 class="h-lg">Why Invest in Agricultural Land?</h2>
      <p class="lead">Agricultural land offers an opportunity to own a valuable piece of nature while creating possibilities for farming, leisure, and long-term investment. Shahapur &amp; Kasara natural surroundings and connectivity make it an attractive destination for land buyers.</p>
      <div class="btn-row" style="margin-top:28px">
        <button class="btn btn--primary" type="button" data-enquire="visit" data-project="{LUXORA}">{icon("calendar")} Request A Visit</button>
      </div>
    </div>
  </div>
</section>

<section class="section section--dark" id="completed">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>
        <h2 class="h-lg">Our Completed Projects</h2>
      </div>
      <a class="btn btn--outline-light" href="projects.html">View All Projects {icon("arrow", "icon--arrow")}</a>
    </div>
    {completed_grid(dark=True)}
  </div>
</section>

<section class="section">
  <div class="container split split--reverse">
    <div class="reveal">
      <div class="media-card" style="aspect-ratio:4/3.6">
        {img("land-buying-consultation-vatika-estate", "Family consulting a Vatika Estate land advisor", "(max-width: 1024px) 100vw, 50vw")}
      </div>
    </div>
    <div class="reveal reveal-delay-1">
      <span class="eyebrow">{icon("users")} Consulting</span>
      <h2 class="h-lg">Selling Plot We Make It Simple</h2>
      <p class="lead">At Vatika Estate, we help you find the perfect plot for your dream second home. Enjoy peaceful surroundings, natural beauty, and the opportunity to own a valuable piece of land away from the city. Your space to relax, reconnect, and build your future starts here.</p>
      <div class="btn-row" style="margin-top:28px">
        <button class="btn btn--primary" type="button" data-enquire="enquiry">Get Started {icon("arrow", "icon--arrow")}</button>
      </div>
    </div>
  </div>
</section>
{cta_band()}
"""
    page("index.html", "Vatika Estate | Agricultural Land in Shahapur & Kasara",
         "Vatika Estate offers premium agricultural land in Shahapur & Kasara — peaceful locations, road connectivity, water availability and legally verified plots with clear documentation.",
         "home", body, hero_preload="aerial-view-farmhouse-plots-vatika")


def build_about():
    why = [
        ("sun", "Peaceful Location", "Enjoy a calm and serene environment away from city life.", "fruit-orchard-agricultural-land-shahapur", "Orchard with farmhouse in Shahapur"),
        ("road", "Road Connectivity", "Convenient access to major roads and nearby locations.", "homestead-farmhouse-vegetable-garden", "Homestead farmhouse with garden"),
        ("water", "Water Availability", "Reliable water access for agricultural and land-use needs.", "aerial-view-farmhouse-plots-vatika", "Aerial view of farmhouse plots"),
        ("tree", "Natural Surroundings", "Experience the beauty of greenery and nature.", "orchard-pathway-farmhouse-kasara", "Orchard pathway near Kasara"),
        ("file", "Clear Documentation", "Transparent and properly verified property documentation.", "farmhouse-plot-shahapur-vatika-estate", "Farmhouse plot in Shahapur"),
        ("trend", "Investment Potential", "A valuable opportunity for long-term land investment.", "organic-farming-plot-kasara", "Organic farming plot near Kasara"),
    ]
    cards = "".join(f"""
      <article class="img-card reveal reveal-delay-{i % 4}">
        <div class="img-card__img">{img(n, a, "(max-width: 680px) 100vw, (max-width: 1024px) 50vw, 25vw")}</div>
        <div class="img-card__body"><h3>{icon(ic)} {t}</h3><p>{d}</p></div>
      </article>""" for i, (ic, t, d, n, a) in enumerate(why))
    body = page_hero("About Vatika Estate",
                     "Premium agricultural land opportunities in Shahapur &amp; Kasara.",
                     '<li aria-current="page">About Us</li>', "sunrise-farmland-shahapur", "Sunrise over farmland in Shahapur") + f"""
<section class="section">
  <div class="container split">
    <div class="about-media reveal">
      <figure>{img("second-home-farmhouse-garden-vatika", "Second home farmhouse with garden", "(max-width: 1024px) 55vw, 30vw")}</figure>
      <figure>{img("farmhouse-kitchen-garden-vatika-estate", "Farmhouse kitchen garden", "(max-width: 1024px) 40vw, 22vw")}</figure>
    </div>
    <div class="reveal reveal-delay-1">
      <h2 class="h-lg">Who We Are</h2>
      <p class="lead">Vatika Estate is a real estate company focused on agricultural land for sale, helping buyers find peaceful locations with good connectivity, natural surroundings and strong investment potential.</p>
      <p>Vatika Estate offers premium agricultural land in Shahapur &amp; Kasara for those looking to invest in nature and secure their future. We provide carefully selected land options with clear documentation, peaceful surroundings, and excellent long-term investment potential.</p>
      <div class="btn-row" style="margin-top:26px">
        <a class="btn btn--dark" href="contact.html">Contact Us {icon("arrow", "icon--arrow")}</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="mv-grid">
      <article class="mv-card reveal">
        <div class="mv-card__img">{img("green-paddy-fields-agricultural-land", "Green paddy fields", "(max-width: 680px) 100vw, 25vw")}</div>
        <div class="mv-card__body">
          <div class="feature__icon">{icon("sprout")}</div>
          <h2 class="h-md">Our Mission</h2>
          <p>To provide suitable agricultural land opportunities and make land ownership a simple, transparent and confident experience.</p>
        </div>
      </article>
      <article class="mv-card reveal reveal-delay-1">
        <div class="mv-card__img">{img("weekend-home-kasara-hills", "Weekend home in the hills near Kasara", "(max-width: 680px) 100vw, 25vw")}</div>
        <div class="mv-card__body">
          <div class="feature__icon">{icon("sun")}</div>
          <h2 class="h-md">Our Vision</h2>
          <p>To become a trusted name for agricultural land buyers by connecting people with valuable land and nature-focused opportunities.</p>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>
        <h2 class="h-lg">Why Choose Us?</h2>
        <p>At Vatika Estate, we help you find the right agricultural land with clear guidance, trusted support and a simple buying experience.</p>
      </div>
      <button class="btn btn--primary" type="button" data-enquire="visit" data-project="{LUXORA}">{icon("calendar")} Request A Visit</button>
    </div>
    <div class="img-cards">{cards}</div>
  </div>
</section>

{cta_band()}"""
    page("about.html", "About Us | Vatika Estate — Agricultural Land Experts in Thane",
         "Learn about Vatika Estate — 16.55 lakh+ sq.ft sold and 100+ satisfied customers. Our mission: simple, transparent agricultural land ownership in Shahapur & Kasara.",
         "about", body, ld=[breadcrumb_ld([("Home", ""), ("About Us", "about.html")])])


def build_projects():
    body = page_hero("Our Projects",
                     "From our ongoing Vatika Luxora project near Kasara to eight successfully completed developments across the Shahapur belt.",
                     '<li aria-current="page">Projects</li>', "aerial-view-farmhouse-plots-vatika", "Aerial view of Vatika farmhouse plots") + f"""
<section class="section" id="ongoing">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">{icon("home")} Ongoing Project</span>
      <h2 class="h-lg">Vatika Luxora</h2>
      <p>22 acres of premium farmland with 71 individually demarcated plots, a luxury entrance gate, wire fencing and 40 ft internal roads.</p>
    </div>
    {luxora_card()}
  </div>
</section>

<section class="section section--white" id="completed">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>
        <span class="eyebrow">{icon("check")} Completed Projects</span>
        <h2 class="h-lg">Delivered with trust</h2>
      </div>
      <button class="btn btn--primary" type="button" data-enquire="enquiry" data-project="Completed project (resale / information)">Enquire Now {icon("arrow", "icon--arrow")}</button>
    </div>
    {completed_grid()}
  </div>
</section>
{cta_band()}"""
    page("projects.html", "Projects | Vatika Luxora & Completed Projects — Vatika Estate",
         "Explore Vatika Estate projects: Vatika Luxora (ongoing, Kasara) plus completed projects Vatika Farm, Vatika Hills, Vatika Greens, Vatika Aangan, Gokul Vatika, Vatika Estate and Vatika Roots.",
         "projects", body, ld=[breadcrumb_ld([("Home", ""), ("Projects", "projects.html")])])


def build_luxora():
    highlights = [
        ("pin", "Village Dhakane", "Taluka Shahapur, District Thane"),
        ("map", "22 acres of premium farmland", "Spacious, well-planned layout"),
        ("ruler", "71 well-planned plots", "Each plot of 11 guntas"),
        ("file", "Farming licence included", "For all plot owners"),
        ("gate", "Luxury entrance gate", "A grand arrival experience"),
        ("fence", "Complete wire fencing", "Around the entire 22-acre project"),
        ("road", "12 m (40 ft) murrum internal roads", "Smooth access to every plot"),
        ("shield", "Individual plot demarcation", "Clear ownership boundaries"),
        ("bolt", "Common electricity & water supply", "Within the project"),
    ]
    hl = "".join(f'<div class="highlight"><div class="feature__icon">{icon(ic)}</div><div><strong>{t}</strong><span>{d}</span></div></div>'
                 for ic, t, d in highlights)
    gal = ["agricultural-land-kasara-vatika-luxora", "rice-crop-fertile-soil-kasara", "farmland-sunset-view-shahapur", "green-paddy-fields-agricultural-land"]
    gal_alts = ["Agricultural land at Vatika Luxora", "Fertile rice crop near Kasara", "Sunset over farmland", "Green paddy fields"]
    gal_html = "".join(f'<a href="assets/img/{n}.webp" data-lightbox="luxora" data-caption="{a}">{img(n, a, "(max-width: 680px) 50vw, 200px")}</a>'
                       for n, a in zip(gal, gal_alts))
    body = page_hero("Vatika Luxora",
                     "Agriculture plots at Village Dhakane, Taluka Shahapur, near Kasara — 22 acres, 71 plots, farming licence included.",
                     '<li><a href="projects.html">Projects</a></li><li aria-current="page">Vatika Luxora</li>',
                     "agricultural-land-kasara-vatika-luxora", "Vatika Luxora farmland in Kasara") + f"""
<section class="section">
  <div class="container detail-grid">
    <div class="prose">
      <h2>Why invest in Kasara?</h2>
      <p>Kasara is one of the fastest-growing investment destinations on the Mumbai–Nashik belt, offering the perfect blend of nature, connectivity and long-term value. Strategically located on the Central Railway line and the Mumbai–Nashik Expressway (NH3), Kasara provides seamless access to Mumbai, Thane, Kalyan and Nashik — making weekend travel effortless and convenient.</p>
      <p>Surrounded by lush greenery, mountains, waterfalls and scenic views, Kasara offers a serene, pollution-free lifestyle that is ideal for farmhouses, weekend homes and eco-retreats. Its fertile soil and pleasant climate also make it suitable for organic farming, fruit plantations and sustainable agriculture.</p>
      <p>With major infrastructure upgrades, improving connectivity and rising tourism in the Kasara–Igatpuri region, land prices are steadily appreciating — making this the right time to invest at an attractive entry point. Investors benefit from both lifestyle value and strong long-term growth.</p>
      <p>Kasara offers the rare combination of affordability, natural beauty and future potential — an excellent choice for investors, nature lovers and families looking for a peaceful escape just a short drive from Mumbai.</p>

      <h3>Project highlights</h3>
      <div class="highlight-list">{hl}</div>

      <h3>Connectivity</h3>
      <div class="connect-list">
        <div class="connect">{icon("road")}<strong>11 km</strong>from the Mumbai–Nashik Highway</div>
        <div class="connect">{icon("train")}<strong>12 km</strong>from Kasara Railway Station</div>
        <div class="connect">{icon("pin")}<strong>89 km</strong>from Thane</div>
      </div>

      <h3>Pricing</h3>
      <p>Affordable price: only <strong>₹299 per sq.ft</strong> — ideal for farmhouses, organic farming and long-term investment.</p>

      <h3>Layout plan</h3>
      <a class="layout-plan" href="assets/img/vatika-luxora-plot-layout-plan.webp" data-lightbox="layout" data-caption="Vatika Luxora — plot layout plan">
        {img("vatika-luxora-plot-layout-plan", "Vatika Luxora plot layout plan showing 71 plots", "(max-width: 1024px) 100vw, 760px")}
        <span>{icon("zoom")} Click to enlarge</span>
      </a>

      <h3>Gallery</h3>
      <div class="mini-gallery">{gal_html}</div>

    </div>

    <aside>
      <div class="sticky-card">
        <div class="sticky-card__head" data-hide-on-success>
          <h2>Interested in Vatika Luxora?</h2>
          <p>Share your details to get the brochure and a call back.</p>
        </div>
        <div class="sticky-card__body">
          {lead_form("lux", "Vatika Luxora Enquiry", in_modal=False, submit_label="Get Brochure").replace('value="' + LUXORA + '">', 'value="' + LUXORA + '" selected>')}
        </div>
      </div>
    </aside>
  </div>
</section>"""
    ld = [breadcrumb_ld([("Home", ""), ("Projects", "projects.html"), ("Vatika Luxora", "vatika-luxora.html")]), {
        "@context": "https://schema.org",
        "@type": "Place",
        "name": "Vatika Luxora",
        "description": "22-acre agricultural land project with 71 plots of 11 guntas each at Village Dhakane, Taluka Shahapur, District Thane, near Kasara.",
        "address": {"@type": "PostalAddress", "addressLocality": "Dhakane, Shahapur", "addressRegion": "Maharashtra", "addressCountry": "IN"},
        "image": SITE_URL + "/assets/img/agricultural-land-kasara-vatika-luxora.webp",
    }]
    page("vatika-luxora.html", "Vatika Luxora | Agriculture Plots near Kasara — Vatika Estate",
         "Vatika Luxora: 22 acres, 71 agricultural plots of 11 guntas at Dhakane, Shahapur near Kasara. Farming licence, fencing, 40 ft roads, water & electricity.",
         "luxora", body, ld=ld)


def build_gallery():
    items = [
        ("aerial-view-farmhouse-plots-vatika", "Aerial view of farmhouse plots", "farmhouse"),
        ("agricultural-land-kasara-vatika-luxora", "Agricultural land at Vatika Luxora", "project farmland"),
        ("fruit-orchard-agricultural-land-shahapur", "Fruit orchard in Shahapur", "farmland"),
        ("vatika-luxora-plot-layout-plan", "Vatika Luxora layout plan", "project"),
        ("weekend-home-kasara-hills", "Weekend home in the Kasara hills", "farmhouse"),
        ("sunrise-farmland-shahapur", "Sunrise over farmland", "farmland"),
        ("second-home-farmhouse-garden-vatika", "Second-home farmhouse garden", "farmhouse"),
        ("rice-crop-fertile-soil-kasara", "Rice crop on fertile soil", "farmland project"),
        ("homestead-farmhouse-vegetable-garden", "Homestead with vegetable garden", "farmhouse"),
        ("green-paddy-fields-agricultural-land", "Green paddy fields", "farmland project"),
        ("orchard-pathway-farmhouse-kasara", "Orchard pathway to a farmhouse", "farmhouse"),
        ("farmland-sunset-view-shahapur", "Sunset view over farmland", "farmland project"),
        ("organic-farming-plot-kasara", "Organic farming plot", "farmland"),
        ("farmhouse-plot-shahapur-vatika-estate", "Farmhouse plot with fruit trees", "farmhouse"),
        ("farmhouse-kitchen-garden-vatika-estate", "Farmhouse kitchen garden", "farmhouse"),
        ("land-buying-consultation-vatika-estate", "Consultation with a land advisor", "lifestyle"),
    ]
    g = "".join(f'<a class="gallery__item reveal" href="assets/img/{n}.webp" data-lightbox="gallery" data-caption="{c}" data-cat="{cat}"><figure style="margin:0">{img(n, c, "(max-width: 680px) 50vw, 33vw")}<figcaption>{c}</figcaption></figure></a>'
                for n, c, cat in items)
    body = page_hero("Gallery", "A glimpse of the land, landscapes and lifestyle waiting for you at Vatika Estate.",
                     '<li aria-current="page">Gallery</li>', "green-paddy-fields-agricultural-land", "Green paddy fields") + f"""
<section class="section">
  <div class="container">
    <div class="filters" role="group" aria-label="Filter gallery">
      <button type="button" class="is-active" data-filter="all" aria-pressed="true">All</button>
      <button type="button" data-filter="project" aria-pressed="false">Vatika Luxora</button>
      <button type="button" data-filter="farmland" aria-pressed="false">Farmland</button>
      <button type="button" data-filter="farmhouse" aria-pressed="false">Farmhouses</button>
    </div>
    <div class="gallery">{g}</div>
  </div>
</section>
{cta_band()}"""
    page("gallery.html", "Gallery | Agricultural Land & Farmhouse Photos — Vatika Estate",
         "Browse photos of Vatika Estate agricultural land, Vatika Luxora layout plan, farmland and farmhouse inspiration in Shahapur & Kasara.",
         "gallery", body, ld=[breadcrumb_ld([("Home", ""), ("Gallery", "gallery.html")])])


def build_contact():
    body = page_hero("Contact Us", "Have a question or want to visit a site? Call, WhatsApp or send us a message — we're happy to help.",
                     '<li aria-current="page">Contact</li>', "orchard-pathway-farmhouse-kasara", "Orchard pathway near Kasara") + f"""
<section class="section">
  <div class="container contact-grid">
    <div>
      <span class="eyebrow">{icon("leaf")} Get In Touch</span>
      <h2 class="h-lg">Our contact information</h2>
      <p style="margin-bottom:28px">Reach us through any of the channels below.</p>
      <div class="info-cards">
        <div class="info-card"><div class="feature__icon">{icon("pin")}</div><div><h3>Our Address</h3><p>{ADDRESS}</p><a href="{MAP_LINK}" target="_blank" rel="noopener" style="margin-top:6px">Get directions →</a></div></div>
        <div class="info-card"><div class="feature__icon">{icon("phone")}</div><div><h3>Phone Number</h3><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div></div>
        <div class="info-card"><div class="feature__icon">{icon("wa")}</div><div><h3>WhatsApp</h3><a href="{WA_LINK}" target="_blank" rel="noopener">Chat on {PHONE_DISPLAY}</a></div></div>
        <div class="info-card"><div class="feature__icon">{icon("mail")}</div><div><h3>Email Address</h3><a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a><a href="mailto:{EMAIL_SALES}">{EMAIL_SALES}</a></div></div>
      </div>
    </div>
    <div class="form-card" id="schedule-visit">
      <h2 class="h-md" data-hide-on-success>Schedule a visit</h2>
      <p class="text-muted" data-hide-on-success>Fill in the form and our land advisor will get in touch to plan your site visit.</p>
      {lead_form("c", "Contact / Site Visit", in_modal=False, submit_label="Send Message")}
    </div>
  </div>
</section>
<section style="padding-bottom:100px">
  <div class="container">
    <div class="map"><iframe src="{MAP_EMBED}" title="Vatika Estate office location — Centrum IT Park, Wagle Estate, Thane" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
  </div>
</section>"""
    page("contact.html", "Contact Us | Vatika Estate, Thane — +91 83569 01661",
         "Contact Vatika Estate at Centrum IT Park, Wagle Estate, Thane West. Call or WhatsApp +91 83569 01661 to book a site visit for agricultural land in Shahapur & Kasara.",
         "contact", body, ld=[breadcrumb_ld([("Home", ""), ("Contact", "contact.html")])])


def build_privacy():
    body = page_hero("Privacy Policy", "How Vatika Estate collects, uses and protects your personal information.",
                     '<li aria-current="page">Privacy Policy</li>', "green-paddy-fields-agricultural-land", "Green fields") + f"""
<section class="section">
  <div class="container">
    <article class="legal">
      <span class="updated">Last updated: 14 October 2026</span>
      <p>Vatika Estate ("Vatika Estate", "we", "us" or "our") respects your privacy. This Privacy Policy explains how we collect, use, share and protect personal information when you visit <a href="index.html">vatikaestate.co.in</a> (the "Website") or contact us. By using the Website or submitting your details, you agree to the practices described below.</p>

      <h2>1. Information we collect</h2>
      <p>We collect only the information you choose to give us, and limited technical information:</p>
      <ul>
        <li><strong>Enquiry details</strong> — your name, mobile number, email address, project of interest, preferred site-visit date and any message you send through our enquiry, brochure, site-visit or contact forms.</li>
        <li><strong>Communication records</strong> — details of calls, WhatsApp messages or emails you exchange with us.</li>
        <li><strong>Technical information</strong> — basic data such as browser type, device and pages visited, which may be collected automatically by our hosting provider and embedded services.</li>
      </ul>

      <h2>2. How we use your information</h2>
      <ul>
        <li>To respond to your enquiries and call you back about our projects;</li>
        <li>To share brochures, price sheets, layout plans and project updates you request;</li>
        <li>To arrange and confirm site visits;</li>
        <li>To assist with documentation and the plot purchase process if you choose to proceed;</li>
        <li>To improve our Website and services, and to comply with legal obligations.</li>
      </ul>
      <p>We will contact you by phone, SMS, email or WhatsApp only in connection with your enquiry. You can ask us to stop at any time.</p>

      <h2>3. Sharing of information</h2>
      <p>We do <strong>not</strong> sell or rent your personal information. We may share it only with:</p>
      <ul>
        <li><strong>Indo Asian Buildcon Private Limited</strong>, our marketing partner, solely to respond to your enquiry;</li>
        <li>Service providers who help us run the Website and deliver form submissions by email, under appropriate confidentiality obligations;</li>
        <li>Government or legal authorities where required by law.</li>
      </ul>

      <h2 id="cookies">4. Cookies &amp; local storage</h2>
      <p>Our Website does not use advertising cookies. It uses your browser's local storage only to remember whether you have already seen or submitted our enquiry form, so we don't show it to you repeatedly. Embedded services such as Google Maps and Google Fonts may set their own cookies, governed by Google's privacy policy. You can clear or block cookies and local storage in your browser settings at any time.</p>

      <h2>5. Data security &amp; retention</h2>
      <p>We take reasonable technical and organisational measures to protect your information against unauthorised access, loss or misuse. We retain enquiry information only for as long as needed to serve you and to meet legal or regulatory requirements, after which it is deleted.</p>

      <h2>6. Your rights</h2>
      <p>In accordance with applicable Indian law, including the Digital Personal Data Protection Act, 2023, you may:</p>
      <ul>
        <li>Request access to the personal information we hold about you;</li>
        <li>Ask us to correct, update or erase your information;</li>
        <li>Withdraw your consent to being contacted;</li>
        <li>Raise a grievance about how your information is handled.</li>
      </ul>
      <p>To exercise these rights, email <a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a> or call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>

      <h2>7. Third-party links</h2>
      <p>Our Website links to third-party sites such as Facebook, Instagram, LinkedIn, WhatsApp and Google Maps. We are not responsible for their privacy practices and encourage you to read their policies.</p>

      <h2>8. Children's privacy</h2>
      <p>Our Website is not intended for individuals under 18 years of age, and we do not knowingly collect their personal information.</p>

      <h2>9. Changes to this policy</h2>
      <p>We may update this Privacy Policy from time to time. The latest version will always be available on this page with the updated date shown above.</p>

      <h2>10. Contact us</h2>
      <p>Vatika Estate<br>{ADDRESS}<br>Phone / WhatsApp: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>Email: <a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a></p>
    </article>
  </div>
</section>"""
    page("privacy-policy.html", "Privacy Policy | Vatika Estate",
         "Read the Vatika Estate privacy policy — what information we collect through our enquiry forms, how we use it, and your rights.",
         "", body, no_popup=True, ld=[breadcrumb_ld([("Home", ""), ("Privacy Policy", "privacy-policy.html")])])


def build_terms():
    body = page_hero("Terms of Service", "The terms that apply to your use of the Vatika Estate website.",
                     '<li aria-current="page">Terms of Service</li>', "green-paddy-fields-agricultural-land", "Green fields") + f"""
<section class="section">
  <div class="container">
    <article class="legal">
      <span class="updated">Last updated: 14 October 2026</span>
      <p>These Terms of Service govern your use of vatikaestate.co.in (the "Website"), operated by Vatika Estate. By accessing the Website you agree to these terms.</p>

      <h2>1. Information only</h2>
      <p>All content on this Website — including project descriptions, prices, plot sizes, layout plans, amenities and connectivity details — is provided for general information only. It does not constitute an offer, invitation to offer, or contract of any kind. Any purchase is governed solely by the agreement executed between you and the seller.</p>

      <h2>2. Images &amp; representations</h2>
      <p>Photographs, renderings and illustrations on the Website are for representational purposes only and may not depict the actual project, plots, structures or surroundings.</p>

      <h2>3. Pricing &amp; availability</h2>
      <p>Prices, plot availability, specifications and amenities are subject to change without prior notice. Please contact us for the latest information before making any decision.</p>

      <h2>4. Due diligence</h2>
      <p>Buyers are advised to independently verify all documents, approvals and details, and to seek professional legal and financial advice before purchasing any property.</p>

      <h2>5. Enquiries &amp; communication</h2>
      <p>By submitting a form on the Website, you consent to being contacted by Vatika Estate and its marketing partner, Indo Asian Buildcon Private Limited, regarding your enquiry. Your information is handled as described in our <a href="privacy-policy.html">Privacy Policy</a>.</p>

      <h2>6. Intellectual property</h2>
      <p>The Vatika Estate name, logo, text, graphics and brochures on this Website are the property of Vatika Estate and may not be copied or reused without written permission.</p>

      <h2>7. Limitation of liability</h2>
      <p>Vatika Estate is not liable for any loss or damage arising from reliance on information on this Website or from the use of any third-party links.</p>

      <h2>8. Governing law</h2>
      <p>These terms are governed by the laws of India, and courts at Thane, Maharashtra shall have exclusive jurisdiction.</p>

      <h2>9. Contact</h2>
      <p>Questions about these terms? Email <a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a> or call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
    </article>
  </div>
</section>"""
    page("terms.html", "Terms of Service | Vatika Estate",
         "Terms of service and disclaimer for the Vatika Estate website.",
         "", body, no_popup=True, ld=[breadcrumb_ld([("Home", ""), ("Terms of Service", "terms.html")])])


def build_404():
    body = f"""
<section class="notfound">
  <div class="container">
    <strong>404</strong>
    <h1 class="h-lg">This page has moved on</h1>
    <p class="lead">The page you're looking for doesn't exist. Let's get you back on solid ground.</p>
    <div class="btn-row" style="justify-content:center;margin-top:26px">
      <a class="btn btn--primary" href="index.html">Back to Home {icon("arrow", "icon--arrow")}</a>
      <a class="btn btn--outline" href="projects.html">View Projects</a>
    </div>
  </div>
</section>"""
    page("404.html", "Page Not Found | Vatika Estate", "The page you are looking for could not be found.", "", body, no_popup=True, base="/")


def build_seo_files():
    pages = [("", "1.0"), ("about.html", "0.8"), ("projects.html", "0.9"), ("vatika-luxora.html", "0.9"),
             ("gallery.html", "0.6"), ("contact.html", "0.8"), ("privacy-policy.html", "0.3"), ("terms.html", "0.3")]
    urls = "\n".join(f"  <url><loc>{SITE_URL}/{p}</loc><lastmod>2026-10-14</lastmod><priority>{pr}</priority></url>" for p, pr in pages)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    print("built sitemap.xml, robots.txt")


if __name__ == "__main__":
    build_home()
    build_about()
    build_projects()
    build_luxora()
    build_gallery()
    build_contact()
    build_privacy()
    build_terms()
    build_404()
    build_seo_files()
