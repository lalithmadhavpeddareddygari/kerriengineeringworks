#!/usr/bin/env python3
"""Capture KEW page screenshots after scroll-triggering reveals and lazy images."""

from __future__ import annotations

import asyncio
from pathlib import Path

from playwright.async_api import async_playwright

BASE_URL = "http://127.0.0.1:8765"
OUT_DIR = Path("/opt/cursor/artifacts/kew-screenshots")
VERSION = "v6"

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


async def capture_page(browser, path: str, slug: str, label: str) -> None:
    context = await browser.new_context(
        viewport=VIEWPORTS[label],
        device_scale_factor=DESKTOP_CAPTURE_SCALE if label == "desktop" else 2,
    )
    page = await context.new_page()
    wait = "domcontentloaded" if slug == "contact" else "load"
    await page.goto(f"{BASE_URL}/{path}", wait_until=wait, timeout=90000)
    await page.wait_for_timeout(1200)
    await scroll_full_page(page)
    await wait_for_images(page)
    await scroll_full_page(page)
    await wait_for_images(page)
    out = OUT_DIR / f"{slug}-{label}-{VERSION}.png"
    await page.screenshot(path=str(out), full_page=True)
    await context.close()
    print(f"wrote {out}")


async def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for path, slug in PAGES:
            for label in VIEWPORTS:
                await capture_page(browser, path, slug, label)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())