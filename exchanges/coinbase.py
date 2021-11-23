import cbpro


class Coinbase:
    @staticmethod
    def get_all_symbols() -> [str]:
        """
        :return: all Trading Pairs which are traded on the exchange
        """
        symbols = []
        client = cbpro.PublicClient()
        for symbol in client.get_products():
            symbols.append(symbol["id"])
        return sorted(symbols)


    @staticmethod
    def get_price(symbol) -> float:
        """
        :param symbol: a Trading Pair like: BTC-USDT or ETH-BTC
        :return: the current price of the given Trading Pair
        """
        client = cbpro.PublicClient()
        return float(client.get_product_ticker(symbol)["price"])
