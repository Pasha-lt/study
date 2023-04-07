# Declare a CardCheck class to verify the correctness of information on plastic cards.
# This class should have the following methods:
#
# check_card_number(number) - checks a string with a card number and returns
# a boolean value True if the number is in the correct format and False otherwise.
# The number format is as follows: XXXX-XXXX-XXXX-XXXX, where X is any digit (from 0 to 9).
# check_name(name) - checks the name string with the card user's name.
# Returns a boolean value True if the name is written correctly and False otherwise.
#
# The name format: two words (first and last name) separated by a space, written in uppercase Latin letters and digits.
# For example, "name surname".
#
# The CardCheck class is intended to be used as follows (do not write these lines in the program):
#
# is_number = CardCheck.check_card_number("1234-5678-9012-0000")
# is_name = CardCheck.check_name("name surname")
# To check the allowable characters, the following attribute should be specified in the class:
#
# CHARS_FOR_NAME = ascii_lowercase.upper() + digits
# Consider how to declare the check_card_number and check_name methods correctly
# (using the @classmethod and @staticmethod decorators).
#
# P.S. In the program, just declare the class. No need to display anything on the screen.


from string import ascii_lowercase, digits
import re


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        pattern = r'\d{4}-\d{4}-\d{4}-\d{4}$'
        if re.match(pattern, number):
            return True
        else:
            return False

    @staticmethod
    def check_name(name):
        pattern = r'^[A-Z]+\s[A-Z]+$'
        if re.match(pattern, name):
            return True
        else:
            return False
