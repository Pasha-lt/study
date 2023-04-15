# Declare a class named Book in Python programming with the following set of setters and getters:
#
# set_title(self, title) - write the title value to the local private property __title of the Book class objects;
# set_author(self, author) - write the author value to the local private property __author of the Book class objects;
# set_price(self, price) - write the price value to the local private property __price of the Book class objects;
# get_title(self) - get the value of the local private property __title of the Book class objects;
# get_author(self) - get the value of the local private property __author of the Book class objects;
# get_price(self) - get the value of the local private property __price of the Book class objects;
#
# Book class objects are expected to be created with the command:
#
# book = Book(author, title, price)
# In this case, each object should have private local properties:
#
# __author - a string with the author's name;
# __title - a string with the book title;
# __price - an integer with the book price.
#
# P.S. Only the class needs to be declared in the program. No need to print anything on the screen.


class Book:
    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price
