# In the program, it is planned to implement a parser for a string into a specific output format.
# For this, the following class is declared:

# class Loader:
#     def parse_format(self, string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq

# And it is planned to use it as follows:

# ld = Loader()
# res = ld.parse_format("4, 5, -6.5", Factory())

# The expected output (in the variable res) is a list of real numbers.
# For example, for the given string, it should be:

# [4.0, 5.0, -6.5]
#
# To implement this idea, it is necessary to declare the Factory class at the beginning of the program with two methods:
#
# build_sequence(self) - to create an initial empty list (the method should return an empty list);
# build_number(self, string) - to convert the passed string argument into a real number
# (the method should return the resulting float value).
# Declare the Factory class to obtain the desired result as output.
#
# P.S. The program should not print anything to the screen.


class Factory:
    def build_sequence(self):
        self.new_list = []
        return self.new_list

    def build_number(self, string):
        return float(string)


class Loader:
    def parse_format(self, string, factory):
        seq = Factory.build_sequence(self)
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


ld = Loader()
s = input()
res = ld.parse_format(s, Factory())
