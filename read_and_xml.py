import requests
from bs4 import BeatifulSoup

response = requests.request("POST",  url, headers=headers, data=payload) # Получаем ответ в xml формате.
soup = beatifulSoup(response.content, 'html.parser') #парсим xml html.parser`ом.
user_name = soup.find('user_name').text # вытягиваем данные по конкретному тегу.
