import requests
import random
response = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=913')
print(response.json())
print(type(response.json()))
data = response.json()
winner = []
for i in range(1,7):
    # winner.append(data['drwtNo'+str(i)])
    winner.append(data[f'drwtNo{i}'])

win_rate = {
    '1st' : 0,
    '2nd' : 0,
    '3rd' : 0,
    '4th' : 0,
    'fail' : 0
}
for i in range(1000000):
    lotto = random.sample(range(1,46), 6)
    # lotto = [1, 3, 24, 35, 43, 22]
    matched = 0
    for num in lotto:
        if num in winner:
            matched += 1
    # 1. matched = 6 1등
    if matched == 6:
        win_rate['1st'] += 1
    # 2. 5면 3등
    elif matched == 5:
        if data['bnusNo'] in lotto:
            win_rate['2nd'] += 1
        else:
            win_rate['3rd'] += 1
    # 3. 4면 4등
    elif matched == 4:
        win_rate['4th'] += 1
    # 4. 그 외는 fail
    else :
        win_rate['fail'] += 1

print(win_rate)



# print(winner)
# print(lotto)
