import requests

url = 'https://greenteapress.com/thinkpython/thinkpython.pdf'
r = requests.get(url)

with open('filename.pdf', 'wb') as fd:
    fd.write(r.content)

    
# Иногда файл может быть в закодирован в формате base64 тогда чтобы его записать делаем так
import base64
dataStr = response.json()['Data']
base64EncodedStr = base64.b64decode(dataStr.encode('utf-8'))

# create pdf file
with open('filename.pdf', 'wb') as f:
    f.write(base64EncodedStr)
    
