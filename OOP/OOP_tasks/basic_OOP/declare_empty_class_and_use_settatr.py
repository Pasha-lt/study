# Declare an empty class named Car. Use the setattr()
# function to add the following attributes to the class:
#
# model: "Toyota"
# color: "Pink"
# number: "P111UU77"

# Print the value of the color attribute to the screen using the dict dictionary of the Car class.

class Car:
    pass

setattr(Car, "model", "Toyota")
setattr(Car, "color", "pink")
setattr(Car, "number", "P111UU77")

print(Car.__dict__.get("color"))

