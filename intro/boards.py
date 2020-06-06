import requests
url = 'https://jsonplaceholder.typicode.com/posts'
#리스트로 데이터를 받아온다.
response = requests.get(url).json()

for data in response:
    if data['userId'] == 4:
        print(data['title'])

