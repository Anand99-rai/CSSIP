import requests
from bs4 import BeautifulSoup

# URL of the finance website (example: Yahoo Finance)
url = "https://finance.yahoo.com/quote/AAPL/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Search for the price using more general tags
    stock_price = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})
    
    if stock_price:
        stock_price = stock_price.text
    else:
        stock_price = "Stock price not found"

    # Search for the stock name more generally
    stock_name = soup.find("h1")
    
    if stock_name:
        stock_name = stock_name.text
    else:
        stock_name = "Stock name not found"
    
    # Display the stock name and price
    print(f"{stock_name} Current Price: ${stock_price}")
else:
    print("Failed to retrieve data from the website.")
