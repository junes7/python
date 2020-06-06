
# => 33

def snail(height, day, night):
    count = 0
    # while문이 불 필요하게 한 번 더 도는것을 방지하기
    # 위하여 조건문 대신 True를 써준다. 
    # while height >= 0:
    while True:
        count += 1
        height -= day
        if height <= 0:
            break
        height += night
    return count
print(snail(100, 5, 2))
def snail1(height, day, night):
    count = 0
    while True:
        count += 1
        height -= day
        if height <= 0:
            return count
        height += night

print(snail1(100, 5, 2))
