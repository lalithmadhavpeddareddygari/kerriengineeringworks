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
    "laptop1366": {"width": 1366, "height": 768},
    "laptop1440": {"width": 1440, "height": 900},
}

LAPTOP_FIRST_VIEW_KEYS = ("laptop1366", "laptop1440")

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


async def assert_stats_in_viewport(page) -> dict:
    return await page.evaluate(
        """() => {
      const band = document.querySelector(
        ".stats-band--hero-foot, main .stats-band"
      );
      if (!band) {
        return { ok: false, reason: "no stats band" };
      }
      const rect = band.getBoundingClientRect();
      const vh = window.innerHeight;
      const visible =
        rect.top >= -2 &&
        rect.bottom <= vh + 2 &&
        rect.height > 0;
      return {
        ok: visible,
        top: rect.top,
        bottom: rect.bottom,
        vh,
      };
    }"""
    )


async def capture_page(
    browser,
    path: str,
    slug: str,
    label: str,
    version: str,
    *,
    full_page: bool = True,
) -> None:
    viewport = VIEWPORTS[label]
    scale = DESKTOP_CAPTURE_SCALE if label in ("desktop", "laptop1366", "laptop1440") else 2
    if not full_page:
        scale = 1
    context = await browser.new_context(
        viewport=viewport,
        device_scale_factor=scale,
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
    if full_page:
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
    else:
        await wait_for_images(page)
        if slug == "index":
            await wait_for_hero(page)
    await enable_capture_mode(page)
    await page.evaluate("window.scrollTo({ top: 0, behavior: 'instant' })")
    await page.wait_for_timeout(200)
    if slug == "index" and not full_page:
        check = await assert_stats_in_viewport(page)
        if not check.get("ok"):
            raise RuntimeError(f"index first view: stats not in viewport: {check}")
        print(f"stats in viewport OK ({label}): {check}")
    if full_page:
        suffix = label
        out = OUT_DIR / f"{slug}-{suffix}-{version}.png"
    else:
        short = "1366" if label == "laptop1366" else "1440"
        out = OUT_DIR / f"{slug}-firstview-{short}-{version}.png"
    await page.screenshot(path=str(out), full_page=full_page)
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
        choices=tuple(VIEWPORTS.keys()),
        help="Capture only this viewport (requires --slug unless --first-view)",
    )
    parser.add_argument(
        "--first-view",
        action="store_true",
        help="Viewport-only capture of index at 1366×768 and 1440×900",
    )
    parser.add_argument(
        "--full-page",
        action="store_true",
        help="Full-page captures (default when not using --first-view only)",
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

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        if args.first_view:
            for label in LAPTOP_FIRST_VIEW_KEYS:
                await capture_page(
                    browser,
                    "index.html",
                    "index",
                    label,
                    version,
                    full_page=False,
                )
        run_full = args.full_page or (not args.first_view)
        if run_full:
            viewports = ["desktop"]
            if args.viewport:
                viewports = [args.viewport]
            elif not args.first_view and not args.slugs and not args.slug:
                viewports = ["desktop"]
            for path, slug in pages:
                for label in viewports:
                    await capture_page(
                        browser, path, slug, label, version, full_page=True
                    )
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())