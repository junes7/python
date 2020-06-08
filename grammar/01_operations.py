# 01_operations.py
# 논리 연산자
# and, or, not
print("____and____")
print(True and True)
print(True and False)
print(False and False)
print(False and True)

print("____or____")
print(True or True)
print(True or False)
print(False or False)
print(False or True)

print("____not____")
print(not True)
print(not False)
print(not 0)
print(not [])

# in, not in
print("____in____")
print('a' in 'apple')
print(1 not in [1,2,3])

# 단축 평가
# 우선 순위는 not and or 순이다.
# 밑의 경우는 Text가 출력이 되는데 이유는
# false 랑 true랑 비교해서 true가 나왔기 때문에
# 뒤 부분을 연산을 안 하고 출력한다.
print('' or 'Text' or 'Text2')
print('Text' and '' or 'Text2')

