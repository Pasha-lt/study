# The program is supposed to implement a parser for a string of data string into a certain output format.
# For this purpose, the following class has been declared:

# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq

# And it is supposed to be used as follows:
# res = Loader.parse_format("4, 5, -6", Factory)

# The expected output (in the res variable) is a list of integers.
# For example, for the given string, the output should be:

# [4, 5, -6]

# To implement this idea,
# it is necessary to declare the Factory class at the beginning of the program with two static methods:
#
# build_sequence() - to create an empty list (the method returns an empty list)
# build_number(string) - to convert the string string into an integer (the method returns the obtained integer value).
# Declare a class named Factory to obtain the desired output.
#
# P.S. The program should not print anything on the screen.


class Factory:
    @staticmethod
    def build_sequence():
        lst = []
        return lst

    @staticmethod
    def build_number(string):
        return int(string)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
