import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        self.assertEqual(stock, 'ABC')
        self.assertEqual(bid_price, 120.48)
        self.assertEqual(ask_price, 121.2)
        self.assertEqual(price, (120.48 + 121.2) / 2)  # Average of bid and ask

        stock, bid_price, ask_price, price = getDataPoint(quotes[1])
        self.assertEqual(stock, 'DEF')
        self.assertEqual(bid_price, 117.87)
        self.assertEqual(ask_price, 121.68)
        self.assertEqual(price, (117.87 + 121.68) / 2)  # Average of bid and ask

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 120.2, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 122.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        self.assertEqual(stock, 'ABC')
        self.assertEqual(bid_price, 120.48)
        self.assertEqual(ask_price, 119.2)
        self.assertEqual(price, (120.48 + 119.2) / 2)  # Average of bid and ask

        stock, bid_price, ask_price, price = getDataPoint(quotes[1])
        self.assertEqual(stock, 'DEF')
        self.assertEqual(bid_price, 122.87)
        self.assertEqual(ask_price, 120.2)
        self.assertEqual(price, (122.87 + 120.2) / 2)  # Average of bid and ask

    def test_getDataPoint_zeroBidOrAskPrice(self):
        quotes = [
            {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        self.assertEqual(stock, 'ABC')
        self.assertEqual(bid_price, 120.48)
        self.assertEqual(ask_price, 0)
        self.assertEqual(price, (120.48 + 0) / 2)  # Average of bid and ask when ask price is 0

        stock, bid_price, ask_price, price = getDataPoint(quotes[1])
        self.assertEqual(stock, 'DEF')
        self.assertEqual(bid_price, 0)
        self.assertEqual(ask_price, 121.68)
        self.assertEqual(price, (0 + 121.68) / 2)  # Average of bid and ask when bid price is 0

    def test_getDataPoint_largeNumbers(self):
        quotes = [
            {'top_ask': {'price': 10000.0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 10500.0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 12000.0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 11800.0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        self.assertEqual(stock, 'ABC')
        self.assertEqual(bid_price, 10500.0)
        self.assertEqual(ask_price, 10000.0)
        self.assertEqual(price, (10500.0 + 10000.0) / 2)  # Average of large bid and ask

        stock, bid_price, ask_price, price = getDataPoint(quotes[1])
        self.assertEqual(stock, 'DEF')
        self.assertEqual(bid_price, 11800.0)
        self.assertEqual(ask_price, 12000.0)
        self.assertEqual(price, (11800.0 + 12000.0) / 2)  # Average of large bid and ask

if __name__ == '__main__':
    unittest.main()
