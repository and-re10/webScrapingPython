# Import Selenium -> pip3 install selenium
# Download Google Chrome driver
# Paste the drive in Applications Folder (non de chemin option + edit )
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
PATH = os.environ.get('PATH_CHROME_DRIVER')

driver = webdriver.Chrome(PATH)

driver.get(f"https://coinmarketcap.com/fr/")

def get_currencys(currency_array):

    names = driver.find_elements(By.CLASS_NAME, 'iJjGCS')

    compt = 0
    for name in names:
        compt += 1
        currency_array.append(name.text)
        print(compt, " ", name.text)
    
    # print(currency_array)
    # print(len(currency_array))

# Prendre toutes les cryptos sur coin market cap
compt_scroll = 0
scroll_diff = 1000
while compt_scroll < 9100:  
    driver.execute_script(f"window.scrollTo(0, {compt_scroll})") 
    time.sleep(1)
    compt_scroll += 1000
# Array pour les cryptos
cryptos = []
get_currencys(cryptos)

crypto = input("Enter the crypto you want to search: ")

driver.get(f"https://coinmarketcap.com/fr/currencies/{crypto}/")
# print(driver.title)

time.sleep(10)

def get_price(prices_array):
    # cibler le prix de la crypto
    price = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div').text

    # enlever la virgule pour pouvoir convertir en nombre decimal
    if "," in price:
        price = price.replace(",", "")
        convert_price = float(price[1:7])
    else :
        convert_price = float(price[1:7])
    

    
    # Verifier s'il existe deja des prix dans l'array
    if len(prices_array) == 0:
        # Premier loop si l'array est vide
        print(f"First loop 0%")
    elif len(prices_array) > 0:
        if prices_array[0] > convert_price:
            diff_total = -((abs(prices_array[0] - convert_price)*100)/prices_array[0])
            diff_total = str(diff_total)[0:5]
        elif prices_array[0] <= convert_price:
            diff_total = +((abs(prices_array[0] - convert_price)*100)/prices_array[0])
            diff_total = str(diff_total)[0:4]
            
        # Autres loops s'il exsite 1 ou plus prix dans l'array
        if prices_array[-1] > convert_price:
            # Condition pour montrer que le prix a baissé
            diff = (abs(prices_array[-1] - convert_price)*100)/prices_array[-1]
            print(f"The price feel down {str(diff)[0:4]}%. Total {diff_total}%")

        if prices_array[-1] == convert_price:
            # Condition pour montrer que le prix est le meme
            print(f"Same price. Total {diff_total}%")

        elif prices_array[-1] < convert_price:
             # Condition pour montrer que le prix a augmenté
            diff = (abs(prices_array[-1] - convert_price)*100)/prices_array[-1]
            print(f"The price increased {str(diff)[0:4]}%. Total {diff_total}%")
    
    # Ajouter le nouveau prix a l'array
    prices_array.append(convert_price)

    # Afficher le dernier prix
    print(f"The price is {convert_price}")


# Compteur pour la boucle
compt = 0
# Array pour garder les prix 
prices = []
# Time to execute the code
timer = 60*1
# Boucle while pour executer la function plusieurs fois
while compt < timer:
    get_price(prices)
    time.sleep(1)
    compt += 1

# Faire l'evaluation entre le premier prix et le dernir
if prices[0] > prices[-1]:
    diff = (abs(prices[0] - prices[-1])*100)/prices[0]
    print(f'From the first price, it fell down {str(diff)[0:4]}%')

elif prices[0] < prices[-1]:
    diff = (abs(prices[0] - prices[-1])*100)/prices[0]
    print(f'From the first price, it increased {str(diff)[0:4]}%')
else:
    print('The price have not changed from the start')

# Fermer le browser
driver.quit()