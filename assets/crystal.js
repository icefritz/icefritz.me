/* IceFritz crystal menu. Pages add <div class="crystal-nav" data-crystal-nav></div>; this fills it in.
   Click or tap the crystal to open; click outside or press Esc to close. No hover. */
(function () {
  var PAGES = [
    { href: "/", title: "Home", sub: "Break the ice" },
    { href: "/boosts/", title: "Boosts", sub: "Server & resource boosts" }
  ];
  var GEM = '<svg class="crystal" viewBox="0 0 40 80" aria-hidden="true">' +
    '<path d="M20 0 34 34 20 80 6 34Z" fill="#51c5d9"/><path d="M20 0 34 34H20Z" fill="#b6f0fb"/>' +
    '<path d="M20 0 6 34H20Z" fill="#7fdcef"/><path d="M20 80 34 34H20Z" fill="#284e68"/>' +
    '<defs><clipPath id="gem-clip"><path d="M20 0 34 34 20 80 6 34Z"/></clipPath></defs>' +
    '<g class="cracks" clip-path="url(#gem-clip)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round">' +
    '<path pathLength="1" d="M20 31 16 24 18 17 15 8" stroke-width="1.2"/><path pathLength="1" d="M20 31 25 37 22 46 26 56" stroke-width="1.2"/>' +
    '<path pathLength="1" d="M20 31 13 37 10 34" stroke-width=".9"/><path pathLength="1" d="M20 31 28 26 31 31" stroke-width=".9"/>' +
    '<path pathLength="1" d="M22 46 17 51 18 60" stroke-width=".7"/><path pathLength="1" d="M16 24 11 27" stroke-width=".6"/></g></svg>' +
    '<span class="shards" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></span>';

  function norm(p) { return p.replace(/index\.html$/, "").replace(/\/?$/, "/"); }
  function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;"); }

  function init(wrap) {
    var here = norm(location.pathname);
    var items = PAGES.filter(function (p) { return norm(p.href) !== here; });
    wrap.innerHTML =
      '<button class="crystal-btn" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu" title="Menu">' + GEM + "</button>" +
      '<nav class="site-nav" id="site-nav" aria-label="Site">' +
      items.map(function (p) { return '<a href="' + p.href + '"><b>' + esc(p.title) + "</b><span>" + esc(p.sub) + "</span></a>"; }).join("") +
      "</nav>";

    var btn = wrap.querySelector(".crystal-btn");
    var links = wrap.querySelectorAll(".site-nav a");
    var burst;

    function crack() {
      btn.classList.remove("burst", "shake");
      void btn.offsetWidth; // restart the animation
      btn.classList.add("burst", "shake");
      clearTimeout(burst);
      burst = setTimeout(function () { btn.classList.remove("burst", "shake"); }, 700);
    }
    function set(open) {
      if (open && !wrap.classList.contains("is-open")) crack();
      wrap.classList.toggle("is-open", open);
      document.documentElement.classList.toggle("menu-open", open);
      btn.setAttribute("aria-expanded", String(open));
      btn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      links.forEach(function (a) { a.tabIndex = open ? 0 : -1; });
    }
    set(false);
    btn.addEventListener("click", function () { set(!wrap.classList.contains("is-open")); });
    document.addEventListener("click", function (e) { if (!wrap.contains(e.target)) set(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && wrap.classList.contains("is-open")) { set(false); btn.focus(); } });
    wrap.addEventListener("focusout", function (e) { if (e.relatedTarget && !wrap.contains(e.relatedTarget)) set(false); });
    window.addEventListener("pageshow", function () { set(false); });
  }

  function start() { document.querySelectorAll("[data-crystal-nav]").forEach(init); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
