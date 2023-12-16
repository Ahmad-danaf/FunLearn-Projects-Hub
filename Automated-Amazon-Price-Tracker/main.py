# Note, Amazon/camelcamelcamel will update it's website. So the CSS Selectors and XPATH may change. #
from notification_manager import NotificationManager
from bs4 import BeautifulSoup
import requests

# copy the product URL from Amazon and proceed to search it on https://camelcamelcamel.com/.
# Once you've found the relevant page, paste the URL you obtain below.
# FOR EXAMPLE: product_url = 'https://camelcamelcamel.com/product/B075CYMYK6'
product_url = 'https://camelcamelcamel.com/product/B075CYMYK6'

# Modify the BUY_PRICE variable to your desired price
BUY_PRICE = 100  # Replace with your desired price
 

header = { # i get the info from http://myhttpheader.com/
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6"
}


response = requests.get(product_url, headers=header)
soup= BeautifulSoup(response.text, 'xml')

try:
    price = float(soup.select_one("div.pwheader.amazon span.price").get_text().split("$")[1])
except:
    price = None
    title = None
else:
    try:
        title = soup.findAll('h2')[1].get_text()
    except:
        title = None

notification_manager = NotificationManager()

if price:
    if price < BUY_PRICE:
        if title:
            msg = f"{title} is now {price}"
            notification_manager.sent_mail(msg, product_url)
        else:
            print("Title is None")
            msg = f"Your product is now {price}"
            notification_manager.sent_mail(msg, product_url)
    else:
        print("Price is not lower than BUY_PRICE")
else:
    print("Price is None")