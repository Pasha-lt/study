import requests

# простой get запрос
response = requests.get("https://httpbin.org/get")

# Проверка статус кода на то что он двухсотый.
assert response.status_code == 200

# Проверка на то что статус код меньше 400
assert response.ok

# Отправляем в headers User-Agent и меняем его.
headers = {"User-Agent": "unknown"}
response_2 = requests.get("https://httpbin.org/get", headers=headers)
print(response_2.text)

# Передаем параметры через get (?a=b)
response_3 = requests.get("https://httpbin.org/get?a=b")
print(response_3.text)

# Передаем параметры через get c помощью params
params = {'a': 'b', 'c': 121}
response_4 = requests.get("https://httpbin.org/get", params=params)
print(response_4.text)

# Передаем post запрос. У нас появляються новые параметры json, data, files, form
params = {'a': 'b', 'c': 121}
json = {'username': 'supersecret'}
response_5 = requests.post("https://httpbin.org/post", params=params, json=json)
print(response_5.text)

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

# Вариант отправки куки через опцию реквестс
cookies = {'1P_JAR': '2021-06-05-11',
           'NID': '216=Qr92tw37VVegswx9-r-B8PZ-XUhy1mCIpqLh55rR0ai6q4h5QMESJAiMsZY6zCnOSekzPsG5jEDEyXZdaskH4lMESzFQkFcxqh8Fo0V3BQedWGUQca8Jap3F1H6wfUG65bfHO1Y2xvjqlOay1gkQJ50BlRGd98En-rZ0nHjl3SY'}
r = requests.get(google, proxies=proxy, cookies=cookies, verify=False)
for el in r.cookies.items():
    print(el)
