#print("Hello, World!")

# 저장, 조건, 반복
# 1. 저장
# int? str? bool?
number = 10
string = "10"
boolean = True

print(number, string, boolean)
# arr 배열
# 2. 리스트 저장
arr = [number, string, boolean]
arr_2 = [10, "10", True, number]
# 2-1. 인덱스로 접근하기
print(arr_2[0], arr_2[1], arr_2[2])
# 2-2. 자료형 출력하기
print(type(arr_2[0]), type(arr_2[1]), type(arr_2[2]))
# 3. dictionary
mask = {
    '삼성' : 100,
    '역삼' : 50,
    '선릉' : 30,
    '영등포' : 10
}
print(mask)
print(mask['삼성'])

# 변수에 다른 값을 저장한다.
