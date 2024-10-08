
# HTTP İstekleri ile Python Uygulamaları

Bu projede, Python kullanarak HTTP isteklerini gerçekleştirmek için dört temel örnek oluşturdum: GET, POST, PUT ve DELETE. Bu istekler, web üzerindeki API'lerle etkileşimde bulunmama yardımcı oluyor. Örneklerimi `jsonplaceholder.typicode.com` adlı bir test API'sini kullanarak gerçekleştirdim.

## Proje Yapısı

Projem aşağıdaki dosyaları içeriyor:

```

│
├── get_request.py
├── post_request.py
├── put_request.py
└── delete_request.py
```

### 1. `get_request.py`

Bu dosya, belirli bir kaynağı almak için GET isteği yapıyor. Örneğin, belirli bir gönderiyi (post) almak için kullanıyorum. 

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"  # Örnek API URL'si
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("GET İsteği Başarılı!")
    print(data)
else:
    print("GET İsteği Hatası:", response.status_code)
```

- **Açıklama**: 
  - `requests.get(url)` fonksiyonu, belirtilen URL'den veri alıyor.
  - Eğer istek başarılıysa (HTTP 200 durumu), alınan verileri ekrana yazdırıyorum.

### 2. `post_request.py`

Bu dosya, yeni bir kaynak oluşturmak için POST isteği yapıyor. Örneğin, yeni bir gönderi oluşturmak için kullanıyorum.

```python
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
```

- **Açıklama**: 
  - `requests.post(url, json=data)` fonksiyonu, belirtilen URL'ye yeni bir veri gönderiyor.
  - Eğer istek başarılıysa (HTTP 201 durumu), oluşturulan veriyi ekrana yazdırıyorum.

### 3. `put_request.py`

Bu dosya, var olan bir kaynağı güncellemek için PUT isteği yapıyor.

```python
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
```

- **Açıklama**: 
  - `requests.put(url, json=data)` fonksiyonu, belirtilen URL'deki veriyi güncelliyor.
  - Eğer istek başarılıysa (HTTP 200 durumu), güncellenen veriyi ekrana yazdırıyorum.

### 4. `delete_request.py`

Bu dosya, belirli bir kaynağı silmek için DELETE isteği yapıyor.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)

if response.status_code == 200:
    print("DELETE İsteği Başarılı!")
else:
    print("DELETE İsteği Hatası:", response.status_code)
```

- **Açıklama**: 
  - `requests.delete(url)` fonksiyonu, belirtilen URL'deki veriyi siliyor.
  - Eğer istek başarılıysa (HTTP 200 durumu), işlem başarılı olarak kabul ediliyor.

## Kullanım

Bu dosyaları çalıştırmak için bilgisayarımda Python yüklü olmalı. Her bir dosyayı terminal veya komut istemcisinde çalıştırarak örnek HTTP isteklerini deneyebilirim.

### Gereksinimler

- Python 3.x
- `requests` kütüphanesi (Kurmak için: `pip install requests`)

