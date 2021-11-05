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
"""

my_string = """
Please contact my@google.com for assistance
обычный текст 123.234.33.10:808 просто текст 11.234.33.10:801 0673898909 +3809875689
Andrey fust Find CHSN Проверка русского текста Андрей одолжил ДЕНЕГ Aaaaa Bbbbb Rrrrrr
"""

# Ищем в строке имейл
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
match = re.search(pattern, my_string)
if match:
    print(match.group())  # my@google.com

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
phone_numbers = re.findall(r'([A-C][a-z]+)', my_string)
print(phone_numbers)

# Диапазон можно указывать не навесь алфавит, а на конкретную букву например.
phone_numbers = re.findall(r'([R][a-z]+)', my_string)
print(phone_numbers)
