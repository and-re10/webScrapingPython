from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time 
import string
import re # Regex
import os
PATH = os.environ.get('PATH_CHROME_DRIVER')

driver = webdriver.Chrome(PATH)

driver.get(f"https://www.amazon.fr/")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price 

def search_products(prducts_array):
    # Find the input to search a product
    search = driver.find_element(By.ID, "twotabsearchtextbox")
    print(search.text)
    # Write the product inside the serach bar
    search_value = input("Qual o produto quer procurar?")
    search.send_keys(search_value)
    # Press the key enter to search the procuct
    search.send_keys(Keys.ENTER)
    # Get the current url
    currentURL = driver.current_url;
    print(currentURL)
    
    # Product_Name a-section a-spacing-none a-spacing-top-small // et // a-size-base-plus a-color-base a-text-normal
    products_name = driver.find_elements(By.CLASS_NAME, 'a-size-base-plus')
     # Product_Price a-price-whole
    products_price = driver.find_elements(By.CLASS_NAME, 'a-price-whole')
    compt = 0
    min_price = float(input("Qual o valor minimo do produto? "))
    max_price = float(input("Qual o valor maximo do produto? "))
    # print(convert_price)
    while compt < len(products_price):
        if products_price[compt]:
            convert_price = products_price[compt].text.strip().replace(",", ".")
            convert_price = re.sub(r"\s+", "", convert_price)
            print(convert_price)
            convert_price = float(convert_price)
            # print(convert_price)

            convert_price = float(convert_price)
            if products_name[compt] and (convert_price >= min_price) and (convert_price <= max_price):
                product = Product(products_name[compt].text, convert_price)
                prducts_array.append(product)

        compt += 1
   

products = []
time.sleep(5)
search_products(products)
for product in products:
    print("Name: " + product.name + "\n" + "Price: ",product.price)



driver.quit()