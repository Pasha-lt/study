from functools import reduce

# вариант с использованием цикла для поиска факториала.
number = int(input("Введите число с которого мы будем брать факториал: "))
mult_number = 1
for i in range(1, number+1):
    mult_number *= i
print(mult_number)

# вариант с использованием reduce для поиска факториала.
number = int(input("Введите число с которого мы будем брать факториал: "))
factorial = reduce(lambda x,y:x*y, range(1, number+1))
print(factorial)
