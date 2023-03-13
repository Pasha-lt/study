# Please declare a class named "Dictionary" and define the following attributes in it:
#
# ukr: "Пайтон"
# eng: "Python"

# Then, using the getattr() function, read and print the value of the ukr_word attribute to the screen.
# If this attribute is not present in the class, the getattr() function should return the boolean value False.

class Dictionary:
    ukr = "Пайтон"
    eng = "Python"

print(getattr(Dictionary, "ukr_word", False))
print(getattr(Dictionary, "Пайтон", True))