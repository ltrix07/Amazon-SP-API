import requests
from amazon_sp_api import TOKEN_URL
from requests.auth import HTTPBasicAuth


def authorize(app_id, app_secret, app_refresh):
    token_data = {
        'grant_type': 'refresh_token',
        'refresh_token': app_refresh,
        'client_id': app_id,
        'client_secret': app_secret
    }
    token_resp = requests.post(TOKEN_URL, data=token_data)
    return token_resp.json()['access_token']
