from amazon_sp_api import authorize


class AmazonAPI:
    def __init__(self, client_id, client_secret, refresh_token):
        self.token = authorize(client_id, client_secret, refresh_token)
        self.headers = {
            'x-amz-access-token': self.token,
            'Content-Type': 'application/json'
        }

    def get_orders(self):
        endpoint = 'orders/v0/orders'


