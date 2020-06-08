# 04_dict_and_set
# 1. dictionary
# key, value로 이루어져 있음
dict_a = {}
dict_b = dict()
# key가 중복이 불가능하다
dict_a = {'삼성':100, '역삼':50, '삼성':30}
# 위와 같았을 때 동일한 키의 값을 덮어 씌어버렸다.
print(dict_a)

print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())
# key값으로 value값에 접근하는 방법
print(dict_a['삼성'])
print(dict_a.get('삼성'))

# .get과 []차이점
dict_a = {'삼성':100, '역삼':50}
# print(dict_a.get('선릉'))
# print(dict_a['선릉'])

# 2. set 집합
# set는 순서가 없이 저장된다.
# 중복이 없다.
set_a = {1, 2, 3}
set_b = {3, 5, 9}
# set_b = set()
print(set_a)
print(set_a - set_b)
print(set_a | set_b)
print(set_a & set_b)

list_a = [1,1,1,1]
# 아래와 같이 한 줄로 중복 제거를 해 줄 수 있다.
print(list(set(list_a))[0])
# immutable 불가변성 mutable 가변성

string_a = "immutable"
string_b = string_a
# string_a랑 string_b의 할당받은 메모리의 주소값을
# 출력하고 싶을때 id(string_a) 형태를 사용한다.
print(id(string_a), id(string_b))
string_b += 'e'
print(string_a,string_b)
print(id(string_a), id(string_b))

# list_a = ['immutable?','real?']

# list_a 랑 list_b 포인터가 "immutable"이라는 값이 들어있는 주소를
# 가리키고 있기 때문에 id()를 찍어보면 동일하다.
list_a = "immutable"
list_b = list_a
print(list_a, list_b)
print(id(list_a), id(list_b))


list_a = [3, 'real?']
list_b = list_a
print(list_a, list_b)
print(id(list_a), id(list_b))
# list_b라는 포인터를 통해서 3이라는 데이터를 mutable이라는
# 데이터로 변경해준다. 그리고 동일하게 같은 주소값을 가리키고
# 있기 때문에 주소값이 변경되지 않는다.
list_b[0] = 'mutable'
print(list_a, list_b)
print(id(list_a), id(list_b))
list_b = ['mutable']

# print(string[0])
# print(list_a[0])
# string[0] = 'a'
# list_a[0] = 'mutable'

# print(list_a)
# list_a = ['mutable']
# print(list_a)

