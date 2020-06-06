# Computational Thinking
# 같은 문자가 여러 번 반복되는 패턴을 발견
data = 'aaaaabbbccccccddddddddd'
encoded = ''

count = 1
for i in range(1, len(data)):
    if data[i] == data[i - 1]:
    # 반복되는 문자를 세기
        count += 1
    else:
        # str(count)는 정수형 형태를 문자열 형태로 변형 해준다.
        #문자가 반복되는 횟수를 적어준다.
        encoded += data[i - 1] + str(count)
        count = 1

    if i == len(data) - 1:
        encoded += data[i] + str(count)

print(data)
print(encoded)
