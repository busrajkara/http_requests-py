import requests

url = "https://jsonplaceholder.typicode.com/posts/1"  # Örnek API URL'si
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("GET İsteği Başarılı!")
    print(data)
else:
    print("GET İsteği Hatası:", response.status_code)
