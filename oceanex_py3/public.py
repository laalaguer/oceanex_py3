'''
Public API methods of Oceanex.

See https://api.oceanex.pro/doc/v1/
'''

URL = 'https://api.oceanex.pro/v1'
TIMEOUT = 15  # 15 seconds

import requests

class Market:
    '''
    What type of pairs that are supported in this current market.

    Attributes
    ----------
    left: `str`
        eg. 'BTC'
    right: `str`
        eg. 'USDT'
    identifier: `str`
        The identifier that you fill in when you query it with the exchange api. eg. `btcusdt`
    '''

    def __init__(self, left, right, identifier):
        self.left = left.upper()
        self.right = right.upper()
        self.identifier = identifier

    def __eq__(self, obj):
        return isinstance(obj, Market) and obj.left == self.left and self.right == obj.right and self.identifier == obj.identifier

def get_markets():
    ''' Query markets that this exchange supports.

    Returns
    -------
    markets
        A `list` of `Market` or `[]` if error occurs.

    '''

    url = URL + '/markets'
    
    r = requests.post(url, timeout=TIMEOUT)
  
    result = r.json()

    if result['code'] != 0:
        return []
    else:
        temp = []
        for pair in result['data']:
            left = pair['name'].split('/')[0]
            right = pair['name'].split('/')[1]
            m = Market(left, right, pair['id'])
            temp.append(m)
        return temp

class Order:
    '''
    Order in the order book.

    Attributes
    ----------
    price: float
        Price of the order
    volume: float
        Quantity of the order
    side: str
        'ask' or 'bid' or 'unknown'
    '''
    def __init__(self, price, volume, side):
        self.price = float(price)
        self.volume = float(volume)
        if side.lower() == 'ask':
            self.side = 'ask'
        elif side.lower() == 'bid':
            self.side = 'bid'
        else:
            self.side = 'unknown'

def get_orderbook(market, limit):
    ''' Get the current orderbook in market and limit results
    Parameters
    ----------
    market: str
        The market identifier used to query against exchages.
    
    limit: int
        The result limit in lines.
    
    Returns
    -------
    
    asks
        A `list` of `Order`, `[]` if a logic error occurs.
    
    bids
        A `list` of `Order`, `[]` if a logic error occurs.

    timestamp
        A unix timestamp in int, `0` if a logic error occurs.
    '''

    url = URL + '/order_book'
    data = {
        "market": market,
        "limit": limit
    }

    r = requests.post(url, data, timeout=TIMEOUT)
    result = r.json()

    if result['code'] != 0:
        return [], [], 0
    else:
        asks = [Order(x[0], x[1], 'ask') for x in result['data']['asks']]
        bids = [Order(x[0], x[1], 'bid') for x in result['data']['bids']]
        timestamp = int(result['data']['timestamp'])

        return asks, bids, timestamp

class Trade:
    ''' The trade that is completed on the open market.

    Attributes
    ----------
    identifier: int
        order number
    price: float
        price of the order
    volume: float
        volume of the order
    funds: float
        price x volume = funds, the amount user paid for completing the order
    created_on: int
        unix timestamp of when it is created
    side: str
        'ask' or 'bid' or 'unknown'
    '''
    def __init__(self, identifier, price, volume, funds, created_on, side):
        self.identifier = identifier
        self.price = float(price)
        self.volume = float(volume)
        self.funds = float(funds)
        self.created_on = int(created_on)
        if side.lower() == 'ask':
            self.side = 'ask'
        elif side.lower() == 'bid':
            self.side = 'bid'
        else:
            self.side = 'unknown'

def get_trades(market, limit=0, from_id=0, to_id=0):
    '''
    Gets the trades that completed in the market.

    Parameters
    ----------

    market: str
        The identifier used to call the api, eg. 'btcusdt'
    
    limit: int
        Limit the results.

    from_id: int
        Limit the results to be after trade id.
    
    to_id: int
        Limit the results to be before the trade id.

    Returns
    -------
    trades
        A `list` of `Trade`, `[]` if logic error occurs.
    
    '''
    url = URL + '/trades'

    data = {
        "market": market
    }

    if limit:
        data['limit'] = limit

    if from_id:
        data['from'] = from_id
    
    if to_id:
        data['to'] = to_id

    r = requests.post(url, data=data, timeout=TIMEOUT)
    result = r.json()

    if result['code'] != 0:
        return []
    else:
        return [ Trade(x['id'], x['price'], x['volume'], x['funds'], x['created_on'], x['side']) for x in result['data'] ]