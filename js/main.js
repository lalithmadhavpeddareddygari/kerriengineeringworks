/* Kerri Engineering Works — minimal site JS */

(function () {
  const navToggle = document.getElementById("navToggle");
  const headerNav = document.getElementById("headerNav");

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

  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", (e) => {
      const id = anchor.getAttribute("href");
      if (id.length < 2) return;
      const target = document.querySelector(id);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });
})();