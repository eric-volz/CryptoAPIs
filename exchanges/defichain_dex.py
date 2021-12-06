import requests
import json


class DefiChain_DEX:
    @staticmethod
    def get_all_pairs() -> [str]:
        """
        :return: all Trading Pairs which are traded on the exchange
        """
        pairs = []
        url = "https://api.defichain.io/v1/listpoolpairs"
        req = json.loads(requests.get(url).text)

        pairs = []

        for key in req:
            pairs.append(req[key]["symbol"])
        return sorted(pairs)

    @staticmethod
    def get_price(pair: str) -> float:
        """
        :param symbol: a Trading Pair like: BTC-USDT or ETH-BTC
        :return: the current price of the given Trading Pair
        """
        url = f"https://api.defichain.io/v1/listswaps"
        req = json.loads(requests.get(url).text)

        split = pair.split("-")
        pair = split[0] + "_" + split[1]
        print(pair)

        price = float(req[pair]['last_price'])
        return round(price, 3)

    @staticmethod
    def get_percent_of_klines(pair: str, interval: str) -> float:
        """
        :param symbol: a Trading Pair like: BTC-USDT or ETH-BTC
        :param interval: type of candlestick pattern: 1min, 3min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 8hour,
                                                      12hour, 1day, 1week
        :return: the percentage of how much the Trading Pair raised in a specific time
        """
        raise Exception("Not Supported")
