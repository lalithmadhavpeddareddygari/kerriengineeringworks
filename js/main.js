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

  /* Gallery carousel */
  const track = document.getElementById("gallery-track");
  if (track) {
    const slides = Array.from(track.querySelectorAll(".gallery-slide"));
    let current = 0;
    const galleryReduceMotion = window.matchMedia(
      "(prefers-reduced-motion: reduce)"
    ).matches;

    function slideScrollLeft(index) {
      const slide = slides[index];
      const tRect = track.getBoundingClientRect();
      const sRect = slide.getBoundingClientRect();
      return (
        track.scrollLeft +
        (sRect.left - tRect.left) -
        (track.clientWidth - slide.offsetWidth) / 2
      );
    }

    function nearestIndex() {
      const mid = track.getBoundingClientRect().left + track.clientWidth / 2;
      let best = 0;
      let bestDist = Infinity;
      slides.forEach((slide, i) => {
        const r = slide.getBoundingClientRect();
        const d = Math.abs(r.left + r.width / 2 - mid);
        if (d < bestDist) {
          bestDist = d;
          best = i;
        }
      });
      return best;
    }

    function updateActive(i) {
      const idx = typeof i === "number" ? i : nearestIndex();
      current = idx;
      slides.forEach((slide, n) => {
        slide.classList.toggle("is-active", n === idx);
      });
    }

    function goTo(i, instant) {
      if (!slides.length) return;
      current = (i + slides.length) % slides.length;
      track.scrollTo({
        left: slideScrollLeft(current),
        behavior: instant || galleryReduceMotion ? "auto" : "smooth",
      });
      updateActive(current);
    }

    let scrollTick;
    track.addEventListener(
      "scroll",
      () => {
        updateActive();
        clearTimeout(scrollTick);
        scrollTick = setTimeout(() => updateActive(), 60);
      },
      { passive: true }
    );

    window.addEventListener("resize", () => goTo(current, true));

    const prevBtn = track.parentElement.querySelector(".gallery-nav--prev");
    const nextBtn = track.parentElement.querySelector(".gallery-nav--next");
    if (prevBtn) prevBtn.addEventListener("click", () => goTo(current - 1));
    if (nextBtn) nextBtn.addEventListener("click", () => goTo(current + 1));

    track.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        goTo(current - 1);
      }
      if (e.key === "ArrowRight") {
        e.preventDefault();
        goTo(current + 1);
      }
    });

    let touchStartX = 0;
    track.addEventListener(
      "touchstart",
      (e) => {
        touchStartX = e.changedTouches[0].screenX;
      },
      { passive: true }
    );
    track.addEventListener(
      "touchend",
      (e) => {
        const dx = e.changedTouches[0].screenX - touchStartX;
        if (Math.abs(dx) > 48) {
          goTo(dx < 0 ? current + 1 : current - 1);
        }
      },
      { passive: true }
    );

    window.requestAnimationFrame(() => {
      goTo(0, true);
      updateActive(0);
    });
    window.addEventListener("load", () => goTo(current, true));
  }
})();