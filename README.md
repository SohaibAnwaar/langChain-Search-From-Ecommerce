# Dentaltix Product Search - Backend

Backend for Dentaltix Product Search, a system for querying product information from the Dentaltix website.

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

<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.loom.com/share/20f9a3b333b94f0a9e5d8bcc657f76ef?sid=5662e18c-edd7-4836-95da-b948adfc0630" style="border: 1px solid black"></iframe>
