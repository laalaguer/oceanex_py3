''' Tests for public methods. '''
import time
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

    # Get the nearest 500 lines of JUR trades.
    all_trades = []
    trades = public.get_trades('jurvet', 20)
    assert len(trades) == 20
    for trade in trades:
        all_trades.append(trade)

    next_id = trades[-1].identifier
    while True:
        trades = public.get_trades('jurvet', 500, to_id=next_id)
        for trade in trades:
            all_trades.append(trade)
        if len(trades) == 500:
            next_id = trades[-1].identifier
            time.sleep(1)
            continue
        else:
            break