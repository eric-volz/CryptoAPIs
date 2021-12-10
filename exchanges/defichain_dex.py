import requests
import json


class DefiChain_DEX:
    @staticmethod
    def get_all_pairs() -> [str]:
        """
        :return: all Trading Pairs which are traded on the exchange
        """
        url = "https://ocean.defichain.com/v0/mainnet/poolpairs"
        req = json.loads(requests.get(url).text)

        pairs = []

        for pair in req["data"]:
            pairs.append(pair["symbol"])
        return sorted(pairs)

    @staticmethod
    def get_price(price_pair: str):
        """
        :param price_pair: a Trading Pair like: BTC-USDT or ETH-BTC
        :return: the current price of the given Trading Pair
        """
        url = f"https://ocean.defichain.com/v0/mainnet/poolpairs"
        req = json.loads(requests.get(url).text)

        for pair in req["data"]:
            if pair["symbol"] == price_pair:
                return round(float(pair["priceRatio"]["ab"]), 3)
        return None

    @staticmethod
    def get_oracle_price(price_pair: str):
        """
        :param price_pair: a Trading Pair like: BTC-USDT or ETH-BTC
        :return: the current price of the given Trading Pair
        """
        url = f"https://ocean.defichain.com/v0/mainnet/prices"
        req = json.loads(requests.get(url).text)

        for pair in req["data"]:
            if pair["id"] == price_pair:
                return round(float(pair["price"]["aggregated"]["amount"]), 3)
        return None

    @staticmethod
    def get_percent_of_klines(pair: str, interval: str) -> float:
        """
        :param pair: a Trading Pair like: BTC-USDT or ETH-BTC
        :param interval: type of candlestick pattern: 1min, 3min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 8hour,
                                                      12hour, 1day, 1week
        :return: the percentage of how much the Trading Pair raised in a specific time
        """
        raise Exception("Not Supported")
