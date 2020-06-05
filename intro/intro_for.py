#반복문 종류 2개
# 1. While
# while 문은 어떤 구간이 정해져 있지 않고, 무한대로?
n = 0
# while n < 3 :
#     print(n)
#     n += 1
# # 0 1 2
# while n < 3 :
#     n += 1
#     print(n)
# print(n)

# 2. for
# number = list(range(3,10,3))
# print(number)

# for num in range(10):
#     print(num)

# 2-1. list for
# number = [10,9,8,7,6,5,4,3,2,1,0]
# for num in number:
#     print(num)

# number = ['삼성','역삼','선릉','영등포']
# for num in number:
#     print(num)

# 2-2. idx로 접근하고 싶어요.
number = ['삼성','역삼','선릉','영등포']
for i in range(len(number)):
    print(i)
    print(number[i])
print("*"*30)

# 3. dictionary
mask = {
    '삼성' : 100,
    '역삼' : '50게',
    '선릉' : True
}
for i in mask:
    print(i)
print("*"*30)
# 동작은 위 코드와 동일하나, dict라는걸 표현하기 위함이다.
for i in mask.keys():
    print(i)
    print(mask[i])
print("*"*30)
for i in mask.values():
    print(i)
print("*"*30)    
for key, val in mask.items():
    print(key)
    print(val)
    print(mask[key])
    print(key,val)
print("*"*30)
# 2-3. enumerate 열거형
for idx, i in enumerate(number):
    print(idx, i)
print("*"*30)