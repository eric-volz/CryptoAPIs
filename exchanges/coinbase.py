import cbpro


class Coinbase:
    @staticmethod
    def get_all_pairs() -> [str]:
        """
        :return: all Trading Pairs which are traded on the exchange
        """
        pairs = []
        client = cbpro.PublicClient()
        for pair in client.get_products():
            pairs.append(pair["id"])
        return sorted(pairs)

    @staticmethod
    def get_price(pair: str) -> float:
        """
        :param symbol: a Trading Pair like: BTC-USDT or ETH-BTC
        :return: the current price of the given Trading Pair
        """
        client = cbpro.PublicClient()
        return float(client.get_product_ticker(pair)["price"])

    @staticmethod
    def get_percent_of_klines(pair: str, interval: str) -> float:
        """
        :param symbol: a Trading Pair like: BTC-USDT or ETH-BTC
        :param interval: type of candlestick pattern: 1m, 5m, 15m, 1h, 6h, 8h, 1d
        :return: the percentage of how much the Trading Pair raised in a specific time
        """
        client = cbpro.PublicClient()
        if interval == "1m":
            interval = 60
        elif interval == "5m":
            interval = 300
        elif interval == "15m":
            interval = 900
        elif interval == "1h":
            interval = 3600
        elif interval == "6h":
            interval = 21600
        elif interval == "1d":
            interval = 86400
        req = client.get_product_historic_rates(pair, granularity=interval)
        data = req[0]

        return round(Coinbase.get_price(pair) / data[3] - 1, 4)
