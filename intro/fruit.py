# 장바구니에 아래와 같은 과일이 들어 있고 과일 판별 
# 리스트가 있습니다. 현재 장바구니에는 과일이 몇 개이고,
# 과일이 아닌 것은 몇 개인지 출력하시요.

import random

basket_items = {
    'apples': 4, 
    'oranges': 19,
    'kites': 3,
    'sandwiches': 8
}

fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

fruit_count = 0
not_fruit_count = 0

# dict(사전)의 키, 벨류값 불러와서
for key, val in basket_items.items():
    # 해당 키 값이 fruits 리스트에 있는지 확인 
    if key in fruits:
        # 있으면 fruit_count에 val 더하기
        fruit_count += val
    else:
        # 없으면 not_fruit_count에 val 더하기
        not_fruit_count += val

print(f'과일의 갯수는 {fruit_count}개, 과일이 아닌 것은 {not_fruit_count}개 있습니다.')
