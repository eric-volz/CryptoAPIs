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
    def get_price(symbol: str) -> float:
        """
        :param symbol: a Trading Pair like: BTCUSDT or ETHBTC
        :return: the current price of the given Trading Pair
        """
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        req = json.loads(requests.get(url).text)

        return float(req["price"])

    @staticmethod
    def get_percent_of_klines(symbol: str, interval: str) -> float:
        """
        :param symbol: a Trading Pair like: BTCUSDT or ETHBTC
        :param interval: type of candlestick pattern: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 1w
        :return: the percentage of how much the Trading Pair raised in a specific time
        """
        url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}"
        req = json.loads(requests.get(url).text)

        data = req[-1]
        return round(float(data[4]) / float(data[1]) - 1, 4)
