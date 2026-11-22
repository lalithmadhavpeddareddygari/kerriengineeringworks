/* Kerri Engineering Works — site behaviour */

(function () {
  document.documentElement.classList.add("js-enhanced");

  const navToggle = document.getElementById("navToggle");
  const headerNav = document.getElementById("headerNav");
  const siteHeader = document.getElementById("siteHeader");

  if (navToggle && headerNav) {
    navToggle.addEventListener("click", () => {
      const isOpen = headerNav.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      navToggle.setAttribute(
        "aria-label",
        isOpen ? "Close menu" : "Open menu"
      );
    });

    headerNav.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        headerNav.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.setAttribute("aria-label", "Open menu");
      });
    });
  }

  if (siteHeader) {
    const onScroll = () => {
      siteHeader.classList.toggle("is-scrolled", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", (e) => {
      const id = anchor.getAttribute("href");
      if (!id || id.length < 2) return;
      const target = document.querySelector(id);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });

  /* Reveal on scroll — never leave content hidden */
  const revealEls = document.querySelectorAll(".reveal");
  const reduceMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  function markVisible(el) {
    el.classList.add("is-visible");
  }

  function revealInViewport() {
    const vh = window.innerHeight || document.documentElement.clientHeight;
    revealEls.forEach((el) => {
      const rect = el.getBoundingClientRect();
      if (rect.top < vh * 0.94 && rect.bottom > 0) {
        markVisible(el);
      }
    });
  }

  document
    .querySelectorAll(".page-hero .reveal, .hero .reveal, .clients-feature .reveal")
    .forEach(markVisible);

  if (revealEls.length) {
    if (reduceMotion) {
      revealEls.forEach(markVisible);
    } else if ("IntersectionObserver" in window) {
      const revealObs = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              markVisible(entry.target);
              revealObs.unobserve(entry.target);
            }
          });
        },
        { rootMargin: "0px 0px 5% 0px", threshold: 0.02 }
      );
      revealEls.forEach((el) => revealObs.observe(el));
      revealInViewport();
      window.addEventListener("load", revealInViewport);
      window.addEventListener("resize", revealInViewport);
      window.setTimeout(() => revealEls.forEach(markVisible), 4000);
    } else {
      revealEls.forEach(markVisible);
    }
  }

  /* Hero image crossfade */
  const heroSlides = document.querySelectorAll(".hero__slide");
  const reduceMotionHero = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;
  if (heroSlides.length > 1 && !reduceMotionHero) {
    let heroIdx = 0;
    window.setInterval(() => {
      heroSlides[heroIdx].classList.remove("is-active");
      heroIdx = (heroIdx + 1) % heroSlides.length;
      heroSlides[heroIdx].classList.add("is-active");
    }, 7000);
  }

  /* Stat counters */
  const statCounters = document.querySelectorAll("[data-count]");
  const reduceMotionStats = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;
  function animateCounter(el) {
    const target = Number(el.getAttribute("data-count"));
    const suffix = el.getAttribute("data-suffix") || "";
    if (!Number.isFinite(target) || reduceMotionStats) return;
    const duration = 1200;
    const start = performance.now();
    const tick = (now) => {
      const t = Math.min(1, (now - start) / duration);
      const val = Math.round(target * (0.3 + 0.7 * t));
      el.textContent = `${val}${suffix}`;
      if (t < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }
  if (statCounters.length && "IntersectionObserver" in window) {
    const statObs = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            statObs.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.4 }
    );
    statCounters.forEach((el) => statObs.observe(el));
  }
})();