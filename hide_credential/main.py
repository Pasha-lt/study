import os

# Первый способ сохранение в виртуальном окружении
# Либо в пайчарме edit configuration ...=>Environment variables пишем и тогда с пайчарма доступна
# c пайчармом будет храниться и после прирывания сессии.
# либо в терминале пишем export var=34 где вар переменая которую будем передавать в os.getenv а 12
# значение. Если мы записыаем через терминал то вызывать программу также нужно через терминал.
# Если ввести креденшиалы через терминал то они будут работать пока терминальная сесия открыта.
var = os.getenv('var') #edit configuration ...=>Environment variables
print(var) #andrey


# Второй способ используем библиотеку dotenv. нужно создать файл '.env' и в нем записывать
# все переменные также нужно запустить метод
#pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()
var2 = os.getenv('var2') #edit configuration ...=>Environment variables
print(var2) #вторая_переменная
