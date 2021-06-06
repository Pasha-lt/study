import requests

# # простой get запрос
# response = requests.get("https://httpbin.org/get")
#
# # Проверка статус кода на то что он двухсотый.
# assert response.status_code == 200
#
# # Проверка на то что статус код меньше 400
# assert response.ok

# # Отправляем в headers User-Agent и меняем его.
# headers = {"User-Agent": "unknown"}
# response_2 = requests.get("https://httpbin.org/get", headers=headers)
# print(response_2.text)

# # Передаем параметры через get (?a=b)
# response_3 = requests.get("https://httpbin.org/get?a=b")
# print(response_3.text)

# # Передаем параметры через get c помощью params
# params = {'a': 'b', 'c': 121}
# response_4 = requests.get("https://httpbin.org/get", params=params)
# print(response_4.text)

# # Передаем post запрос. У нас появляються новые параметры json, data, files, form
# params = {'a': 'b', 'c': 121}
# json = {'username': 'supersecret'}
# response_5 = requests.post("https://httpbin.org/post", params=params, json=json)
# print(response_5.text)

# запускаем запрос через прокси, сначала в терминале нужно поднять mitmproxy, работаем с http
# proxy = {'http':'localhost:8080'} # Указываем куда отправляем трафик
# requests.get("http://meta.ua", proxies=proxy)
# requests.get("http://google.com", proxies=proxy)
# requests.get("http://rozetka.com.ua", proxies=proxy)

# запускаем запрос через прокси, сначала в терминале нужно поднять mitmproxy, работаем с https
# c https нам нужен сертификат ssl, можем его игнорировать, просто скипаем этот шаг verify=False, верить сайту
# proxy = {'http':'localhost:8080', 'https':'localhost:8080'} # Указываем куда отправляем трафик
# requests.get("https://meta.ua", proxies=proxy, verify=False)
# requests.get("http://google.com", proxies=proxy)

# Куки нужно чтобы дал сервер
google = "http://google.com"
proxy = {'http': 'localhost:8080', 'https': 'localhost:8080'}  # Указываем куда отправляем трафик
# r = requests.get(google, proxies=proxy, verify=False)
#
# # Достаем куки из нашего запроса
# for el in r.cookies.items():
#     print(el)

# # Отправляем куки. после того как один куки записали ставим(;)
# header = {'cookies':'1P_JAR=2021-06-05-11;NID=216=Qr92tw37VVegswx9-r-B8PZ-XUhy1mCIpqLh55rR0ai6q4h5QMESJAiMsZY6zCnOSekzPsG5jEDEyXZdaskH4lMESzFQkFcxqh8Fo0V3BQedWGUQca8Jap3F1H6wfUG65bfHO1Y2xvjqlOay1gkQJ50BlRGd98En-rZ0nHjl3SY'}
# r = requests.get(google, proxies=proxy, headers=header, verify=False)
# for el in r.cookies.items():
#     print(el)

# # Вариант отправки куки через опцию реквестс
# cookies = {'1P_JAR': '2021-06-05-11',
#            'NID': '216=Qr92tw37VVegswx9-r-B8PZ-XUhy1mCIpqLh55rR0ai6q4h5QMESJAiMsZY6zCnOSekzPsG5jEDEyXZdaskH4lMESzFQkFcxqh8Fo0V3BQedWGUQca8Jap3F1H6wfUG65bfHO1Y2xvjqlOay1gkQJ50BlRGd98En-rZ0nHjl3SY'}
# r = requests.get(google, proxies=proxy, cookies=cookies, verify=False)
# for el in r.cookies.items():
#     print(el)

# редирект и таймаут.
# response = requests.get('http://google.com', proxies=proxy, allow_redirects=False) # Запретить редирект 'allow_redirects=False'
# response = requests.get('http://google.com', proxies=proxy, timeout = 0.1)  # timeout = 0.1 ставим таймаут на ОДИН редирект.
# response = requests.get('http://google.com', proxies=proxy)
# print(response.status_code)

# Загрузка и скачивание файлов Запись сайта.
# site = 'https://www.google.com/'
# r = requests.get(site, proxies=proxy, verify=False)
# with open('.index.html', 'wb')as f:
#     f.write(r.content)

# Загружаем картинку
# url_picture = 'https://www.imgonline.com.ua/examples/bee-on-daisy.jpg'
# r = requests.get(url_picture, proxies=proxy, verify=False)
# with open('image.jpg', 'wb')as f:
#     f.write(r.content)

# Загружаем картинку кусочками в потоковом режими так надежней чем выше
# url_picture = 'https://www.imgonline.com.ua/examples/bee-on-daisy.jpg'
# r = requests.get(url_picture, proxies=proxy, stream=True, verify=False)
# with open('image.jpg', 'wb')as f:
#     for chunk in r.iter_content(chunk_size=1024): # загружаем по дефолту загружает по 1 байту
#         f.write(chunk)


# Отправка информации
upload ='http://httpbin.org/anything' # Приемник который ждет что бы в него была загружена информация.
with open('image.jpg', 'rb') as f:
    requests.post(upload, proxies=proxy, data=f)
