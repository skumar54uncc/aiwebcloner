<div align="center">
  <h1 align="center">Orchids AI Website Cloner</h1>

  <p align="center">
    A high-fidelity website cloner that uses generative AI to replicate the aesthetics of any public website.
    <br />
    <a href="#about-the-project"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[[Product Screenshot]](https://drive.google.com/file/d/1p2TvO1LiHllE9pT875QKoVkHg3d9N1kt/view?usp=sharing)

I developed a full-stack application that leverages the power of generative AI to clone the visual aesthetics of any given website. This project goes beyond simple HTML scraping by using a multi-modal AI model to perform a deep visual analysis, resulting in a high-fidelity, static replica built from scratch with modern tools.

Here's why this approach is powerful:

* **It understands aesthetics, not just code:** By analyzing a screenshot, the AI can replicate visual details that are often difficult to extract from complex, minified CSS files.
* **Modern Tech Stack:** It regenerates websites using a clean, modern stack (Tailwind CSS), making the output easy to understand and maintain.
* **Handles Dynamic Content:** By using a headless browser (Playwright) to capture the final rendered state, it works on modern, JavaScript-heavy websites where the initial HTML is just a shell.

This project serves as a strong proof-of-concept for more advanced agentic AI systems in web design and development.

<p align="right">(<a href="#readme-toc">back to top</a>)</p>

### Built With

This project was built using a modern, robust tech stack:

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Tailwind][TailwindCSS]][Tailwind-url]
* [![Python][Python.org]][Python-url]
* [![FastAPI][FastAPI.tiangolo.com]][FastAPI-url]
* [![Gemini][Gemini.google.com]][Gemini-url]

<p align="right">(<a href="#readme-toc">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, please follow these simple steps.

### Prerequisites

Make sure you have the following software installed on your machine:
* **Node.js and npm:**
    ```sh
    npm install npm@latest -g
    ```
* **Python:** Version 3.8 or higher.
* **uv:** A fast Python package installer. If you don't have it, you can install it with pip:
    ```sh
    pip install uv
    ```

### Installation

1.  **Get a free Google Gemini API Key** at [https://aistudio.google.com/](https://aistudio.google.com/).

2.  **Clone the repo:**
    ```bash
    git clone https://github.com/skumar54uncc/aiwebclone.git
    cd aiwebclone
    ```

3.  **Setup the Backend:**
    * Create and activate a virtual environment (This is a best practice to keep project dependencies separate):
        ```sh
        # From the root directory of the project

        # On Windows:
        python -m venv venv
        .\venv\Scripts\activate

        # On macOS/Linux:
        python -m venv venv
        source venv/bin/activate
        ```
    * Install the required Python packages:
        ```sh
        pip install -r requirements.txt
        ```
    * Install the necessary browser binaries for Playwright:
        ```sh
        playwright install
        ```
    * Create a `.env` file and add your API key:
        ```
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```
    * Install Python packages using `uv`:
        ```sh
        uv sync
        ```
    

4.  **Setup the Frontend:**
    * In a new terminal, navigate to the `frontend` directory:
        ```sh
        cd frontend
        ```
    * Install NPM packages:
        ```sh
        npm install
        ```

<p align="right">(<a href="#readme-toc">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

To use the application, first start both the backend and frontend servers.

1.  **Run the Backend Server:**
    * In your backend terminal session, run:
        ```sh
        uvicorn app.main:app --reload

        or 

        python -m app.main
        ```

2.  **Run the Frontend Server:**
    * In your frontend terminal session, run:
        ```sh
        npm run dev
        ```

3.  **Open the Web App:**
    * Navigate to `http://localhost:3000` in your web browser.
    * Enter any public URL into the input field and click "Clone Website".
    * After a few moments, a preview of the cloned website will appear.

<p align="right">(<a href="#readme-toc">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

* [ ] **Implement a "Componentizer" Agent:** Deconstruct the page into smaller components (navbar, hero, footer) and have the AI clone each one individually for higher fidelity.
* [ ] **Develop an "Agentic Crawler":**
    * [ ] Add a Discovery Agent to find all internal links on a site.
    * [ ] Add a Link Rewriter Agent to create a fully navigable, multi-page offline clone.
* [ ] **Self-Correction Loop:** Add a second AI pass where the agent critiques its own work by comparing its clone's screenshot to the original, then refines the code automatically.

<p align="right">(<a href="#readme-toc">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Shailesh Kumar - shailesh.entrant@gmail.com

Project Link: [https://github.com/skumar54uncc/aiwebclone](https://github.com/[skumar54uncc]/[aiwebclone])

<p align="right">(<a href="#readme-toc">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

A few resources that were helpful in this project:

* [Google Gemini API](https://ai.google.dev/docs)
* [Playwright Documentation](https://playwright.dev/python/docs/intro)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Next.js Documentation](https://nextjs.org/docs)
* [Tailwind CSS](https://tailwindcss.com/docs)

<p align="right">(<a href="#readme-toc">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: https://i.imgur.com/your-demo.gif
[Next.js]: https://img.shields.io/badge/Next-black?style=for-the-badge&logo=next.js&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[TailwindCSS]: https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white
[Tailwind-url]: https://tailwindcss.com/
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[FastAPI.tiangolo.com]: https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white
[FastAPI-url]: https://fastapi.tiangolo.com/
[Gemini.google.com]: https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white
[Gemini-url]: https://ai.google.dev/
