import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)

if response.status_code == 200:
    print("DELETE İsteği Başarılı!")
else:
    print("DELETE İsteği Hatası:", response.status_code)
