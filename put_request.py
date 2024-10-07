import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
data = {
    "id": 1,
    "title": "updated title",
    "body": "updated body",
    "userId": 1
}
response = requests.put(url, json=data)

if response.status_code == 200:
    print("PUT İsteği Başarılı!")
    print(response.json())
else:
    print("PUT İsteği Hatası:", response.status_code)
