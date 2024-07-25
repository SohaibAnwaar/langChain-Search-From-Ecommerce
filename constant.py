# Define the product elements' XPath
product_name_xpath_template = '/html/body/div[1]/div[1]/section[2]/div[2]/main/div/div[1]/div/div/div/div/div[2]/div[{}]/div/a/strong'
# product_price_xpath_template = '/html/body/div[1]/div[1]/section[2]/div[2]/main/div/div[1]/div/div/div/div/div[2]/div[{}]/div[2]/div[2]/p/del'
product_price_xpath_templates = [
'/html/body/div[1]/div[1]/section[2]/div[2]/main/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/p', 
'/html/body/div[1]/div[1]/section[2]/div[2]/main/div/div[1]/div/div/div/div/div[2]/div[3]/div[2]/div[2]/p',
'/html/body/div[1]/div[1]/section[2]/div[2]/main/div/div[1]/div/div/div/div/div[2]/div[4]/div[2]/div[2]/p'
]
rating_xpaths = [
    "/html/body/div[1]/div[1]/section[2]/div[2]/main/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/span",
    "/html/body/div[1]/div[1]/section[2]/div[2]/main/div/div[1]/div/div/div/div/div[2]/div[3]/div[2]/div[2]/div/span",
    "/html/body/div[1]/div[1]/section[2]/div[2]/main/div/div[1]/div/div/div/div/div[2]/div[4]/div[2]/div[2]/div/span"
]
url_xpath_for_templete='/html/body/div[1]/div[1]/section[2]/div[2]/main/div/div[1]/div/div/div/div/div[2]/div[{}]/div/a'