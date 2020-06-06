from lt import lottos

pick = lottos.lotto(1000000)
print(pick)

# 1. 만약 4등 한적이 있으면
if pick['3rd'] >= 1:
# 2. 4등 '몇 번' 했습니다.
    print(f'3등{pick["3rd"]}번 했습니다')
# 3. 4등 한 적 없으면, 실패 출력
else:
    print('3등 실패')
if pick['1st'] >= 1
    print(f)
