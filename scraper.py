# All the imports
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import os



# Link to the page who we want to scrap
URL = 'https://www.amazon.fr/Harry-Potter-lInt%C3%A9grale-Sorciers-Rowling/dp/B00K3OM4E8/ref=zg_bs_dvd_home_1?_encoding=UTF8&psc=1&refRID=AKE44HM37KJEZ73FJN7M'

# User Agent of the PC ( you can find typing on Google Search "my user agent") 

user_agent = os.environ.get('USER_AGENT')

headers = {
    "user-agent": user_agent
}


def check_price(prices_array):

    # make the request to the url
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # get the title of the product via id
    # title = soup.find(id="productTitle").get_text().strip()
    # get the price of the procuct via id
    price = soup.find(id="priceblock_ourprice").get_text().strip()
    
    # Verifcation of the price and convert the string to float
    # Check if the price contains a comma instead of a period
    if "," in price[0:5]:
        # Replace the comme to a period
        convert_price = price[0:5].replace(",", ".")
        # Convert to float
        convert_price = float(convert_price)
    else :
        # Convert to a float
        convert_price = float(price[0:5])

    # Checking if the price 
    if len(prices_array) == 1:
        if prices_array[0] > convert_price:
            # Get the percentage of the increase or decrease of the price
            diff = round((abs(round(prices_array[0] - convert_price))*100)/round(prices_array[0]))
            print(f"Price feel down {diff}%")
            # send_mail()
        elif prices_array[0] == convert_price :
            # Get the percentage of the increase or decrease of the price
            diff = round((abs(round(prices_array[0] - convert_price))*100)/round(prices_array[0]))
            print(f"Same price {convert_price}€")
        else :
            # Get the percentage of the increase or decrease of the price
            diff = round((abs(round(prices_array[0] - convert_price))*100)/round(prices_array[0]))
            print(f"The price increased {diff}%")
    elif len(prices_array) > 1:
        if prices_array[-1] > convert_price:
            # Get the percentage of the increase or decrease of the price
            diff = round((abs(round(prices_array[-1] - convert_price))*100)/round(prices_array[-1]))
            print(f"Price feel down {diff}%")
            # send_mail()
        elif prices_array[-1] == convert_price :
            # Get the percentage of the increase or decrease of the price
            diff = round((abs(round(prices_array[-1] - convert_price))*100)/round(prices_array[-1]))
            print(f"Same price {convert_price}€")
        else :
            # Get the percentage of the increase or decrease of the price
            diff = round((abs(round(prices_array[-1] - convert_price))*100)/round(prices_array[-1]))
            print(f"The price increased {diff}%")

    # Add the price to the array
    prices_array.append(convert_price)

    # print(title)
    print(convert_price)



def send_mail(email, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.strattls()
    server.ehlo()

    email = os.environ.get('USER_EMAIL')
    password = os.environ.get('USER_PASSWORD')

    server.login(email, password)

    subject = 'Price feel down!'
    body = f"Check the amazon link {URL}"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        email,
        'other mail',
        msg
    )
    print("HEY EMAIL HAS BEEN SENT")

    server.quit()

compt_loop = 1
first_price = 14.00
prices = [first_price]
while(compt_loop < 4):
    # print(prices)
    check_price(prices)
    compt_loop += 1
    time.sleep(2)

print("Finish scraping for today")

