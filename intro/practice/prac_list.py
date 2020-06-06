fruits = ['orange','apple','pear','banana','kiwi','apple','banana']
# fruits 배열 중 apple 문자열의 갯수
print(fruits.count('apple'))

print(fruits.count('tangerine'))
# banana 문자열이 있는 인덱스 위치
print(fruits.index('banana'))
# 네번째 인덱스 다음에 banana 문자열이 있는 위치 
print(fruits.index('banana', 4))
# Find next banana starting a position 4
print(fruits)
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)
print("*"*30)
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
stack.pop()
print(stack)
print("*"*30)
