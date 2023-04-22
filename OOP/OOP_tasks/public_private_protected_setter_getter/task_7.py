# Declare the EmailValidator class for checking the correctness of an email address. It is necessary to prohibit the creation of objects of this class: when creating instances, None should be returned, for example:

# em = EmailValidator() # None
# In the class itself, implement the following class methods (@classmethod):

# get_random_email(cls) - for generating a random email address in the format: xxxxxxx...xxx@gmail.com, where x is any valid character in an email (Latin letters, numbers, underscore, and dot);
# check_email(cls, email) - returns True if the email is written correctly and False otherwise.

# The correctness of the email string is determined by the following criteria:

# allowed characters: Latin alphabet, numbers, underscores, dots, and the at sign @ (one);
# the length of the email before the @ symbol should not exceed 100 (inclusive);
# the length of the email after the @ symbol should not be more than 50 (inclusive);
# at least one dot must follow the @ symbol;
# there should not be two dots in a row.
# Also, in the class, you need to implement a private static class method:

# is_email_str(email) - to check the type of the email variable, if it is a string, then return True, otherwise - False.

# The is_email_str() method should be used in the check_email() method before checking the correctness of the email. If the email parameter is not a string, then check_email() returns False.

# An example of using the EmailValidator class (you don't need to write these lines in the program):

# res = EmailValidator.check_email("sc_lib@list.ru") # True
# res = EmailValidator.check_email("sc_lib@list_ru") # False
# P.S. Only declare the class in the program. Do not output anything to the screen.

# Regenerate response

from random import randint
from string import ascii_lowercase, digits, ascii_uppercase

class EmailValidator():
    EMAIL_CHARS = ascii_lowercase + ascii_uppercase + digits + "_.@"
    EMAIL_RANDOM_CHARS = ascii_lowercase + ascii_uppercase + digits + "_"
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if not set(email) < set(cls.EMAIL_CHARS):
            return False

        s = email.split("@")
        if len(s) != 2:
            return False

        if len(s[0]) > 100 or len(s[1]) > 50:
            return False

        if "." not in s[1]:
            return False

        if email.count("..") > 0:
            return False
        return True

    @staticmethod
    def __is_email_str(email):
        return type(email) == str

    @classmethod
    def get_random_email(cls):
        n = randint(4, 20)
        length = len(cls.EMAIL_RANDOM_CHARS) - 1
        return "".join(cls.EMAIL_RANDOM_CHARS[randint(0, length)] for i in range(n)) + "@gmail.com"







