# Задача на паттерн Компоновщик
# Рассмотрите код ниже. У нас есть два класса SingleValue и ManyValues. SingleValue хранит одно числовое значение, 
# а ManyValues может хранить как числовые значения так и SingleValue объекты.
# Вам нужно добавить и к SingleValue и к ManyValues свойство sum, которое возвращает сумму всех значений, хранимых в объекте.
# При этом вам надо реализовать единственное свойство sum! То есть, не следует добавлять sum физически в оба класса.
# Вот пример юнит-теста кода, к которому вам надо прийти:


# class FirstTestSuite(unittest.TestCase)
#    def test(self):
#        single_value = SingleValue(11)
#        other_values = ManyValues()
#        other_values.append(22)
#        other_values.append(33)

#        all_values = ManyValues()
#        all_values.append(single_value)
#        all_values.append(single_values)

#        self.asserEqual(all_values.sum, 66)


#class SingleValue:
#    def __init__(self, value):
#        self.value = value

#class ManyValues(list):
#    pass


from abc import ABC
from collections.abc import Iterable


class ValueContainer(Iterable, ABC):
    @property
    def sum(self):
        result = 0
        for c in self:
            for i in c:
                result += i
        return result


class SingleValue(ValueContainer):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, ValueContainer):
    pass
