# Dentaltix Product Search - Backend

<div>
    <a href="https://www.loom.com/share/d05b237659a0494f814b116921c55c77">
      <p>Code - make_url.py — TGL - 23 July 2024 - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/d05b237659a0494f814b116921c55c77">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/20f9a3b333b94f0a9e5d8bcc657f76ef-41f05647d0bf8ff4-full-play.gif">
    </a>
  </div>
  
### Required Versions and Packages
- Python 3.12 or higher
- LangChain (latest version)
- OpenAI API key
- Chrome WebDriver (managed by webdriver-manager)

### Installation Steps
To run this application locally, follow these steps:

1. **Clone the repository:**
```
git clone https://github.com/yourusername/dentaltix-product-search.git
cd dentaltix-product-search
```

2. **Create and activate a virtual environment:**

```bash
python3 -m venv env
source env/bin/activate
```

### Install the required packages:

```bash
pip install -r requirements.txt
```
### Then run manullay this command on terminal:
```
playwright install

```

### Set up environment variables:

```
Copy .env-example to .env and add your OpenAI API key.
cp .env-example .env
Edit .env to include your OpenAI API key:
nano .env
# Add the line: OPENAI_API_KEY=your_openai_api_key_here
```

### Run the application:
```
Execute the script to start processing user input and open the search URL in a new browser tab:
python3 make_url.py
```

### Input Data:

When prompted, enter your product search query in the terminal. For example:

- I need gloves of brand Blossom
The application will generate a search URL and open it in a new Chrome tab.

### Loom Video
For a detailed walkthrough of the project and setup instructions, check out the Loom video:


