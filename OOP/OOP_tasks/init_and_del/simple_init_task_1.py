# Declare a class called Money so that objects of this class can be created as follows:
#
# my_money = Money(100)
# your_money = Money(1000)
#
# Here, when creating objects, the amount of money that should be stored in the local property (attribute)
# money of each instance of the class is specified.
#
# P.S. There is no need to output anything on the screen in the program.

class Money:

    def __init__(self, money):
        self.money = money


my_money = Money(100)
your_money = Money(1000)
