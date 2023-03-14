import requests
import pprint
import re

r = requests.get('https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E9%8D%B5%E7%9B%A4&page=1&sort=sale/dc')
if r.status_code == requests.codes.ok:
    data = r.json()
    #pprint.pprint(data)

    for product in data['prods']:
        print('商品:', product['name'])
        print('價格:', product['price'])
