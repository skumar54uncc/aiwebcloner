# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
import base64
from playwright.async_api import async_playwright
import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

# --- Configuration ---
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    print("Error: GOOGLE_API_KEY not found in .env file. Please set it.")
else:
    genai.configure(api_key=GOOGLE_API_KEY)

# --- FastAPI App Setup ---
app = FastAPI(title="Website Cloner API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Models ---
class CloneRequest(BaseModel):
    url: str

# --- Helper Functions ---

async def scrape_with_browser(url: str):
    """
    Uses Playwright to capture a FULL PAGE screenshot, final HTML, and primary font of a URL.
    """
    print(f"Scraping original website: {url}")
    async with async_playwright() as p:
        browser = None
        try:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            # Set a common viewport for consistency before taking a full-page screenshot
            await page.set_viewport_size({"width": 1920, "height": 1080})
            await page.goto(url, wait_until="load", timeout=60000)
            await page.wait_for_timeout(2000) # Let animations and lazy-loaded elements settle
            
            screenshot_bytes = await page.screenshot(type="png", full_page=True)
            screenshot_base64 = base64.b64encode(screenshot_bytes).decode('utf-8')
            
            html_content = await page.content()
            font_family = await page.evaluate("() => getComputedStyle(document.body).fontFamily")
            
            print(f"Scraping complete. Detected font: {font_family}")
            return (screenshot_base64, html_content, font_family)
        except Exception as e:
            error_message = f"Error scraping {url}: {str(e)}"
            print(error_message)
            return (None, f"<html><body><h1>Scraping Error</h1><p>{error_message}</p></body></html>", None)
        finally:
            if browser:
                await browser.close()

async def clone_with_llm(screenshot_base64: str, html_content: str, target_url: str, font_family: str):
    """
    Sends all available context to the LLM and asks for the highest-fidelity HTML clone.
    This version focuses the AI on a single task for maximum quality.
    """
    print(f"Generating high-fidelity clone for {target_url}...")

    # --- THE ULTIMATE HIGH-QUALITY PROMPT ---
    prompt = f"""
    You are a world-renowned digital forger and master of frontend engineering, tasked with a mission of the highest importance: to create a perfect, static replica of a webpage. Your analysis must be forensic, your execution flawless.

    **Primary Directive:**
    Your only task is to return a single block of perfect, production-ready HTML code. You must synthesize all provided context to create a clone that is perceptually indistinguishable from the original.

    **Full Context Dossier:**
    1.  **Target URL:** `{target_url}`. Use this URL to recall any specific knowledge you have about this domain, its typical frameworks, design systems, or brand guidelines. This is your primary anchor.
    2.  **Visual Evidence:** A full-page screenshot is provided. This is the ground truth for all visual and aesthetic details.
    3.  **Structural Data:** The original page's final DOM structure is provided for content and layout hints.
    4.  **Typographic Intel:** The primary computed font family has been detected as `{font_family}`.

    **The Canon of Perfection (Requirements for the HTML):**
    -   **Aesthetic & Structural Integrity:** Replicate the layout, colors, and typography with fanatical precision. This includes `letter-spacing`, `line-height`, `font-smoothing`, exact `box-shadows`, gradients, and element positioning.
    -   **Typography:** The primary font family is `{font_family}`. You MUST import this font from Google Fonts in the `<head>` if it's a known web font. Replicate all font weights and styles as seen in the screenshot.
    -   **Technology:** Use Tailwind CSS *exclusively*. Include the CDN script (`<script src="https://cdn.tailwindcss.com"></script>`).
    -   **Responsiveness:** The code must be production-grade and adapt perfectly to all viewports (`sm:`, `md:`, `lg:`).
    -   **Static Output:** The output must be pure HTML. No JavaScript, except for the Tailwind CDN.
    -   **Asset Replication:** Use `https://placehold.co/` for all images, matching dimensions from the screenshot. Recreate icons with inline SVG.

    **Output Format:**
    Your entire response MUST BE ONLY the complete HTML code, starting with `<!DOCTYPE html>` and ending with `</html>`. Do not include any other text, explanations, or markdown formatting like ```html ... ```.
    """
    
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    
    image_part = {"mime_type": "image/png", "data": screenshot_base64}
    text_part = f"Original DOM structure for reference:\n\n```html\n{html_content[:50000]}\n```" # Increased context
    
    try:
        response = await model.generate_content_async([prompt, image_part, text_part])
        
        # Clean the response to ensure it's just HTML
        cloned_html = response.text.strip()
        if cloned_html.startswith("```html"):
            cloned_html = cloned_html[7:]
        if cloned_html.endswith("```"):
            cloned_html = cloned_html[:-3]
        
        print("High-fidelity clone generated.")
        return cloned_html.strip()
        
    except Exception as e:
        error_message = f"An error occurred during LLM generation: {str(e)}"
        # For debugging, it's useful to see what the LLM responded with, if anything.
        raw_response = "No response object"
        if 'response' in locals() and hasattr(response, 'text'):
            raw_response = response.text
        print(f"LLM Raw Response Text: {raw_response}")
        return f"<html><body><h1>Cloning Error</h1><p>{error_message}</p></body></html>"

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Website Cloner API is running!"}
    
@app.post("/clone")
async def clone_website_endpoint(request: CloneRequest):
    try:
        # Step 1: Scrape the original website for all context
        original_screenshot_b64, original_html, font_family = await scrape_with_browser(request.url)
        if not original_screenshot_b64:
            return {"cloned_html": original_html}

        # Step 2: Generate the clone's HTML in a single, powerful pass
        final_html = await clone_with_llm(
            original_screenshot_b64,
            original_html,
            request.url,
            font_family
        )

        # Step 3: Return the final HTML
        return {"cloned_html": final_html}

    except Exception as e:
        error_message = f"A critical error occurred in the cloning workflow: {str(e)}"
        print(error_message)
        return {"cloned_html": f"<html><body><h1>Workflow Error</h1><p>{error_message}</p></body></html>"}

# --- Main Execution Block ---
if __name__ == "__main__":
    import uvicorn
    # This is the standard way to run for development
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
