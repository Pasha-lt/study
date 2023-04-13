# Declare a class named Money and define the following variables and methods within it:
#
# a private local variable money (integer) for storing the amount of money (unique for each object of the Money class);
# a public method set_money(money) for passing a new value to the private local variable money
# (the change is made only if the check_money(money) method returns True);
# a public method get_money() for retrieving the current balance (money);
# a public method add_money(mn) for adding funds from an mn object of the Money class to the funds of the current object;
# a private class method check_money(money) for checking the correctness of the funds amount in the money parameter
# (returns True if the value is correct and False otherwise).
# The correctness check is based on the criterion: the money parameter must be an integer greater than or equal to zero.
#
# Example of using the Money class (do not include these lines in the program):
#


# mn_1 = Money(10)
# mn_2 = Money(20)
# mn_1.set_money(100)
# mn_2.add_money(mn_1)
# m1 = mn_1.get_money() # 100
# m2 = mn_2.get_money() # 120


class Money:
    def __init__(self, money):
        self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()

    def __check_money(self, money):
        return money >= 0 and type(money) is int




