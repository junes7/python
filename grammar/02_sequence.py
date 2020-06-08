# 02_sequence.py
# 데이터가 순차적으로 나열이 되어있다.
# 주의할 점. 정렬 되어있다는 뜻은 아니다.
# list, tuple, range, string
# 1. list
list_a = []
list_b = list()
list_a = ['삼성', 23, True]
# 1-1. idx로 접근하기
print(list_a[0])
# 아래와 같이 인덱스로 -1을 넣으면 
# 맨 뒤의 요소를 출력할 수 있다.
print(list_a[-1])
print(list_a[-2])

# 2. tuple
tuple_a = ()
tuple_a = (1, 2)
print(tuple_a)
# 값을 하나만 넣고자 한다면
# 괄호 안에 반드시 콤마(,)를 넣어준다.
tuple_b = (1,)
tuple_c = (1)
print(type(tuple_b))
print(type(tuple_c))

# 3. range
print(range(10))
print(type(range(10)))
print(list(range(10)))
print(list(range(3,10,2)))




