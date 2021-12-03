import requests
import json


class Binance:
    @staticmethod
    def get_all_pairs() -> [str]:
        """
        :return: all Trading Pairs which are traded on the exchange
        """
        pairs = []
        url = "https://api1.binance.com/api/v3/exchangeInfo"
        req = json.loads(requests.get(url).text)

        for pair in req["symbols"]:
            pairs.append(pair["symbol"])
        return sorted(pairs)

    @staticmethod
    def get_price(pair: str) -> float:
        """
        :param symbol: a Trading Pair like: BTCUSDT or ETHBTC
        :return: the current price of the given Trading Pair
        """
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={pair}"
        req = json.loads(requests.get(url).text)

        return float(req["price"])

    @staticmethod
    def get_percent_of_klines(pair: str, interval: str) -> float:
        """
        :param symbol: a Trading Pair like: BTCUSDT or ETHBTC
        :param interval: type of candlestick pattern: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 1w
        :return: the percentage of how much the Trading Pair raised in a specific time
        """
        url = f"https://api.binance.com/api/v3/klines?symbol={pair}&interval={interval}"
        req = json.loads(requests.get(url).text)

        data = req[-1]
        return round(float(data[4]) / float(data[1]) - 1, 4)
