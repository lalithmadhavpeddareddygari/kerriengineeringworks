#!/usr/bin/env python3
"""Capture KEW page screenshots after scroll-triggering reveals and lazy images."""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright

BASE_URL = "http://127.0.0.1:8765"
OUT_DIR = Path("/opt/cursor/artifacts/kew-screenshots")
VERSION = "v7"

PAGES = [
    ("index.html", "index"),
    ("products.html", "products"),
    ("about.html", "about"),
    ("clients.html", "clients"),
    ("contact.html", "contact"),
    ("horizontal-system.html", "horizontal-system"),
    ("vertical-system.html", "vertical-system"),
    ("macro-etching.html", "macro-etching"),
    ("dust-conveying.html", "dust-conveying"),
]

VIEWPORTS = {
    "desktop": {"width": 1440, "height": 900},
    "mobile": {"width": 390, "height": 844},
}

DESKTOP_CAPTURE_SCALE = 2


async def wait_for_images(page) -> None:
    await page.evaluate(
        """async () => {
      const imgs = Array.from(document.images);
      await Promise.all(
        imgs.map(
          (img) =>
            new Promise((resolve) => {
              if (img.complete && img.naturalWidth > 0) {
                resolve();
                return;
              }
              const done = () => resolve();
              img.addEventListener("load", done, { once: true });
              img.addEventListener("error", done, { once: true });
              setTimeout(done, 12000);
            })
        )
      );
    }"""
    )


async def scroll_full_page(page) -> None:
    await page.evaluate(
        """async () => {
      const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
      const step = Math.max(320, window.innerHeight * 0.72);
      let y = 0;
      const max = document.body.scrollHeight;
      while (y <= max) {
        window.scrollTo({ top: y, behavior: "instant" });
        await sleep(180);
        y += step;
      }
      window.scrollTo({ top: document.body.scrollHeight, behavior: "instant" });
      await sleep(400);
      window.scrollTo({ top: 0, behavior: "instant" });
      await sleep(250);
    }"""
    )


async def wait_for_hero(page) -> None:
    await page.evaluate(
        """async () => {
      const slide = document.querySelector('.hero__slide.is-active, .hero__slide');
      if (!slide || !(slide instanceof HTMLImageElement)) return;
      await new Promise((resolve) => {
        if (slide.complete && slide.naturalWidth > 0) {
          resolve();
          return;
        }
        const done = () => resolve();
        slide.addEventListener('load', done, { once: true });
        slide.addEventListener('error', done, { once: true });
        setTimeout(done, 15000);
      });
    }"""
    )


async def wait_for_contact_embeds(page) -> None:
    await page.wait_for_timeout(800)
    try:
        await page.wait_for_selector(".map-wrap iframe", timeout=20000)
        map_frame = page.frame_locator(".map-wrap iframe")
        await page.locator(".map-wrap").scroll_into_view_if_needed()
        await page.wait_for_timeout(2500)
        await map_frame.locator("body").wait_for(state="attached", timeout=15000)
    except Exception:
        pass
    try:
        await page.wait_for_selector(
            ".hubspot-form-mount iframe, .hubspot-wrap__target iframe",
            timeout=45000,
        )
    except Exception:
        pass
    await page.wait_for_timeout(6500)


async def enable_capture_mode(page) -> None:
    await page.evaluate(
        """() => {
      document.documentElement.classList.add("capture-mode");
    }"""
    )


async def force_reveals_visible(page) -> None:
    await page.evaluate(
        """() => {
      document.querySelectorAll('.reveal').forEach((el) => {
        el.classList.add('is-visible');
      });
    }"""
    )


async def assert_index_images_loaded(page) -> None:
    ok = await page.evaluate(
        """() => {
      const checks = [
        '.home-visual-strip img',
        '.home-product-card img.img-lifted',
        '.home-product-card img[src*="horizontal-station"]',
      ];
      return checks.every((sel) => {
        const img = document.querySelector(sel);
        return img && img.complete && img.naturalWidth > 0;
      });
    }"""
    )
    if not ok:
        await wait_for_images(page)
        ok = await page.evaluate(
            """() => {
        const imgs = document.querySelectorAll(
          '.home-visual-strip img, .home-product-card__media img'
        );
        return Array.from(imgs).every(
          (img) => img.complete && img.naturalWidth > 0
        );
      }"""
        )
    if not ok:
        raise RuntimeError("index.html: critical images did not finish loading")


async def capture_page(
    browser, path: str, slug: str, label: str, version: str
) -> None:
    context = await browser.new_context(
        viewport=VIEWPORTS[label],
        device_scale_factor=DESKTOP_CAPTURE_SCALE if label == "desktop" else 2,
    )
    page = await context.new_page()
    if slug in ("contact", "index"):
        wait_until = "networkidle"
    else:
        wait_until = "load"
    await page.goto(f"{BASE_URL}/{path}", wait_until=wait_until, timeout=90000)
    await page.wait_for_timeout(400)
    if slug == "index":
        await wait_for_hero(page)
        await wait_for_images(page)
        await page.wait_for_timeout(400)
    await force_reveals_visible(page)
    await page.evaluate("window.scrollTo({ top: 0, behavior: 'instant' })")
    await page.wait_for_timeout(300)
    if slug == "index":
        await wait_for_hero(page)
    await scroll_full_page(page)
    await wait_for_images(page)
    await force_reveals_visible(page)
    await scroll_full_page(page)
    await wait_for_images(page)
    await force_reveals_visible(page)
    await page.evaluate("window.scrollTo({ top: 0, behavior: 'instant' })")
    await page.wait_for_timeout(400)
    if slug == "index":
        await wait_for_images(page)
        await assert_index_images_loaded(page)
    if slug == "contact":
        await wait_for_contact_embeds(page)
        await scroll_full_page(page)
        await wait_for_contact_embeds(page)
    await enable_capture_mode(page)
    await page.evaluate("window.scrollTo({ top: 0, behavior: 'instant' })")
    await page.wait_for_timeout(200)
    out = OUT_DIR / f"{slug}-{label}-{version}.png"
    await page.screenshot(path=str(out), full_page=True)
    await context.close()
    print(f"wrote {out}")


async def main() -> None:
    parser = argparse.ArgumentParser(description="Capture KEW page screenshots")
    parser.add_argument(
        "--version",
        default=VERSION,
        help="Filename suffix (default: %(default)s)",
    )
    parser.add_argument("--slug", help="Capture only this page slug (e.g. index)")
    parser.add_argument(
        "--slugs",
        help="Comma-separated slugs (e.g. index,contact); overrides default page list",
    )
    parser.add_argument(
        "--viewport",
        choices=("desktop", "mobile"),
        help="Capture only this viewport (requires --slug)",
    )
    args = parser.parse_args()
    version = args.version

    pages = PAGES
    if args.slugs:
        wanted = {s.strip() for s in args.slugs.split(",") if s.strip()}
        pages = [(p, s) for p, s in PAGES if s in wanted]
        if len(pages) != len(wanted):
            missing = wanted - {s for _, s in pages}
            print(f"unknown slug(s): {', '.join(sorted(missing))}", file=sys.stderr)
            sys.exit(1)
    elif args.slug:
        pages = [(p, s) for p, s in PAGES if s == args.slug]
        if not pages:
            print(f"unknown slug: {args.slug}", file=sys.stderr)
            sys.exit(1)

    viewports = list(VIEWPORTS.keys())
    if args.viewport:
        viewports = [args.viewport]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for path, slug in pages:
            for label in viewports:
                await capture_page(browser, path, slug, label, version)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())