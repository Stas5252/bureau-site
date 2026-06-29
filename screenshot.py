import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        
        # We need absolute path for file URL
        path = os.path.abspath("index.html").replace('\\', '/')
        await page.goto(f"file:///{path}")
        
        # Take a full page screenshot
        await page.screenshot(path="full_page.jpg", full_page=True)
        print("Screenshot saved to full_page.jpg")
        await browser.close()

asyncio.run(main())
