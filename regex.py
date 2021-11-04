import re
"""
\d = ANy Digit 0-9
\D = Any non DIGIT
\w = Any Alphabet symbol [A-Z a-z]
\W = Any non Alphabet symbol
\s = breakspace
\S = non breakspace
"""

my_string = """
Please contact my@google.com for assistance
обычный текст 123.234.33.10:808 просто текст 11.234.33.10:801 0673898909 +3809875689
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

