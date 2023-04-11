# Declare a messenger class named Viber. This class should have the following methods:
#
# add_message(msg) - adds a new message to the list of messages;
# remove_message(msg) - removes a message from the list;
# set_like(msg) - toggle a like for the message msg
# (i.e., change the fl_like attribute of the msg object: if there is no like, it is set, if there is one, it is removed);
# show_last_message(number) - displays the last messages;
# total_messages() - returns the total number of messages.
#
# These methods are meant to be used as follows (do not write these lines in the program):
#
# msg = Message("Hello everyone!")
# Viber.add_message(msg)
# Viber.add_message(Message("This is a Python OOP course."))
# Viber.add_message(Message("What do you think about it?"))
# Viber.set_like(msg)
# Viber.remove_message(msg)
# The Message class (also to be declared)
# allows you to create message objects with the following set of local properties:
#
# text - message text (string);
# fl_like - whether a like is set or not set for the message
# (boolean value True - if there is a like and False - otherwise, initially False);
#
# P.S. How to store the list of messages is up to you.

class Viber:
    message_storage = {}

    @classmethod
    def add_message(cls, msg):
        cls.message_storage[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        cls.message_storage.pop(id(msg))

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, numbers):
        for message in tuple(cls.message_storage.values())[-numbers]:
            print(message)

    @classmethod
    def total_messages(cls):
        return len(cls.message_storage)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like







