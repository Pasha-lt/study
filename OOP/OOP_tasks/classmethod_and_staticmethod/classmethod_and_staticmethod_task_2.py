# The following class is declared in the program to work with login/password input forms:
#
# class FormLogin:
# def init(self, lgn, psw):
# self.login = lgn
# self.password = psw
#

# def render_template(self):
#     return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
# Which is supposed to be used as follows:
#
# login = FormLogin(TextInput("Login"), PasswordInput("Password"))
# html = login.render_template()
#
# It is necessary to declare the TextInput and PasswordInput classes, the objects of which are formed by the commands:
#
# login = TextInput(name, size)
# psw = PasswordInput(name, size)
#
# In each object of these classes, the following local properties should be present:
#
# name - the name of the field (stores the passed name, for example, "Login" or "Password");
# size - input field size (integer, default 10).
#
# The TextInput and PasswordInput classes should also have the method:
#
# get_html(self) - returns the generated HTML string in the format
# (1st string for the TextInput class; 2nd - for the PasswordInput class):
#
# <p class='login'><field name>: <input type='text' size=<field size> />
# <p class='password'><field name>: <input type='text' size=<field size> />
# For example, for the login field:
#
# <p class='login'>Login: <input type='text' size=10 />
# The TextInput and PasswordInput classes should also have the class method (@classmethod):
#
# check_name(cls, name) - to check the correctness of the passed field name (should be called in the initializer)
# according to the following criteria:
#
# the length of the name is at least 3 characters and no more than 50;
# only Ukrainian and English alphabet characters, digits, and spaces can be used in names.
# If the check fails, an exception should be raised using the command:
#
# raise ValueError("Invalid field name")
#
# For checking the permissible characters in each class, the attribute CHARS_CORRECT should be defined:
#
# CHARS = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя " + ascii_lowercase
# CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
# As per the task, only the TextInput and PasswordInput classes need to be declared with the corresponding functionality.
# Nothing else.
#
# P.S. In this task, there will be duplication of code in the TextInput and PasswordInput classes.
# At this stage, it is normal.


from string import ascii_lowercase, digits


class TextInput:
    CHARS = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


    @classmethod
    def check_name(cls, name):
        if type(name) != str or len(name) < 3 or len(name) > 50:
            raise ValueError("Invalid field name")
        if not set(name) < set(cls.CHARS_CORRECT):
            raise ValueError("Invalid field name")

class PasswordInput:
    CHARS = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


    @classmethod
    def check_name(cls, name):
        if type(name) != str or len(name) < 3 or len(name) > 50:
            raise ValueError("Invalid field name")
        if not set(name) < set(cls.CHARS_CORRECT):
            raise ValueError("Invalid field name")





class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


login = FormLogin(TextInput("Login"), PasswordInput("Password"))
html = login.render_template()