import pdfplumber

# Вытягиваем текствое содержимое из PDF файла.
with pdfplumber.open('filename.pdf') as f: # открываем файл что бы не перегружать оперативку большим файлом выводим постранично и сравниваем
    entrance_msa = any(['Нужная нам строчка' in i.extract_text() for i in f.pages]) # Используя any если будет хобя бы 1 совпадение вернет True
    return entrance_msa
