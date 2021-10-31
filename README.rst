oceanex_py3
===========
oceanex_py3 is a Python SDK to query, trade and manage funds on Oceanex.

Installation
------------

.. code-block:: bash

   pip3 install oceanex_py3

Source Code
------------

https://github.com/laalaguer/oceanex_py3

Documentation
-------------

See `/docs` for detailed APIs.

Examples
-------------

Get all trading pairs supported on Oceanex.

.. code-block:: python

   from oceanex_py3 import public
   
   markets = public.get_markets()
   
   for each in markets:
       print(each.identifier, each.left, each.right)
   
   # etcusdt ETC USDT
   # ltcusdt LTC USDT
   # dashusdt DASH USDT


Get current buy/sell orderbook status on the market.

.. code-block:: python

   from oceanex_py3 import public
   
   asks, bids, timestamp = public.get_orderbook('btcusdt', 10) # limit result to 10 orders.


Post an order to the market on behalf of user.

.. code-block:: python

   from oceanex_py3 import personal
   
   test_config = {
       'uid': 'IDxxxxx',
       'apikey_id': 'Kxxxxxxx',
       'private_key_location': '/xxx/xxx/xxx/key.pem'
   }
   
   p = personal.Personal(
       test_config['uid'],
       test_config['apikey_id'],
       test_config['private_key_location']
   )
   
   order = p.new_sell_limit_order('vet', 'btc', 600000, 10000)


Cancel all the orders.

.. code-block:: python

   from oceanex_py3 import personal
   
   test_config = {
       'uid': 'IDxxxxx',
       'apikey_id': 'Kxxxxxxx',
       'private_key_location': '/xxx/xxx/xxx/key.pem'
   }
   
   p = personal.Personal(
       test_config['uid'],
       test_config['apikey_id'],
       test_config['private_key_location']
   )
   
   p.cancel_all_orders()
