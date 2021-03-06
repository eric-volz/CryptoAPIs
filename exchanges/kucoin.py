import requests
import json


class KuCoin:
    @staticmethod
    def get_all_pairs() -> [str]:
        """
        :return: all Trading Pairs which are traded on the exchange
        """
        pairs = []
        url = "https://api.kucoin.com/api/v1/symbols"
        req = json.loads(requests.get(url).text)

        for pair in req["data"]:
            pairs.append(pair["symbol"])
        return sorted(pairs)

    @staticmethod
    def get_price(pair: str) -> float:
        """
        :param symbol: a Trading Pair like: BTC-USDT or ETH-BTC
        :return: the current price of the given Trading Pair
        """
        url = f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={pair}"
        req = json.loads(requests.get(url).text)

        return float(req["data"]["price"])

    @staticmethod
    def get_percent_of_klines(pair: str, interval: str) -> float:
        """
        :param symbol: a Trading Pair like: BTC-USDT or ETH-BTC
        :param interval: type of candlestick pattern: 1min, 3min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 8hour,
                                                      12hour, 1day, 1week
        :return: the percentage of how much the Trading Pair raised in a specific time
        """
        url = f"https://api.kucoin.com/api/v1/market/candles?type={interval}&symbol={pair}"
        req = json.loads(requests.get(url).text)

        data = req["data"][0]
        return round(float(data[2]) / float(data[1]) - 1, 4)