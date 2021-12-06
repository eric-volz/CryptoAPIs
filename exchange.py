from .exchanges import Binance, Coinbase, KuCoin, DefiChain_DEX


def get_exchange(exchange: str):
    if exchange == 'binance':
        return Binance
    elif exchange == 'coinbase':
        return Coinbase
    elif exchange == 'kucoin':
        return KuCoin
    elif exchange == 'defichain_dex':
        return DefiChain_DEX
    else:
        raise Exception(f"The exchange {exchange} existiert nicht!")


def get_day_percent_of_kline(exchange, pair):
    obj_exchange = get_exchange(exchange)
    if exchange == 'binance' or exchange == 'coinbase':
        return obj_exchange.get_percent_of_klines(pair, '1d')
    elif exchange == 'kucoin':
        return obj_exchange.get_percent_of_klines(pair, '1day')
    elif exchange == 'defichain_dex':
        raise Exception("Not Supported")

