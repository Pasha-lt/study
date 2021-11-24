import base64

# Кодируем строку. Сначала нужно закодировать текст в байт строку.
my_text = 'Encode this text'.encode('utf-8') #кодируем в байт строку
encoded_text = base64.b64encode(my_text) #кодируем из байтов в 64 разрядный
print(encoded_text)

# расшифровываем текст
decoded_text = base64.b64decode(encoded_text) #декодируем из base64
decode_byte = decoded_text.decode('utf-8') #декодируем из байт строки
print(decode_byte)

# кодируем рисунок в base64
with open("2.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print(type(str))
    with open("picture.txt","w") as f:
        f.write(str.decode())
    
# преобразовываем из кода в рисунок
image_binary=base64.decodebytes(str)
with open('image.jpg','wb') as f:
    f.write(image_binary)
