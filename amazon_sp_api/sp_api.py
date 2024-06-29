from amazon_sp_api import API_URL
from amazon_sp_api.auth import authorize
import requests


class Order:
    def __init__(self, credentials: dict, marketplace: str):
        self.marketplace = marketplace
        self.token = authorize(
            credentials.get('lwa_app_id'), credentials.get('lwa_client_secret'),
            credentials.get('refresh_token')
        )
        self.headers = {
            'x-amz-access-token': self.token,
            'Content-Type': 'application/json'
        }

    def get_orders(
            self, created_after: str, **kwargs
    ):
        """
        Возвращает ордера, созданные или обновленные в течение периода времени, указанного в заданных параметрах.
    Вы также можете применить ряд критериев фильтрации, чтобы сузить список возвращаемых ордеров.
    Если присутствует NextToken, он будет использоваться для получения ордеров вместо других критериев.
        :param created_after: Необходимый параметр для получения ордеров после определенной даты.
        :param kwargs: Приведены в Args
        :return: Словарь со списком всех ордеров.

        Args:
            key CreatedAfter: date
            key CreatedBefore: date
            key LastUpdatedAfter: date
            key LastUpdatedBefore: date
            key OrderStatuses: [str]
            key MarketplaceIds: [str]
            key FulfillmentChannels: [str]
            key PaymentMethods: [str]
            key BuyerEmail: str
            key SellerOrderId: str
            key MaxResultsPerPage: int
            key EasyShipShipmentStatuses: [str]
            key NextToken: str
            key AmazonOrderIds: [str]
            key RestrictedResources: [str]
        """
        endpoint = 'orders/v0/orders/'
        params = {
            'MarketplaceIds': self.marketplace,
            'CreatedAfter': created_after,
            **kwargs
        }
        resp = requests.get(API_URL + endpoint, headers=self.headers, params=params)
        return resp.json()

    def get_order(self, order_id: str) -> dict:
        """
        Функция для получения информации по ордеру.
        :param order_id: Номер ордера.
        :return: Словарь с информацией об ордере.
        """
        endpoint = f'orders/v0/orders/{order_id}'
        resp = requests.get(API_URL + endpoint, headers=self.headers)
        return resp.json()





