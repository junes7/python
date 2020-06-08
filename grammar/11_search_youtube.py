import requests
# API 키 값
key = 'AIzaSyDLfDw9iAqVIW_ANbtwCCdfCLYAwEMsCcg'
# string interpolation
search = input("검색어를 입력해 주세요 : ")
# query 쿼리 질의할 것
q = f'q={search}'
# type 매개변수는 특정 리소스 유형만 검색하도록
# 검색 쿼리를 제한한다. 값은 쉼표로 구분된 리소스
# 유형의 목록이다. 
my_type = 'type=video'
# 필수 매개변수
# part 매개변수는 API 응답이 포함하는 search 리소스 속성 
# 하나 이상의 쉼표로 구분된 목록을 지정한다. 매개변수 값에
# 포함할 수 있는 part이름은 id 및 snippet이다.
part = 'part=snippet'
url = f'https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}&{q}&maxResults=20'
# print(url)

# 1. 검색어를 입력하면
# 2. 영상들을 검색할 것
# 3. 그 영상들의 제목과 채널명

response = requests.get(url)
# print(type(response.json))
datas = response.json()
# 채널명, 영상 제목
for data in datas['items'][:10]:
    print(data['snippet']['title'], end =' 채널명 ')
    print(data['snippet']['channelTitle'])

