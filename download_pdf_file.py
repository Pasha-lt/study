import requests

url = 'https://greenteapress.com/thinkpython/thinkpython.pdf'
r = requests.get(url)

with open('filename.pdf', 'wb') as fd:
    fd.write(r.content)
