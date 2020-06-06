import random
# 난수 메소드를 사용하기전에 random 클래스를 호출해 와야 한다.
# 1. 로또번호 추첨하는데 5번 반복해서
# n = 0
# while n < 5:
#    lotto = random.sample(range(1, 46), 6)
#    print(sorted(lotto))
#    n+=1

for i in range(5):
    print(sorted(random.sample(range(1, 46), 6)))
print("*"*30)
lotto = [sorted(random.sample(range(1, 46), 6)) for i in range(5)]
print(lotto)
# 2. 음식점 이름(key), 전화번호 딕셔너리
food = {
    '자장면' : '02-538-8887',
    '햄버거' : '02-567-1357',
    '피자' : '02-355-8758'
}
# 2-1. 그 중에서 무작위 음식점 하나 뽑아서
arr = ['자장면','햄버거','피자']
pick = random.choice(arr)

pick = random.choice(list(food.keys()))
print(pick)
# 2-2. 가게이름이랑 전화번호 출력
print(pick, food[pick])
print('가게 이름은',pick)
print('전화번호는',food[pick])

# f-string이라는 format을 지원해준다.
print(f'가게 이름은 {pick}, 전화번호는 {food[pick]}')

# interpolation 보간법

