from amazon_sp_api.sp_api import Order
import json


with open('./creds/creds.json', 'r') as f:
    creds = json.load(f)


def test_get_order():
    amz_api = Order(credentials=creds, marketplace='ATVPDKIKX0DER')
    assert amz_api.get_order('113-3916693-7198605')
    assert amz_api.get_order('113-1715711-5883427')


if __name__ == '__main__':
    test_get_order()

