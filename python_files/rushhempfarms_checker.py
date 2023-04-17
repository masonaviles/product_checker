import requests
from bs4 import BeautifulSoup

# Set up the TextBelt API endpoint
url = 'https://textbelt.com/text'

# Replace the placeholder with your phone number
phone_number = '17064614265'

# Send a request to the product page and parse the HTML with BeautifulSoup
product_url = 'https://rushhempfarms.com/product/thca-badder-1g/'
response = requests.get(product_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Check if the product is in stock and set up the message accordingly
if "OUT OF STOCK" not in soup.get_text():
    message = "The product is in stock! Go to " + product_url + " to order now."
    response = requests.post(url, {
        'phone': phone_number,
        'message': message,
        'key': 'textbelt'  # Use 'textbelt' for the free tier
    })
    if response.json()['success']:
        print("Message sent!")
    else:
        print("Error sending message.")
else:
    print("The product is out of stock.")