import requests
from bs4 import BeautifulSoup
from workers import send_text

# Replace the placeholder with your phone number
phone_number = '17064614265'

# Send a request to the product page and parse the HTML with BeautifulSoup
product_url = 'https://rushhempfarms.com/product/thca-badder-1g/'
response = requests.get(product_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Check if the product is in stock and send the message accordingly
if "OUT OF STOCK" not in soup.get_text():
    send_text(product_url, phone_number)
else:
    print("The product is out of stock.")