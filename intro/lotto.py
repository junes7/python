import random
# print(dir(random))

# choice를 써보자.
number = random.choice(range(10))
print(number)

# list에서 무작위로 뽑아보자.
arr = ['100', '50', '30', '20']
pick = random.choice(arr)
print(pick)

# dict에도 써보자.
mask = {
    '100' : '삼성',
    '50' : '역삼',
    '30' : '선릉',
    '20' : '영등포'
}
print(mask[pick])

#sample
# 1-45 숫자 중 6개 출력
lotto = random.sample(range(1, 46), 6)
print(lotto)
# iterable 객체로부터 정렬된 리스트를 생성
print(sorted(lotto))
print(lotto)
# 리스트를 정렬된 형태로 변경
print(lotto.sort())
print(lotto)
