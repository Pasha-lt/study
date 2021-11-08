import re

"""
\d = ANy Digit 0-9
\D = Any non DIGIT
\w = Any Alphabet symbol [A-Z a-z]
\W = Any non Alphabet symbol
\s = breakspace
\S = non breakspace
? = 0 or 1 characters
+ = 1 or more characters
* = 0 or more characters
. = 1 new symbol
\. = dot
^ = start string
$ = end string
a|b = symbol a or b

https://regex101.com/ = Cайт для тренировки и составления Регулярок
"""

my_string = """
Please contact my@google.com for assistance
обычный текст 123.234.33.10:808 просто текст 11.234.33.10:801 0673898909 +3809875689
andrey_str@gmail.com подросток патока полдень
Andrey fust Find CHSN Проверка русского текста Андрей одолжил ДЕНЕГ Aaaaa Bbbbb Rrrrrr rrrr
порог пригород
Вы можете посмотреть карту сайта <a href="map.php">тут</a>.
Посетите также <a href="best.php"раздел></a>
"""

# Ищем в строке имейл. search - ищет только первое вхождение.
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
match = re.search(pattern, my_string)
if match:
    print(match.group())

# Еще один вариант поиска имейлов с в другой записи. Выводи сразу все емейлы.
# findall - ищет все вхождения
email_patern = r"[\w._-]+@[\w._-]+\.[\w.]+"
result = re.findall(email_patern, my_string)
print(result)

# Ищем в строке айпи адрес с портом
for in_str in my_string.split('текст'):
    match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:\:\d{1,5})?)', in_str)
    if match:
        print(match[0])

# Чтобы не разделять текст и не искать по одному вхождению мы можем сразу искать все.
all_result = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:\:\d{1,5})?)', my_string)
print(all_result)

# Ищем телефонные номера, в запросе говорим что нужно числа состоящие из 10-11 цифр.
phone_numbers = re.findall(r'(\d{10,11})', my_string)
print(phone_numbers)

# Ищем слово с заглавной буквы. Ищем большую букву затем сколько угодно маленьких
phone_numbers = re.findall(r'([A-Z][a-z]+)', my_string)
print(phone_numbers)

# Ищем слова с заглавной буквы в русском варианте
phone_numbers = re.findall(r'([А-Я][а-я]+)', my_string)
print(phone_numbers)

# Диапазон можно указывать не на весь алфавит, а на его часть
# 'А-С - певрая буква от А до С большая', [a-z] - вторая буква и дальше '*' любое количество символов.
phone_numbers = re.findall(r'([A-C][a-z]+)', my_string)
print(phone_numbers)

# Диапазон можно указывать не на весь алфавит, а на конкретную букву например.
# Первая буква большая или маленькая 'R'
phone_numbers = re.findall(r'([Rr][a-z]+)', my_string)
print(phone_numbers)

# Чтобы исключить что-то используем дужки и знак вопроса знак восклицания '(?!)'
# сначала пишем что исключаем потом условие и исключаем все что начинается на 're'
phone_numbers = re.findall(r'((?!re)[Rr][a-z]+)', my_string)
print(phone_numbers)

# \b указываем с чего начинается строка
pattern = r'\bпо\w+'
p_word = re.findall(pattern, my_string)
print(p_word)

# первая буква или 'п' или 'А'
pattern = r'([п|А][\w]+)'
p_word2 = re.findall(pattern, my_string)
print(p_word2)

# href=" - указываем с чего начинается, заканчивается кавычками (")
# В скобках пишем что нам нужно вытащить из этого шаблона
pattern = r'href="(.+?)"'
result = re.findall(pattern, my_string)
print(result)

# замена патерна на пустое место, тоесть удаление.
string = 'Вы можете посмотреть карту сайта <a href="map.php">тут</a>. Посетите также <a href="best.php"раздел></a>'
pattern = r'<(.+?)>'
result = re.sub(pattern, '', string)
print(result)  # Вы можете посмотреть карту сайта тут. Посетите также
