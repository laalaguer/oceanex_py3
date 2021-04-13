'''
Tests for personal methods.
'''

from oceanex_py3 import personal
from oceanex_py3 import public
from . import configuration

test_config = configuration.test_config
p = personal.Personal(test_config['uid'], test_config['apikey_id'], test_config['private_key_location'])

def test_accounts():
    accounts = p.get_accounts()
    assert len(accounts) != 0

def test_buy_status_cancel():
    ''' Test with the market '''
    # create a buy order, which is really low
    _, bids, _ = public.get_orderbook('ticvet', 10)
    lowest_buy_price = bids[0].price
    for each in bids:
        if each.price < lowest_buy_price:
            lowest_buy_price = each.price

    order1 = p.new_buy_limit_order('tic', 'vet', lowest_buy_price, 101/lowest_buy_price)
    assert order1 != None
    assert order1.price == lowest_buy_price

    # create a sell order.
    asks, _, _ = public.get_orderbook('vetbtc', 10)
    highest_sell_price = asks[0].price
    for each in asks:
        if each.price > highest_sell_price:
            highest_sell_price = each.price

    order2 = p.new_sell_limit_order('vet', 'btc', highest_sell_price, 10000)
    assert order2 != None
    assert order2.price == highest_sell_price

    # check the all the order status.
    m_orders = p.orders_status([order1.identifier, order2.identifier])
    assert m_orders[0].price == order1.price
    assert m_orders[1].price == order2.price

    # cancel orders
    assert p.cancel_orders([order1.identifier, order2.identifier]) == True
    # cancel all orders
    assert p.cancel_all_orders() == True