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

# def test_buy_status_cancel():
#     ''' Test with the market '''
#     # create a buy order, which is really low
#     _, bids, _ = public.get_orderbook('vthovet', 10)
#     lowest_buy_price = bids[0].price
#     for each in bids:
#         if each.price < lowest_buy_price:
#             lowest_buy_price = each.price

#     order1 = p.new_buy_limit_order('vtho', 'vet', lowest_buy_price, 101/lowest_buy_price)
#     assert order1 != None
#     assert order1.price == lowest_buy_price

#     # create a sell order.
#     asks, _, _ = public.get_orderbook('vetbtc', 10)
#     highest_sell_price = asks[0].price
#     for each in asks:
#         if each.price > highest_sell_price:
#             highest_sell_price = each.price

#     order2 = p.new_sell_limit_order('vet', 'btc', highest_sell_price, 10000)
#     assert order2 != None
#     assert order2.price == highest_sell_price

#     # check the all the order status.
#     m_orders = p.orders_status([order1.identifier, order2.identifier])
#     assert m_orders[0].price == order1.price
#     assert m_orders[1].price == order2.price

#     # cancel orders
#     assert p.cancel_orders([order1.identifier, order2.identifier]) == True
#     # cancel all orders
#     assert p.cancel_all_orders() == True

# def test_withdraw():
#     ''' Test withdraw VET to user's pocket,
#         You must have whitelisted below address in your ocean account
#     '''
#     receiver = '0x422D582C08d7965cD5Fefef1572faaA15783f473'
#     withdraw_order = p.withdraw(receiver, 'vet', 300, memo="Thanks to your work")
#     assert withdraw_order != None

def test_get_deposit_addresses():
    ''' Test deposit addresses for USDT and VET '''

    for x in ['BTC', 'VET', 'USDT']:
        addresses = p.get_deposit_addresses(x)
        assert len(addresses.resources) > 0

        for each in addresses.resources:
            print(each.currency_id)
            print(each.address)
            print(each.deposit_status)