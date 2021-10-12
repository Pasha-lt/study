from dataclasses import dataclass

#############################################
# По умолчанию у Data Class есть методы __init__, __repr__ и __eq__, поэтому их не нужно реализовывать самостоятельно.
@dataclass()
class Coordinate:
    x: int
    y: int
    z: int
    pi: float = 3.14  # можно присвоить в классе

    @property
    def area(self):
        return self.pi * (self.x ** 2)


a = Coordinate(4, 5, 3)
a.x = 1000
print(a)  # Coordinate(x=1000, y=5, z=3, pi=3.14)
print(a.area)  # 3140000.0
#############################################

#############################################
# использую frozen=True мы можем запретить изменять значения
@dataclass(frozen=True)
class CircleArea:
    r: int
    pi: float = 3.14

    @property
    def area(self):
        return self.pi * (self.r ** 2)


a_1 = CircleArea(2)
print(a_1)  # CircleArea(r=2, pi=3.14)
# a_1.r = 10  #dataclasses.FrozenInstanceError: cannot assign to field 'r'
#############################################



#############################################
# Вариант с наследованием сначала класический вариант потом с Data Class
##### Классический вариант 10 строк #####
class Employee:
    def __init__(self, name, lang):
        self.name = name
        self.lang = lang


class Developer(Employee):
    def __init__(self, name, lang, salary):
        super().__init__(name, lang)
        self.salary = salary

    def __str__(self):
        return f'Developer {self.name=} {self.lang=} {self.salary=}'


Alex = Developer('Alex', 'Python', 5000)
print(Alex)  # Developer self.name='Alex' self.lang='Python' self.salary=5000
##### Классический вариант конец#####
##### вариант с Data Class 7 строк #####
@dataclass
class Employee:
    name: str
    lang: str = 'Python'


@dataclass
class Developer(Employee):
    salary: int = 0


Alex = Developer('Alex', 'Python', 5000)
print(Alex)  # Вернется: Developer(name='Alex', lang='Python', salary=5000)
##### вариант с Data Class конец#####
