my_str = "Life is too short, you need pyhton"

# 문자열을 반복문으로
for char i my_str:
    print(char)
print(my_str[0])
# split()함수에 아무것도 안 넣었을 때에는 
# 공백기준으로 나뉜다.

# 문자열 (빈 공간을 기준으로) 분할하기 
new_str = my_str.split(' ')
print(new_str)

print(my_str.find('i'))
print(my_str.index('i'))
# print(my_str.index('a'))

# 리스트 안의 문자열 인덱스로 접근하기
print(new_str[0][0])

# 문자열 (특정 문자열로) 대체하기
new_str = my_str.replace('Life','Time')
print(my_str)
print(new_str)

# 모음을 모아둔 리스트
vowels = ['a','e','i','o','u']

# 모음이 my_str에 있는지 확인하기
for char in vowels:
    if char in my_str:
        my_str = my_str.replace(char, '')

# 새로운 값 result에 조건에 부합하는 값 저장하기
result = ''
for char in my_str:
    if char not in vowels:
        result += char
print(result)

for char in my_str:
    if char in vowels:
        pass
    else:
        result += char
print(result)