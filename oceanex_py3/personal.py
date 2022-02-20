'''
Personal API methods of Oceanex. Requires authentication.

See https://api.oceanex.pro/doc/v1/
'''
import jwt
import requests

URL = 'https://api.oceanex.pro/v1'
TIMEOUT = 15  # 15 seconds

class Personal:
    def __init__(self, uid, apikey_id, private_key_location):
        self.uid = uid
        self.apikey_id = apikey_id
        with open(private_key_location, 'rb') as private_file:
            self.private_key = private_file.read()
    
    def _build_data(self, data):
        ''' Build the data to be sent to the requests.data part '''
        payload = {
            'uid': self.uid,
            'apikey_id': self.apikey_id,
            'data': data
        }

        jwt_token = jwt.encode(payload, self.private_key, algorithm="RS256")

        body = {
            'user_jwt': jwt_token
        }

        return body
    
    def get_accounts(self):
        ''' Get the wallets of a single user.

        Returns
        -------

        wallets
            A `list` of `Account`
        '''
        url = URL + '/members/me'
        data = {}
        data = self._build_data(data)
        r = requests.post(url, data=data, timeout=TIMEOUT)
        result = r.json()

        if result['code'] != 0:
            return []
        else:
            return [ Account(x['currency'], x['balance'], x['locked']) for x in result['data']['accounts'] ]
    
    def _new_limit_order(self, left, right, price, volume, buy_or_sell='buy'):
        ''' Creates a limit order, either buy or sell
        '''

        side = buy_or_sell

        market = left.lower() + right.lower()
        volume = str(volume)
        price = str(price)
        ord_type = 'limit'

        url = URL + '/orders'
        data = {
            'market': market,
            'side': side,
            'volume': volume,
            'price': price,
            'ord_type': ord_type
        }

        data = self._build_data(data)

        r = requests.post(url, data=data, timeout=TIMEOUT)
        result = r.json()

        if result['code'] != 0:
            return None
        else:
            return UserOrder(
                result['data']['remaining_volume'],
                result['data']['price'],
                result['data']['created_on'],
                result['data']['side'],
                result['data']['volume'],
                result['data']['state'],
                result['data']['ord_type'],
                result['data']['avg_price'],
                result['data']['executed_volume'],
                result['data']['id'],
                result['data']['market']
            )


    def new_buy_limit_order(self, left, right, price, volume):
        ''' Create a buy limit order.

        Parameters
        ----------

        left: str
            eg. 'vet'

        right: str
            eg. 'usdt'
        
        price: float
            eg. 10.1
        
        volume: float
            eg. 101

        Returns
        -------
        order
            A `UserOrder` or None if operation failed.
        '''

        return self._new_limit_order(left, right, price, volume, buy_or_sell='buy')

    def new_sell_limit_order(self, left, right, price, volume):
        ''' Create a sell limit order.

        Parameters
        ----------

        left: str
            eg. 'vet'

        right: str
            eg. 'usdt'
        
        price: float
            eg. 10.1
        
        volume: float
            eg. 101

        Returns
        -------
        order
            A `UserOrder` or None if operation failed.
        '''

        return self._new_limit_order(left, right, price, volume, buy_or_sell='sell')

    def orders_status(self, order_id_list):
        ''' Get a list of order status.

        Parameters
        ----------

        order_id_list: list
            A list of order ids. either in str or int.

        Returns
        -------

        order
            A `UserOrder` or None if operation failed.

        '''
        order_id_list = [ int(x) for x in order_id_list ]

        url = URL + '/orders'
        data = {
            'ids': order_id_list
        }

        data = self._build_data(data)

        r = requests.get(url, data=data, timeout=TIMEOUT)

        result = r.json()
        if result['code'] != 0:
            return None
        else:
            return [ UserOrder(
                x['remaining_volume'],
                x['price'],
                x['created_on'],
                x['side'],
                x['volume'],
                x['state'],
                x['ord_type'],
                x['avg_price'],
                x['executed_volume'],
                x['id'],
                x['market']
            ) for x in result['data']]


    def cancel_orders(self, order_id_list):
        ''' Cancel multiple orders.
        
        Parameters
        ----------

        order_id_list: list
            A list of order ids. either in str or int.

        Returns
        -------
        boolean
            Success or not.
        '''
        order_id_list = [int(x) for x in order_id_list]
        url = URL + '/order/delete/multi'
        data = {
            'ids': order_id_list
        }
        data = self._build_data(data)
        r = requests.post(url, data=data, timeout=TIMEOUT)
        result = r.json()
        if result['code'] != 0:
            return False
        else:
            flags = []
            for each in result['data']:
                if each['id'] in order_id_list:
                    flags.append(True)
            
            if len(order_id_list) == len(flags):
                return True
            else:
                return False
    
    def cancel_all_orders(self):
        ''' Cancel all the opening orders '''
        url = URL + '/orders/clear'
        data = {}
        data = self._build_data(data)
        r = requests.post(url, data=data, timeout=TIMEOUT)
        result = r.json()

        if result['code'] != 0:
            return False
        else:
            return True

class Account:
    ''' User wallets, balances.

    Attributes
    ----------

    symbol: str
        eg. 'BTC'
    
    balance: float
        eg. 101.101
    
    locked_balance: float
        en. 101.101
    '''

    def __init__(self, symbol, balance, locked_balance):
        self.symbol = symbol.lower()
        self.balance = float(balance)
        self.locked_balance = float(locked_balance)


class UserOrder:
    ''' UserOrder that is created, either executed, half-executed, or not-yet-executed.

    Attributes
    ----------
    remaining_volume: float
        remain volume that not yet executed.

    price: float
        price of the target order, can be `None` for market orders.
    
    created_on: int
        unixtimestamp
    
    side: str
        'buy', 'sell'
    
    volume: float
        volume of the order
    
    state: str
        'wait', 'done' or 'cancel'
    
    ord_type: str
        'limit' or 'market'
    
    avg_price: float
        average execution price.
    
    executed_volume: float
        volume that has finished.
    
    identifier: int
        identifier of the order.
    
    market: str
        which market this order belongs to.

    '''
    def __init__(self, remaining_volume, price, created_on, side, volume, state, ord_type, avg_price, executed_volume, identifier, market):
        self.remaining_volume = float(remaining_volume)
        if price == None:
            self.price = 0
        else:
            self.price = float(price)
        self.created_on = int(created_on)
        self.side = side.lower()
        self.volume = float(volume)
        self.state = str(state)
        self.ord_type = str(ord_type)
        self.avg_price = float(avg_price)
        self.executed_volume = float(executed_volume)
        self.identifier = int(identifier)
        self.market = str(market)