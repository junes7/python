import requests
url = 'https://api.bithumb.com/public/ticker/btc'
response = requests.get(url).json()['data']
# data = response.json()
# my_dict = data['data']
# print(response)
fluctuation = int(response['max_price']) - int(response['min_price'])
if fluctuation + int(response['opening_price']) >= int(response['closing_price']):
    print("상승장")
else:
    print("하락장")
