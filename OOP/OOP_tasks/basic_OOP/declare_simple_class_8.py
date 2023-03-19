# There is the following class for reading information from an input stream:
# import sys
#
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # reading a list of strings from the input stream
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res

# Which can then be used as follows:

# sr = StreamReader()
# data, result = sr.readlines()

# It is necessary to declare another class StreamData before the StreamReader class with a method:
#
# def create(self, fields, lst_values): ...
#
# which would receive the tuple FIELDS with the names of local attributes (passed to the 'fields' attribute)
# and a list of strings lst_in (passed to the 'lst_values' attribute) as input,
# and would create local properties in the StreamData object
# with field names from 'fields' and corresponding values from 'lst_values'.
#
# If the creation of local properties is successful, the create() method returns True; otherwise, it returns False.
# If the number of fields and the number of strings do not match, the create() method returns False,
# and local attributes should not be created.
#
# P.S. In the program, you only need to declare the StreamData class. Nothing else needs to be done.
# Sample Input:
# 10
# Python - Foundations of Mastery
# 512


import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        for number, key in enumerate(fields):
            setattr(self, key, lst_values[number])
        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # reading a list of strings from the input stream
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
