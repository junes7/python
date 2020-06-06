# 조건문
# 내장함수 -> built-in function
# 형변환 str -> int
number = int(input())
print(number + 3)

# 스트링으로 변환하려면?
#number = str(number)

# 1. if 조건문
if number > 3 :
    ## 들여쓰기 space bar 4번으로
    print("3초과")
# if구문은 스페이스바 4번 해서 들여쓰기를 한다.
print("????")
# 1-2. 조건 여러개 쓰고 싶어요.
if number > 10 :
    print("10초과")
    #그게 아니라,number가 10이하ㅡ 5초과 일때는?
elif 10 >= number >5 :
    print("10이상 5초과")
else :
    print("5이하")
		