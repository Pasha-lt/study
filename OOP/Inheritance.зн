class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Имя человека - {self.name}, возраст - {self.age}'


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)# == Person.__init__(self, name, age)
        self.course = course

    def __str__(self):
        # по факту мы вызываем магический метод из родтельского класса. 
        # return f"{Person.__str__(self).replace('человека', 'студента')}, курс №{self.course}"
        return f"{super().__str__().replace('человека', 'студента')}, курс №{self.course}"


p = Person('Андрей', 44)
print(p) #Имя человека - Андрей, возраст - 44
s = Student('Андрей', 44, 2)
print(s) #Имя студента - Андрей, возраст - 44, курс №2
