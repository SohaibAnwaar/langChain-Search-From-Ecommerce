from langchain import OpenAI
from langchain.prompts import ChatPromptTemplate
import requests, os, webbrowser, subprocess
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer

os.environ['USER_AGENT'] = 'myagent'
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
# Define the task for the LLM
prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful assistant. Users will ask you to find products on the Dentaltix website. Extract the product type, brand preference, and any other preferences such as price from the user's input and construct a search URL. Ensure that the brand name's first letter is always capitalized.

    Example 1:
    User: I need latex gloves of brand Alle, my preference is the lowest price.
    Assistant: https://www.dentaltix.com/en/search-results?keyword=latex+gloves&Brand=Alle&_page=1&sort=price_asc

    Example 2:
    User: I need gloves of brand Alee product lowest price.
    Assistant: https://www.dentaltix.com/en/search-results?keyword=gloves&Brand=Alee&_page=1&sort=price_asc

    {input}
    """
)

llm = OpenAI(openai_api_key=openai_api_key, temperature=0.7)

# Transform user input into a search query
def generate_search_url(user_input):
    formatted_prompt = prompt.format(input=user_input)
    response = llm.generate([formatted_prompt])
    search_url = response.generations[0][0].text.strip()
    search_url = search_url.split('Assistant:')[-1].strip()
    return search_url

# Fetch and display results
def fetch_search_results(search_url):
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    products = []
    for product in soup.select('.product-listing .product-item'):
        name = product.select_one('.product-title').text.strip()
        price = product.select_one('.price').text.strip()
        products.append((name, price))
    
    return products

if __name__ == "__main__":
    user_input = input("Enter your product search query: ")
    search_url = generate_search_url(user_input)
    print(f"Search URL: {search_url}")

    try:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        # Open a new tab and navigate to the search URL
        driver.execute_script(f"window.open('{search_url}', '_blank');")

        # # Load HTML
        # loader = AsyncChromiumLoader([search_url])
        # html = loader.load()

        # # Transform
        # bs_transformer = BeautifulSoupTransformer()
        # docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["span"])
        # data = docs_transformed[0].page_content[0:500]
        # print(data)

        input("Press Enter to close the browser...")

        driver.quit()
    except Exception as e:
        print(str(e))

# Get search results
# search_results = fetch_search_results(search_url)
# for name, price in search_results:
#     print(f"Product: {name}, Price: {price}")
