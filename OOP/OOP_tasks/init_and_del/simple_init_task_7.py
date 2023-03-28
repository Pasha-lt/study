# Declare in the program the Cart class, objects of which are created by the command:
#
# cart = Cart()
#
# Each object of the Cart class should have a local property 'goods' -
# a list of objects for purchase (objects of the Table, TV, Notebook, and Cup classes).
# Initially, this list should be empty.
#
# Declare the following methods in the Cart class:
#
# add(self, gd) - adding a product represented by the gd object to the cart;
# remove(self, indx) - removing a product from the cart by the indx index;
# get_list(self) - obtaining a list of goods from the cart in the form of a list of strings:
# ['<name_1>: <price_1>',
# '<name_2>: <price_2>',
# ...
# '<name_N>: <price_N>']
#
# Declare the following classes in the program to describe goods:
#
# Table - tables;
# TV - televisions;
# Notebook - notebooks;
# Cup - cups.
# Objects of these classes should be created by the command:
#
# gd = ClassName(name, price)
#
# Each object of the goods classes should have local properties:
#
# name - name;
# price - price.
# Create an object 'cart' of the Cart class in the program. Add two TVs (TV), one table (Table),
# two notebooks (Notebook), and one cup (Cup) to it. Come up with names and prices yourself.
#
# P.S. Nothing needs to be displayed on the screen, just create objects according to the specified requirements.
#


class Cart:

    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{x.name}: {x.price}' for x in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
table1 = Table("Jupiter", "700")
nout_1 = Notebook("Macbook air", "70 000")
nout_2 = Notebook("Macbook Pro", "105 000")
tv_1 = TV("Panasonic", "20 000")
tv_2 = TV("Samsung", "35 000")
cup_2 = Cup("Lipton", "50")
cart.add(table1)
cart.add(nout_1)
cart.add(nout_2)
cart.add(tv_1)
cart.add(tv_2)
cart.add(cup_2)
