''' Tests for public methods. '''

from oceanex_py3 import public

def test_markets():
    m = public.Market('btc', 'usdt', 'btcusdt')
    assert m in public.get_markets()

def test_orderbook():
    asks, bids, timestamp = public.get_orderbook('btcusdt', 10)

    assert len(asks) == 10
    assert len(bids) == 10
    assert type(timestamp) == int

def test_non_exist_orderbook():
    asks, bids, timestamp = public.get_orderbook('vvvusdt', 10)

    assert len(asks) == 0
    assert len(bids) == 0
    assert timestamp == 0

def test_trade():
    trades = public.get_trades('btcusdt', 20)
    assert len(trades) == 20
