(function () {
  const mount = document.querySelector(".hubspot-form-mount");
  const fallback = document.getElementById("hubspot-form-fallback");
  if (!mount || !fallback) return;

  function formMounted() {
    const iframe = mount.querySelector("iframe");
    if (iframe && iframe.offsetHeight > 120) return true;
    if (mount.querySelector(".hs-form-field, .hs-form, form")) return true;
    return false;
  }

  window.setTimeout(function () {
    if (!formMounted()) {
      fallback.hidden = false;
    }
  }, 6000);
})();