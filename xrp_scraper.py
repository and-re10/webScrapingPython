# # All the imports
import requests
from bs4 import BeautifulSoup
# import urllib3
import smtplib
import time 
import os


# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# http = urllib3.PoolManager()
# response = http.request('GET', 'https://coinmarketcap.com/')
# https://coinmarketcap.com/
# URL = "https://coinmarketcap.com/currencies/xrp/"
# # File .zshrc
# user_agent = os.environ.get('USER_AGENT')
# headers = {
#     "user-agent": user_agent
# }
# page =  requests.get(URL, headers=headers)
# soup = BeautifulSoup(page.content, 'lxml')
# soup = str(soup)
# btc = soup[soup.find('Bitcoin'):]
# btc= btc[btc.find('Bitcoin'):btc.find('Bitcoin')+1300]
# btc_price = btc[btc.find('$')+50:]
# btc_price = btc_price[btc_price.find('$')+1:]
# btc_price = btc_price.replace('/', ' ')
# btc_price = btc_price.replace('>', ' ')
# btc_price = btc_price[:btc_price.find('a')]
# btc_prices = (btc_price.replace(',', ''))
# btc_prices = float(btc_prices.replace('<', ''))
# btc = soup[soup.find('Bitcoin'):]
# btc_price = soup.find(class_="price___3rj7O").get_text()
# ether_price = soup.find(class_="price___3rj7O ").get_text()
# time.sleep(10)
# btc = soup.find(class_="priceValue___11gHJ").get_text()
# sc-1q9q90x-0 iYFMbU h1___3QSYG
# sc-16r8icm-0 kXPxnI priceTitle___1cXUG
# priceValue___11gHJ
# print(btc)
# print(btc_price)
# print(ether_price)


crypto = input("Enter the crypto you want to search: ")

# # URL = 'https://coinmarketcap.com/fr/currencies/xrp/'
# URL ="https://blockfolio.com/coin/XRP"

URL = f"https://coinmarketcap.com/currencies/{crypto}/"


# # File .zshrc
user_agent = os.environ.get('USER_AGENT')

headers = {
    "user-agent": user_agent
}

def check_price(prices_array):

    page =  requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    time.sleep(2)

    # get the price from the website
    # price = soup.find("div", class_="priceValue___11gHJ").get_text().strip()
    # price = soup.find( class_="PriceFlasher__PriceFlasherBackground-sc-14r4saj-1 gvOhPv").get_text().strip()
    price = soup.find(class_="priceValue___11gHJ").get_text()
    # print(price)
    
    if "," in price:
        price = price.replace(',', '' )
        convert_price = float(price[1:7])
    else:
        convert_price = float(price[1:7])


    if len(prices_array) == 0:
        print(f"First loop")
    elif len(prices_array) > 0:
        if prices_array[-1] > convert_price:
            diff = (abs(prices_array[-1] - convert_price)*100)/prices_array[-1]
            print(f"The price feel down {str(diff)[0:4]}%")

        if prices_array[-1] == convert_price:
            print(f"Same price")

        elif prices_array[-1] < convert_price:
            diff = (abs(prices_array[-1] - convert_price)*100)/prices_array[-1]
            print(f"The price increased {str(diff)[0:4]}%")
    
    prices_array.append(convert_price)


    print(f"The price is {convert_price}")
    
    


prices = []
compt = 0
minute = 2
temps = 5 * (30*minute)
time_analyse = 0

while(compt < temps):
    
    check_price(prices)
    print(compt)
    compt += 1

    
    if compt == (30*minute) or compt == ((2*30)*minute) or compt == ((3*30)*minute) or compt == ((4*30)*minute):
        if prices[0] > prices[-1]:
            diff = (abs(prices[0] - prices[-1])*100)/prices[0]
            print(f'From the first price, it increased {str(diff)[0:4]}%')

        elif prices[0] < prices[-1]:
            diff = (abs(prices[0] - prices[-1])*100)/prices[0]
            print(f'From the first price, it fell down {str(diff)[0:4]}%')
        else:
            print('The price have not changed from the start')

if prices[0] > prices[-1]:
    diff = (abs(prices[0] - prices[-1])*100)/prices[0]
    print(f'From the first price, it increased {str(diff)[0:4]}%')

elif prices[0] < prices[-1]:
    diff = (abs(prices[0] - prices[-1])*100)/prices[0]
    print(f'From the first price, it fell down {str(diff)[0:4]}%')
else:
    print('The price have not changed from the start')

print("End of the Script")




