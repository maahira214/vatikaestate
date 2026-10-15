/* ==========================================================================
   Vatika Estate — site scripts (no dependencies)
   ========================================================================== */
(function () {
  "use strict";

  /* ---------- Site configuration ---------- */
  var CONFIG = {
    // Every lead form posts here. FormSubmit forwards each submission to the inbox below.
    // The very first submission triggers a one-time activation email to this address.
    leadEmail: "vatikaestate2020@gmail.com",
    leadEndpoint: "https://formsubmit.co/ajax/vatikaestate2020@gmail.com",
    phoneDisplay: "+91 83569 01661",
    phoneTel: "+918356901661",
    whatsapp: "918356901661",
    brochureUrl: "assets/docs/vatika-luxora-brochure.pdf",
    brochureName: "Vatika-Luxora-Brochure.pdf",
    autoPopupDelay: 3000
  };

  var doc = document.documentElement;
  doc.classList.remove("no-js");
  var body = document.body;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  var store = {
    get: function (area, key) { try { return window[area].getItem(key); } catch (e) { return null; } },
    set: function (area, key, val) { try { window[area].setItem(key, val); } catch (e) { /* storage blocked */ } }
  };

  /* ---------- Scroll lock shared by drawer / modal / lightbox ---------- */
  var locks = 0;
  function lockScroll() { locks++; body.classList.add("is-locked"); }
  function unlockScroll() { locks = Math.max(0, locks - 1); if (!locks) body.classList.remove("is-locked"); }

  /* ---------- Sticky header + back to top ---------- */
  var header = $(".site-header");
  var toTop = $(".to-top");
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (header) header.classList.toggle("is-scrolled", y > 20);
    if (toTop) toTop.classList.toggle("is-visible", y > 600);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" }); });

  /* ---------- Desktop dropdown (click/keyboard support for touch screens) ---------- */
  $$(".nav [data-dropdown-toggle]").forEach(function (btn) {
    var li = btn.parentElement;
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      var open = !li.classList.contains("is-open");
      $$(".nav li.is-open").forEach(function (o) { o.classList.remove("is-open"); });
      li.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", String(open));
    });
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".nav")) $$(".nav li.is-open").forEach(function (o) {
      o.classList.remove("is-open");
      var b = $("[data-dropdown-toggle]", o); if (b) b.setAttribute("aria-expanded", "false");
    });
  });

  /* ---------- Mobile drawer ---------- */
  var drawer = $(".drawer");
  var overlay = $(".drawer-overlay");
  var menuToggle = $(".menu-toggle");
  function openDrawer() {
    drawer.classList.add("is-open"); overlay.classList.add("is-open");
    drawer.setAttribute("aria-hidden", "false"); menuToggle.setAttribute("aria-expanded", "true");
    lockScroll(); setTimeout(function () { $(".drawer__close", drawer).focus(); }, 50);
  }
  function closeDrawer(silent) {
    if (!drawer.classList.contains("is-open")) return;
    drawer.classList.remove("is-open"); overlay.classList.remove("is-open");
    drawer.setAttribute("aria-hidden", "true"); menuToggle.setAttribute("aria-expanded", "false");
    unlockScroll(); if (!silent) menuToggle.focus();
  }
  if (drawer && menuToggle) {
    menuToggle.addEventListener("click", openDrawer);
    $(".drawer__close", drawer).addEventListener("click", function () { closeDrawer(); });
    overlay.addEventListener("click", function () { closeDrawer(); });
    $$("[data-sub-toggle]", drawer).forEach(function (btn) {
      btn.addEventListener("click", function () {
        var sub = btn.nextElementSibling;
        var open = !sub.classList.contains("is-open");
        sub.classList.toggle("is-open", open);
        btn.setAttribute("aria-expanded", String(open));
      });
    });
    $$("a", drawer).forEach(function (a) { a.addEventListener("click", function () { closeDrawer(true); }); });
  }

  /* ---------- Hero slider ---------- */
  var hero = $("[data-hero]");
  if (hero) {
    var slides = $$(".hero__slide", hero);
    var imgs = $$(".hero__frame img", hero);
    var dotsWrap = $(".hero__dots", hero);
    var current = -1, timer = null, leaveTimer = null;
    slides.forEach(function (_, i) {
      var b = document.createElement("button");
      b.type = "button"; b.setAttribute("aria-label", "Show slide " + (i + 1));
      b.addEventListener("click", function () { go(i); restart(); });
      dotsWrap.appendChild(b);
    });
    var dots = $$("button", dotsWrap);
    function go(i) {
      var next = (i + slides.length) % slides.length;
      if (next === current) return;
      var prev = current;
      current = next;
      clearTimeout(leaveTimer);
      $$(".is-leaving", hero).forEach(function (el) { el.classList.remove("is-leaving"); });
      if (prev > -1) {
        slides[prev].classList.add("is-leaving");
        imgs[prev].classList.add("is-leaving");
      }
      slides.forEach(function (s, k) { s.classList.toggle("is-active", k === current); s.setAttribute("aria-hidden", String(k !== current)); });
      imgs.forEach(function (im, k) { im.classList.toggle("is-active", k === current); });
      dots.forEach(function (d, k) { d.classList.toggle("is-active", k === current); d.setAttribute("aria-current", k === current ? "true" : "false"); });
      leaveTimer = setTimeout(function () {
        $$(".is-leaving", hero).forEach(function (el) { el.classList.remove("is-leaving"); });
      }, 1500);
    }
    // Slides advance automatically every 6 s; the active dot shows the countdown.
    var HERO_DELAY = 6000;
    hero.style.setProperty("--hero-delay", HERO_DELAY + "ms");
    function restart() {
      clearInterval(timer);
      timer = setInterval(function () { go(current + 1); }, HERO_DELAY);
      // re-trigger the progress animation on the active dot
      dots.forEach(function (d) { d.classList.remove("is-active"); });
      void dotsWrap.offsetWidth;
      dots[current].classList.add("is-active");
    }
    $("[data-hero-prev]", hero).addEventListener("click", function () { go(current - 1); restart(); });
    $("[data-hero-next]", hero).addEventListener("click", function () { go(current + 1); restart(); });
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) clearInterval(timer); else restart();
    });
    var hx = null;
    hero.addEventListener("touchstart", function (e) { hx = e.touches[0].clientX; }, { passive: true });
    hero.addEventListener("touchend", function (e) {
      if (hx === null) return;
      var dx = e.changedTouches[0].clientX - hx;
      if (Math.abs(dx) > 50) { go(current + (dx < 0 ? 1 : -1)); restart(); }
      hx = null;
    });
    go(0); restart();
  }

  /* ---------- Carousels ---------- */
  $$("[data-carousel]").forEach(function (wrap) {
    var track = $(".carousel__track", wrap.closest("section") || wrap);
    var step = function () { var c = track.children[0]; return c ? c.getBoundingClientRect().width + 22 : 300; };
    $$("[data-carousel-prev]", wrap.closest("section")).forEach(function (b) {
      b.addEventListener("click", function () { track.scrollBy({ left: -step(), behavior: "smooth" }); });
    });
    $$("[data-carousel-next]", wrap.closest("section")).forEach(function (b) {
      b.addEventListener("click", function () {
        var atEnd = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
        track.scrollTo({ left: atEnd ? 0 : track.scrollLeft + step(), behavior: "smooth" });
      });
    });
    var down = false, startX = 0, startLeft = 0, moved = false;
    track.addEventListener("dragstart", function (e) { e.preventDefault(); });
    track.addEventListener("pointerdown", function (e) {
      if (e.pointerType !== "mouse" || e.button !== 0) return;
      down = true; moved = false; startX = e.clientX; startLeft = track.scrollLeft;
    });
    window.addEventListener("pointermove", function (e) {
      if (!down) return;
      var dx = e.clientX - startX;
      if (!moved && Math.abs(dx) > 5) { moved = true; track.classList.add("is-dragging"); }
      if (moved) track.scrollLeft = startLeft - dx;
    });
    window.addEventListener("pointerup", function () {
      if (!down) return;
      down = false;
      if (moved) {
        var w = step();
        var target = Math.round(track.scrollLeft / w) * w;
        track.classList.remove("is-dragging");
        track.scrollTo({ left: target, behavior: "smooth" });
      }
    });
    track.addEventListener("click", function (e) { if (moved) { e.preventDefault(); e.stopPropagation(); moved = false; } }, true);
  });

  /* ---------- Reveal on scroll + counters ---------- */
  function animateCount(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var decimals = (el.getAttribute("data-count").split(".")[1] || "").length;
    if (reduceMotion) { el.textContent = target.toFixed(decimals); return; }
    var start = null, dur = 1600;
    function tick(t) {
      if (!start) start = t;
      var p = Math.min((t - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = (target * eased).toFixed(decimals);
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add("is-in");
        (function (el) { setTimeout(function () { el.classList.add("reveal-done"); }, 1300); })(en.target);
        if (en.target.hasAttribute("data-count")) animateCount(en.target);
        io.unobserve(en.target);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    $$(".reveal, [data-count]").forEach(function (el) { io.observe(el); });
  } else {
    $$(".reveal").forEach(function (el) { el.classList.add("is-in"); });
    $$("[data-count]").forEach(function (el) { el.textContent = el.getAttribute("data-count"); });
  }

  /* ---------- Focus trap helper ---------- */
  function trapFocus(container, e) {
    if (e.key !== "Tab") return;
    var f = $$('a[href], button:not([disabled]), input:not([type="hidden"]):not(.hp input), select, textarea, [tabindex]:not([tabindex="-1"])', container)
      .filter(function (el) { return el.offsetParent !== null; });
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }

  /* ---------- Lead modal ---------- */
  var modal = $("#lead-modal");
  var lastFocus = null;
  var MODES = {
    enquiry: { title: "Enquire Now", text: "Share your details and our team will get in touch with you. You'll also get access to the project brochure.", submit: "Submit Enquiry", type: "Enquiry" },
    brochure: { title: "Get the Brochure", text: "Fill in your details to get the Vatika Luxora brochure.", submit: "Get Brochure", type: "Brochure Request" },
    visit: { title: "Request a Site Visit", text: "Pick a date that suits you and our team will get in touch to plan your visit.", submit: "Request Visit", type: "Site Visit Request" },
    auto: { title: "Enquire Now", text: "Interested in agricultural land in Shahapur & Kasara? Share your details and get the Vatika Luxora brochure.", submit: "Get Brochure", type: "Popup Lead" }
  };

  function setMode(mode, project) {
    var m = MODES[mode] || MODES.enquiry;
    modal.setAttribute("data-mode", mode);
    $("#lead-modal-title").textContent = m.title;
    $("#lead-modal-text").textContent = m.text;
    var form = $("form", modal);
    $(".btn__label", form).textContent = m.submit;
    form.querySelector('[name="form_type"]').value = m.type;
    var dateInput = form.querySelector('[name="preferred_date"]');
    if (dateInput) {
      dateInput.required = mode === "visit";
      var today = new Date(); today.setDate(today.getDate() + 1);
      dateInput.min = today.toISOString().slice(0, 10);
    }
    if (project) {
      var sel = form.querySelector('[name="project"]');
      if (sel) {
        var found = $$("option", sel).some(function (o) { return o.value === project; });
        if (!found) { var o = document.createElement("option"); o.value = project; o.textContent = project; sel.appendChild(o); }
        sel.value = project;
      }
    }
  }

  function openModal(mode, project, trigger) {
    if (!modal) return;
    resetForm($("form", modal));
    setMode(mode, project);
    lastFocus = trigger || document.activeElement;
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    lockScroll();
    store.set("sessionStorage", "vatika_popup_shown", "1");
    setTimeout(function () { var f = modal.querySelector('input[name="name"]'); if (f) f.focus(); }, 80);
  }
  function closeModal() {
    if (!modal || !modal.classList.contains("is-open")) return;
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    unlockScroll();
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-enquire]");
    if (!t) return;
    e.preventDefault();
    closeDrawer(true);
    openModal(t.getAttribute("data-enquire") || "enquiry", t.getAttribute("data-project"), t);
  });
  if (modal) {
    $$("[data-modal-close]", modal).forEach(function (b) { b.addEventListener("click", closeModal); });
    modal.addEventListener("keydown", function (e) { trapFocus($(".modal__dialog", modal), e); });
  }

  /* Automatic lead popup — 3 seconds after landing, once per browser session,
     never shown again after the visitor has submitted a form. */
  if (modal && !body.hasAttribute("data-no-popup") && location.search.indexOf("nopopup") === -1) {
    var alreadyLead = store.get("localStorage", "vatika_lead_submitted") === "1";
    var shown = store.get("sessionStorage", "vatika_popup_shown") === "1";
    if (!alreadyLead && !shown) {
      setTimeout(function () {
        var busy = modal.classList.contains("is-open") || (drawer && drawer.classList.contains("is-open")) || $(".lightbox.is-open");
        var typing = document.activeElement && /INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName);
        if (!busy && !typing) openModal("auto", null, null);
      }, CONFIG.autoPopupDelay);
    }
  }

  /* ---------- Lead forms ---------- */
  function fieldWrap(input) { return input.closest(".field") || input.closest(".check"); }
  function setError(input, msg) {
    var w = fieldWrap(input); if (!w) return;
    w.classList.add("has-error");
    var err = $(".field__error", w); if (err && msg) err.textContent = msg;
    input.setAttribute("aria-invalid", "true");
  }
  function clearError(input) {
    var w = fieldWrap(input); if (!w) return;
    w.classList.remove("has-error"); input.removeAttribute("aria-invalid");
  }
  function cleanPhone(v) {
    var d = String(v || "").replace(/\D/g, "");
    if (d.length === 12 && d.indexOf("91") === 0) d = d.slice(2);
    if (d.length === 11 && d.charAt(0) === "0") d = d.slice(1);
    return d;
  }
  function validate(form) {
    var ok = true, firstBad = null;
    $$("input, select, textarea", form).forEach(function (el) {
      if (el.closest(".hp") || el.type === "hidden") return;
      clearError(el);
      var v = (el.type === "checkbox") ? el.checked : el.value.trim();
      var msg = "";
      if (el.required && !v) msg = el.type === "checkbox" ? "Please accept to continue." : "This field is required.";
      else if (el.name === "name" && v && v.length < 2) msg = "Please enter your full name.";
      else if (el.name === "phone" && v && !/^[6-9]\d{9}$/.test(cleanPhone(v))) msg = "Enter a valid 10-digit mobile number.";
      else if (el.type === "email" && v && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)) msg = "Enter a valid email address.";
      if (msg) { ok = false; setError(el, msg); if (!firstBad) firstBad = el; }
    });
    if (firstBad) firstBad.focus();
    return ok;
  }
  function resetForm(form) {
    if (!form) return;
    form.reset();
    form.hidden = false;
    $$(".has-error", form).forEach(function (w) { w.classList.remove("has-error"); });
    var alert = $(".form-alert", form); if (alert) alert.classList.remove("is-visible");
    var wrap = form.parentElement;
    var success = $(".form-success", wrap); if (success) success.classList.remove("is-visible");
    $$("[data-hide-on-success]", wrap).forEach(function (el) { el.hidden = false; });
  }
  function downloadBrochure() {
    var a = document.createElement("a");
    a.href = CONFIG.brochureUrl; a.download = CONFIG.brochureName; a.rel = "noopener";
    body.appendChild(a); a.click(); a.remove();
  }

  $$("form[data-lead-form]").forEach(function (form) {
    $$("input, select, textarea", form).forEach(function (el) {
      el.addEventListener("input", function () { clearError(el); });
      el.addEventListener("change", function () { clearError(el); });
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var alertBox = $(".form-alert", form);
      if (alertBox) alertBox.classList.remove("is-visible");
      if (!validate(form)) return;

      // Honeypot: bots fill hidden fields — pretend success, send nothing.
      var honey = form.querySelector('[name="_honey"]');
      var btn = $("button[type=submit]", form);
      var fd = new FormData(form);
      var data = {};
      fd.forEach(function (v, k) { if (k !== "_honey" && k !== "consent") data[k] = String(v).trim(); });
      data.phone = "+91 " + cleanPhone(data.phone);
      var formType = data.form_type || "Enquiry";
      var payload = {
        "Lead Type": formType,
        "Name": data.name,
        "Phone": data.phone,
        "Email": data.email || "—",
        "Interested In": data.project || "—",
        "Preferred Visit Date": data.preferred_date || "—",
        "Message": data.message || "—",
        "Page": document.title + " (" + location.href + ")",
        "Submitted At": new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" }) + " IST",
        "_subject": "New " + formType + " — " + data.name + " | Vatika Estate Website",
        "_template": "table",
        "_captcha": "false"
      };
      if (data.email) payload._replyto = data.email;

      function onSuccess() {
        store.set("localStorage", "vatika_lead_submitted", "1");
        var wrap = form.parentElement;
        var success = $(".form-success", wrap);
        var nameSlot = success && $("[data-lead-name]", success);
        if (nameSlot) nameSlot.textContent = data.name.split(" ")[0];
        form.hidden = true;
        $$("[data-hide-on-success]", wrap).forEach(function (el) { el.hidden = true; });
        if (success) {
          success.classList.add("is-visible");
          var h = $("h3", success);
          if (h) { h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: true }); }
          if (!form.closest(".modal")) success.scrollIntoView({ behavior: "smooth", block: "center" });
        }
        if (formType === "Brochure Request" || formType === "Popup Lead") downloadBrochure();
        if (typeof window.gtag === "function") window.gtag("event", "generate_lead", { form_type: formType });
      }

      if (honey && honey.value) { onSuccess(); return; }

      btn.classList.add("is-loading"); btn.disabled = true;
      fetch(CONFIG.leadEndpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(payload)
      })
        .then(function (res) { return res.json().catch(function () { return {}; }).then(function (j) { return { ok: res.ok, json: j }; }); })
        .then(function (r) {
          var success = r.ok && String(r.json.success) !== "false";
          if (!success) throw new Error(r.json.message || "Submission failed");
          onSuccess();
        })
        .catch(function (err) {
          // Site owners: the exact reason (e.g. "This form needs Activation") is logged here.
          if (window.console) console.warn("[Vatika lead form] Not delivered: " + (err && err.message));
          if (alertBox) {
            var lines = ["Hi Vatika Estate, " + formType, "Name: " + data.name, "Phone: " + data.phone];
            if (data.email) lines.push("Email: " + data.email);
            if (data.project) lines.push("Interested in: " + data.project);
            if (data.preferred_date) lines.push("Visit date: " + data.preferred_date);
            if (data.message) lines.push("Message: " + data.message);
            var waText = encodeURIComponent(lines.join("\n"));
            alertBox.innerHTML = "Sorry, we couldn't send your details right now. <a href=\"https://wa.me/" + CONFIG.whatsapp + "?text=" + waText + "\" target=\"_blank\" rel=\"noopener\">Send them on WhatsApp</a> or call us on <a href=\"tel:" + CONFIG.phoneTel + "\">" + CONFIG.phoneDisplay + "</a>.";
            alertBox.classList.add("is-visible");
          }
        })
        .then(function () { btn.classList.remove("is-loading"); btn.disabled = false; });
    });
  });

  // "Download brochure" buttons that appear only after a lead is captured
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-brochure-download]");
    if (!b) return;
    e.preventDefault();
    downloadBrochure();
  });

  /* ---------- Lightbox ---------- */
  var lb = $(".lightbox");
  if (lb) {
    var lbImg = $("img", lb), lbCap = $("figcaption", lb), lbCount = $(".lightbox__count", lb);
    var group = [], idx = 0, lbLast = null;
    function show(i) {
      idx = (i + group.length) % group.length;
      var item = group[idx];
      var src = item.getAttribute("href");
      if (lbImg.getAttribute("src") !== src) {
        lbImg.classList.add("is-swapping");
        var pre = new Image();
        pre.onload = pre.onerror = function () { lbImg.src = src; requestAnimationFrame(function () { lbImg.classList.remove("is-swapping"); }); };
        pre.src = src;
      }
      lbImg.alt = item.getAttribute("data-caption") || "";
      lbCap.textContent = item.getAttribute("data-caption") || "";
      lbCount.textContent = (idx + 1) + " / " + group.length;
      var multi = group.length > 1;
      $(".lightbox__prev", lb).hidden = !multi; $(".lightbox__next", lb).hidden = !multi;
    }
    function openLb(link) {
      var name = link.getAttribute("data-lightbox");
      group = $$('[data-lightbox="' + name + '"]').filter(function (a) { return !a.classList.contains("is-hidden"); });
      lbLast = link;
      show(group.indexOf(link));
      lb.classList.add("is-open"); lb.setAttribute("aria-hidden", "false");
      lockScroll(); $(".lightbox__close", lb).focus();
    }
    function closeLb() {
      if (!lb.classList.contains("is-open")) return;
      lb.classList.remove("is-open"); lb.setAttribute("aria-hidden", "true");
      unlockScroll(); if (lbLast) lbLast.focus();
    }
    document.addEventListener("click", function (e) {
      var a = e.target.closest("[data-lightbox]");
      if (!a) return; e.preventDefault(); openLb(a);
    });
    $(".lightbox__close", lb).addEventListener("click", closeLb);
    $(".lightbox__prev", lb).addEventListener("click", function () { show(idx - 1); });
    $(".lightbox__next", lb).addEventListener("click", function () { show(idx + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) closeLb(); });
    lb.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") show(idx - 1);
      if (e.key === "ArrowRight") show(idx + 1);
      trapFocus(lb, e);
    });
    var sx = null;
    lb.addEventListener("touchstart", function (e) { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) {
      if (sx === null) return;
      var dx = e.changedTouches[0].clientX - sx;
      if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1));
      sx = null;
    });
    window.__closeLightbox = closeLb;
  }

  /* ---------- Gallery filter ---------- */
  var filters = $(".filters");
  if (filters) {
    filters.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-filter]");
      if (!b) return;
      var f = b.getAttribute("data-filter");
      $$("button", filters).forEach(function (x) { x.classList.toggle("is-active", x === b); x.setAttribute("aria-pressed", String(x === b)); });
      $$(".gallery__item").forEach(function (it) {
        var show = f === "all" || (it.getAttribute("data-cat") || "").split(" ").indexOf(f) > -1;
        it.classList.toggle("is-hidden", !show);
        it.classList.remove("is-shown");
        if (show) { void it.offsetWidth; it.classList.add("is-shown"); }
      });
    });
  }

  /* ---------- Global Escape key ---------- */
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    if (lb && lb.classList.contains("is-open")) { window.__closeLightbox(); return; }
    if (modal && modal.classList.contains("is-open")) { closeModal(); return; }
    if (drawer && drawer.classList.contains("is-open")) closeDrawer();
  });
})();
