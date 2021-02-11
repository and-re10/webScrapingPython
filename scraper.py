# All the imports
import requests
from bs4 import BeautifulSoup
import os



# Link to the page who we want to scrap
URL = 'https://www.amazon.fr/Harry-Potter-lInt%C3%A9grale-Sorciers-Rowling/dp/B00K3OM4E8/ref=zg_bs_dvd_home_1?_encoding=UTF8&psc=1&refRID=AKE44HM37KJEZ73FJN7M'

# User Agent of the PC ( you can find typing on Google Search "my user agent") 

user_agent = os.environ.get('USER_AGENT')

headers = {
    "user-agent": user_agent
}

