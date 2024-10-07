import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response = requests.post(url, json=data)

if response.status_code == 201:
    print("POST İsteği Başarılı!")
    print(response.json())
else:
    print("POST İsteği Hatası:", response.status_code)
