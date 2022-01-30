# path_work_dir = os.getcwd() # путь к текущей папке
# устанавливаем путь к текущей рабочей папке в нашем случае это /home/admin2/Desktop
# os.chdir(r'/home/admin2/Desktop')
# os.rename('old_name.txt', 'new_name.txt' )  # переименование файлов
# os.remove('new_name.txt')  # Удаление файлов
# os.makedirs('dir2')  # Создаем директорию
# atime = os.path.getatime(path) # Дата последнего чтения
# mtime = os.path.getmtime(path) # Дата последнего редактирования
# print(f'Дата последнего использования: {datetime.fromtimestamp(atime)}')
# print(f'Дата последнего редактирования: {datetime.fromtimestamp(mtime)}')

import os
folder_name = 'project'
file_name = 'my_file.txt'

uni_path = os.path.join('docs', folder_name, file_name) # склеиваем путь.
print(uni_path)
abs_path = os.path.abspath(file_name) # генерируем абсолютный путь.
print(abs_path)
step_up_path = os.path.abspath(os.path.join('..', '..')) # поднимаемся на две папки выше. на 1 = ..
step_up_path = os.path.abspath(os.path.join(os.path.sep, os.path.sep)) # тоже что и выше
print(step_up_path)

# просматриваем каталог.
# for i in os.listdir(os.path.abspath(os.path.join(os.path.sep))): #проходим по директории
#     print(os.path.abspath(os.path.join(i)))  # Выводим файлы и папки
    
print(os.path.exists(abs_path))  # Проверяем существует ли такой путь


# размер файла
# size = os.path.getsize(path)
# ksize = size//1024

# Открываем файл
# subprocess.call(['xdg-open', filename]) # Открыть файл linux или МАК
# os.startfile(filename) # Открыть файл window



# Делаем проверку на три операционных системы с открытием файла
def open_file(filename):
    if "win" in sys.platform:
        os.startfile(filename)
    else:
        opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
        subprocess.call([opener, filename])
