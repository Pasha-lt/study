# You are given a command to read data from the input stream in the following format:
# id, name, old, salary (separated by spaces) using the command:
#
# lst_in = list(map(str.strip, sys.stdin.readlines())) # reading a list of lines from the input stream

# For example:
# 1 Anton 35 120000
# 2 Taras 23 12000
# 3 Pavlo 13 1200
# ...
#
# Each line is an element of the lst_in list.
#
# You need to add two methods to the DataBase class:
#
# class DataBase:
# lst_data = []
# FIELDS = ('id', 'name', 'old', 'salary')
#
# select(self, a, b) - returns a list of elements from the lst_data list in the range [a; b] (inclusive) by their indexes (not id, but the indexes of the list); also, take into account that the b limit may exceed the length of the list.
# insert(self, data) - adds new data from the passed list of strings data to the lst_data list;
#
# Each record in the lst_data list should be represented as a dictionary in the format:
#
# {'id': 'number', 'name': 'name', 'old': 'age', 'salary': 'salary'}
#
# For example:
#
# {'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}
#
# Note: in this task, the number of elements in the line (separated by a space) always matches the number of fields in the FIELDS collection.
#
# P. S. Your task is only to add two methods to the DataBase class.
#
# Sample Input:
#
# 1 Anton 35 120000
# 2 Taras 23 12000
# 3 Pavlo 13 1200


import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for i in data:
            new_k = {}
            for number, k in enumerate(i.split()):
                new_k[self.FIELDS[number]] = k
            self.lst_data.append(new_k)
        # second solution
        # for x in data:
        #     self.lst_data.append(dict(zip(self.FIELDS, x.split())))
        
    def select(self, a, b):
        return self.lst_data[a:b + 1]


db = DataBase()
db.insert(lst_in)
