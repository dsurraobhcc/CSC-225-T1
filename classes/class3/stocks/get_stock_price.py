'''
Create an account and select the Free plan here. Also active sandbox
for testing.
https://intercom.help/iexcloud/en/articles/2915433-testing-with-the-iex-cloud-sandbox


DO NOT SHARE YOUR API TOKENS!
'''
import urllib
from urllib.request import Request, urlopen
from urllib.error import URLError
import json

base_url = 'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token='

symbol = input('Enter a stock symbol: ')
base_url = base_url.replace('{symbol}', symbol)

# read api token
token = ''
with open('config.json') as f:
    json_data = json.load(f)
    token = json_data['iex_api_token']

base_url = base_url.replace('{symbol}', symbol) + token
req = Request(base_url)

try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print(e.reason)
    elif hasattr(e, 'code'):
        print(e.code)
else:
    data = response.read()
    json_data = json.loads(data)
    print(json_data['symbol'], json_data['companyName'], json_data['latestPrice'])