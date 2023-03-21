# Declare a class called Translator (for translating from English to Ukrainian) with the following methods:
#
# add(self, eng, ukr) - to add a new pair of English and Ukrainian words
# (if the English word already exists, the new Ukrainian word is added as a synonym for translation,
# for example, go - йти, ходити, їхати); if the eng-ukr pair already exists,
# it should not be added again, for example: add('go', 'йти'), add('go', 'йти');
# remove(self, eng) - to remove a pair by the specified English word;
# translate(self, eng) - to translate from English to Ukrainian
# (the method should return a list of Ukrainian words corresponding to the translation of the English word,
# even if there is only one word in the list).
#
# All additions and deletions of pairs should be performed inside each specific object of the Translator class,
# i.e. the pairs should be stored locally inside the instances of the Translator class.
#
# Create an instance tr of the Translator class and call the add method for the following pairs:
#
# tree - дерево
# car - машина
# car - автомобіль
# leaf - лист
# river - річка
# go - йти
# go - їхати
# go - ходити
# milk - молоко
#
# Then, using the remove() method, remove the pair for the English word car.
# Use the translate() method to translate the word go.
# Print the result as a string of all Ukrainian words associated with the word go:
#
# Output format: йти, їхати, ходити


class Translator:

    def add(self, eng, ukr):
        if "tr" not in self.__dict__:
            self.tr = {}
        self.tr.setdefault(eng, [])
        if ukr not in self.tr[eng]:
            self.tr[eng].append(ukr)

    def remove(self, eng):
        self.tr.pop(eng, False)

    def translate(self, eng):
        return self.tr[eng]


tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "авто")
tr.add("car", "автомобіль")
tr.add("leaf", "листок")
tr.add("river", "річка")
tr.add("go", "йти")
tr.add("go", "їхати")
tr.add("go", "ходити")
tr.add("milk", "молоко")

tr.remove("car")
print(*tr.translate("go"))
