import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get the ratio of price_a to price_b """
    if price_b == 0:
        return "NaN"
    return price_a / price_b


# Main
if __name__ == "__main__":
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        # Store prices in a dictionary
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        # Calculate the ratio using the actual prices
        if "ABC" in prices and "DEF" in prices:
            print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))
        else:
            print("Stock data for ABC or DEF is missing.")
