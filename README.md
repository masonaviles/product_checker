# product_checker
Product Checker is designed to check the availability of a particular product on a website and send a notification if the product is in stock. The bot uses the Requests library to send a GET request to the product page and the BeautifulSoup library to parse the HTML content of the page.

If the product is in stock, the bot sends a text message notification using the TextBelt API. The phone number to receive the notification is specified in the script. The script uses the TextBelt API key to authenticate and send the message. If the product is out of stock, the bot will simply print a message to the console.

The bot can be customized to check the availability of any product on any website. Simply update the product URL and phone number in the script to fit your needs. Additionally, the TextBelt API can be replaced with any other SMS API service, and the bot can be adapted to work with that service.

Overall, this bot is a useful tool for anyone who wants to stay informed about the availability of a particular product online. It can save time and effort by automatically checking for product availability, so you don't have to keep refreshing the product page manually.

## useage
- add scripts in `python_files` to check products
- each script is 1 website

## execution

`python 0_runner.py`
