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


# еще один вариант
my_dict = {"name":"Pasha", "age":"198", "position":"employer"}

@dataclass
class Data:
    name: str
    age: int
    position: str
    

z = Data(name=my_dict["name"], age=my_dict["age"], position=my_dict["position"] )

print(z.name, z.age, z.position) # Pasha 198 employer
print(my_dict["name"], my_dict["age"], my_dict["position"]) # Pasha 198 employer

assert z.name == my_dict["name"]
assert z.age == my_dict["age"]
assert z.position == my_dict["position"]


# Вариант когда у нас есть вложеность.
from dataclasses import dataclass

my_dict = [
    {"животное": "собака", "окрас": "коричневый", "вес": 10, },
    {"животное": "корова", "окрас": "черно-пестрая", "вес": 300},
    {"животное": "коза", "окрас": "белая", "вес": 40}
]


@dataclass()
class FeatureAnimal:
    animal_type: str
    color: str
    weight: int


@dataclass()
class AnimalData:
    data: [FeatureAnimal]


def foo():
    list_with_animal = []
    for i in my_dict:
        all_animals = FeatureAnimal(
            animal_type=i["животное"],
            color=i["окрас"],
            weight=i["вес"]
        )
        
        list_with_animal.append(all_animals)
    z = AnimalData(data=list_with_animal)
    return z


z = foo()

assert z.data[0].color == my_dict[0]["окрас"]
assert z.data[1].animal_type == my_dict[1]["животное"]
assert z.data[2].weight == my_dict[2]["вес"]

