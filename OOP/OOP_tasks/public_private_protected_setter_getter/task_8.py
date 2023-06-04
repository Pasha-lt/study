# Declare the Car class in the program, where you implement an object property named model for writing and reading car model information from the local private variable __model.

# Declare the object property using the @property decorator. Also, in the object property model, the following checks should be implemented:

# the car model is a string;
# the length of the model string should be in the range [2; 100].
# If the check fails, the local property __model remains unchanged.

# Car class objects are supposed to be created with the command:

# car = Car()
# and then work with the object property, for example:

# car.model = "Toyota"
# P.S. Declare only the class in the program. Do not output anything to the screen.

class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model


    @model.setter
    def model(self, value):
        if type(value) and 2 <= len(value) <=100:
            self.__model = value
