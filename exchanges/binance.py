import requests
import json


class Binance:
    @staticmethod
    def get_all_symbols() -> [str]:
        """
        :return: all Trading Pairs which are traded on the exchange
        """
        symbols = []
        url = "https://api1.binance.com/api/v3/exchangeInfo"
        req = json.loads(requests.get(url).text)

        for symbol in req["symbols"]:
            symbols.append(symbol["symbol"])
        return symbols

    @staticmethod
    def get_price(symbol) -> float:
        """
        :param symbol: a Trading Pair like: BTCUSDT or ETHBTC
        :return: the current price of the given Trading Pair
        """
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        req = json.loads(requests.get(url).text)

        return float(req["price"])
