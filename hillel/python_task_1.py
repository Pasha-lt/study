# За допомогою модулю requests зробити запит на
# https://baconipsum.com/api?type=meat-and-filler.
# Запросити мінімум пʼять параграфів тексту.
# Параграфи можна задати як квері-параметри (подивитись на приклад можна тут).
# Кількість параграфів зчитувати зі стандартного вводу на початку роботи програми.
# Обернути назад список рядків у цьому масиві.
# Тобто зробити останній рядок - перший (з індексом нуль),
# передостанній - другий (з індексом 1) і т.д.
# Можна знайти, як це робити в документації класу list, або придумати самостійно.
# Підрахувати у ваших параграфах кількість параграфів, в яких присутнє слово "Pancetta".
# Записати в файл наступну інформацію:
# Ваше імʼя та дату запуску програми, цифру,
# яку ми отримали в третьому пункті та повернутий назад массив параграфів
# (кожен новий параграф записати з нової строки).


import requests
from datetime import date


def request(amount_paragraph):
    url = f"https://baconipsum.com/api?type=meat-and-filler&paras={amount_paragraph}"
    response = requests.get(url=url)
    string_new = response.json()[::-1]
    return string_new


def user_input():
    para = int(input("введіть кількість параграфів: "))
    while para < 5:
        print("Введіть число більше або рівне 5")
        para = int(input("введіть кількість параграфів: "))
    return para


def counter(list_a):
    amount = 0
    for i in list_a:
        if "pancetta" in i:
            amount += 1
    return amount


def writer(text):
    with open("result.txt", "w") as file:
        file.write(text)


def text_shaper(amount_pan, response_list):
    text = "Pavlo" + "\n"
    text += str(date.today()) + "\n"
    text += str(amount_pan) + "\n"
    for i in response_list:
        text += i + "\n"
    return text


if __name__ == "__main__":
    amount_paragraph = user_input()
    response_list = request(amount_paragraph)
    amount_pan = counter(response_list)
    full_text = text_shaper(amount_pan, response_list)
    writer(full_text)
