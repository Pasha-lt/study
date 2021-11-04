import re

# Ищем в строке имейл
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact my@google.com for assistance"
match = re.search(pattern, str)
if match:
   print(match.group()) # my@google.com

# Ищем в строке айпи адрес с портом 
my_str = 'обычный текст 123.234.33.10:808 просто текст 11.234.33.10:801'
for in_str in my_str.split('текст'):
   match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:\:\d{1,5})?)', in_str)
   if match:
      print(match[0])
      
# Чтобы не разделять текст и не искать по одному вхождению мы можем сразу искать все      
all_result = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:\:\d{1,5})?)', my_str)
print(all_result)
