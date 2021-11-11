# path_work_dir = os.getcwd() # путь к текущей папке
# устанавливаем путь к текущей рабочей папке в нашем случае это /home/admin2/Desktop
# os.chdir(r'/home/admin2/Desktop')
# os.rename('old_name.txt', 'new_name.txt' )  # переименование файлов
# os.remove('new_name.txt')  # Удаление файлов
# os.makedirs('dir2')  # Создаем директорию

# Открываем файл
# subprocess.call(['xdg-open', filename]) # Открыть файл linux
# os.startfile(filename) # Открыть файл window



# Делаем проверку на три операционных системы с открытием файла
def open_file(filename):
    if "win" in sys.platform:
        os.startfile(filename)
    else:
        opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
        subprocess.call([opener, filename])
