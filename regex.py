import re

"""
\d = ANy Digit 0-9
\D = Any non DIGIT
\w = Any Alphabet symbol [A-Z a-z]
\W = Any non Alphabet symbol
\s = breakspace
\S = non breakspace
+ = 1 or more characters
\. = dot

https://regex101.com/ = Cайт для тренировки и составления Регулярок
"""

my_string = """
Please contact my@google.com for assistance
обычный текст 123.234.33.10:808 просто текст 11.234.33.10:801 0673898909 +3809875689
andrey_str@gmail.com
Andrey fust Find CHSN Проверка русского текста Андрей одолжил ДЕНЕГ Aaaaa Bbbbb Rrrrrr rrrr
"""

# Ищем в строке имейл
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
match = re.search(pattern, my_string)
if match:
    print(match.group())
    
# Еще один вариант поиска имейлов с в другой записи. Выводи сразу все емейлы.
email_patern  = r"[\w._-]+@[\w._-]+\.[\w.]+"
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

# Диапазон можно указывать не навесь алфавит, а на его часть
# 'А-С - певрая буква от А до С большая', [a-z] - вторая буква и дальше '*' любое количество символов.
phone_numbers = re.findall(r'([A-C][a-z]+)', my_string)
print(phone_numbers)

# Диапазон можно указывать не навесь алфавит, а на конкретную букву например.
# Первая буква большая или маленькая 'R'
phone_numbers = re.findall(r'([Rr][a-z]+)', my_string)
print(phone_numbers)

# Чтобы исключить что-то используем дужки и знак вопроса знак восклицания '(?!)'
# сначала пишем что исключаем потом условие и исключаем все что начинается на 're'
phone_numbers = re.findall(r'((?!re)[Rr][a-z]+)', my_string)
print(phone_numbers)
