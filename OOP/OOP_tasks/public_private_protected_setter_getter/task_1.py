# Declare a class named Clock and define the following variables and methods in it:
#
# private local variable time for storing the current time,
# an integer (unique for each object of the Clock class with an initial value of 0);
# public method set_time(tm) for setting the current time
# (assigns the value of tm to the private local property time, if method check_time(tm) returned True);
# public method get_time() for obtaining the current time from the private local variable time;
# private class method check_time(tm) for checking the correctness of the time in the variable tm
# (returns True if the value is correct and False otherwise).
# The correctness check is performed according to the criterion:
# tm must be an integer greater than or equal to zero and less than 100,000.
#
# The Clock class objects are meant to be used with the command:
#
# clock = Clock(time)
# Create an object clock of class Clock and set the time equal to 4530.
#
# P.S. No need to display anything on the screen.

class Clock:

    def __init__(self, tm):
        self.__time = 0
        if self.__check_time(tm):
            self.__time = tm

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @classmethod
    def __check_time(cls, tm):
        return type(tm) is int and tm >= 0 and tm < 100000


clock = Clock(4530)

