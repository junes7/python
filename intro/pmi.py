import requests
from pprint import pprint

def pmi(params):
    url = f'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address={params}'
    response = requests.get(url).json()

    mask_info = {}
    remain = ['plenty','some','few','empty','break']
    for data in response['stores'][:10]:
        # print(data['name'],data['remain_stat'])
        if data['remain_stat'] == remain[0]:
            mask_info[data['name']] = '100개 이상'
        elif data['remain_stat'] == remain[1]:
            mask_info[data['name']] = '30개 이상'
        elif data['remain_stat'] == remain[2]:
            mask_info[data['name']] = '2개 이상'
        elif data['remain_stat'] == remain[3]:
            mask_info[data['name']] = '1개 이하'
        else:
            mask_info[data['name']] = '판매_중지'

    return mask_info

params = input('주소를 시 구 동으로 입력해 주세요 : ')
mask = pmi(params)

for key, val in mask.items():
    # print(key, '판매처에 마스크가', val, ' 있습니다.')
    print(f'{key}판매처에 마스크가 {val} 있습니다')
# pprint(mask)
    
