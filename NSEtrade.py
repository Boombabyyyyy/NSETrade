# Imports
from urllib.error import HTTPError, URLError
from nsetools import Nse
import time
nse = Nse()

# Function that fetches stock price
def get_current_price(scrip):
        q = nse.get_quote(scrip)['lastPrice']
        print(q)

# Driver code with error handling
print("Please enter the unique stock scrip for the company you're looking to trade:")
stock = input()
while True:
    try:
        get_current_price(stock)
        time.sleep(5)
    except HTTPError:
        print("Something went wrong, please try again later!")
        break
    except URLError:
        print("Please check your internet connection and retry!")
        break
    except TypeError:
        print("No such stock exists, please enter a valid Scrip and retry")
        break


