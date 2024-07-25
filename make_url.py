import time, json
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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import constant

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
def fetch_search_results(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "products-search-results"))
    )

    # Wait for the products to be rendered within the div
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[1]/section[2]/div[2]/main/div/div[1]/div/div/div/div/div[2]/div'))
    )

    products = []
    # Extract product details for the first three products
    for i in range(2, 5):
        try:
            url_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, constant.url_xpath_for_templete.format(i)))
            )
            url = url_element.get_attribute('href')
            # url.append(url)

            product_name_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, constant.product_name_xpath_template.format(i)))
            )
            name = product_name_element.text

            price_xpath = constant.product_price_xpath_templates[i - 2]

            # Wait for the product price element to be present
            product_price_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, price_xpath))
            )
            price = product_price_element.text

            rating_xpath = constant.rating_xpaths[i - 2]
            rating_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, rating_xpath))
            )
            rating = rating_element.text

            product_data = {
                "Product Name": name,
                "Price": price,
                "Url": url,
                "Rating": rating
            }

            # Append the product data to the list
            products.append(product_data)
        except Exception as e:
            print(f"Error extracting product {i-2}: {str(e)}")

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

        # Open the Dentaltix search results page
        driver.get(search_url)
        products = fetch_search_results(driver)
        

        # driver.execute_script(f"window.open('{search_url}', '_blank');")
        # Switch to the new tab

        # Load HTML
        # loader = AsyncChromiumLoader([search_url])
        # html = loader.load()
        # print(html)

        # # Transform
        # bs_transformer = BeautifulSoupTransformer()
        # docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["href"])
        # data = docs_transformed[0]#.page_content[0:500]
        # print(data)
        with open('products.json', 'w') as json_file:
            json.dump(products, json_file, indent=4)

        print("Data saved to products.json")
        input("Press Enter to close the browser...")

    except Exception as e:
        print(str(e))