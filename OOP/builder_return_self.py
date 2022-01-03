# Указав что мы возвращаем self это дает нам возможность несколько раз вызывать метод
# и тем самым несколько раз его использовать, запись через точку.

class Person:
    def __init__(self, name):
        self.name = name

    def add_grade(self, grade):
        # Указав что мы возвращаем self это дает нам возможность несколько раз вызывать метод, запись через точку.
        self.name = f'{self.name} {grade}'
        return self

    def __str__(self):
        return self.name


a = Person("You")
a.add_grade("senior").add_grade("developer")  # Вариант дописывания
print(a)
