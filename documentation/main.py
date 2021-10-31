import lib

# help(foo)  # Выводит название метода и докстринг - работает без принта.метода
# print(lib.foo.__doc__)  # Выводит только док стрингу
# print(print.__doc__)  # Выводит только док стрингу
# print(lib.bar.__doc__)
# print(lib.value)
# help(lib)

# help(lib.Main)
# Help on class Main in module req:
# class Main(builtins.object)
#  |  Class Main - docstring
#  |
#  |  Methods defined here:
#  |
#  |  first_method(self)
#  |      first_method print 'AAAAA'
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
############################################################

help(lib.bar)


# print(lib.Main.first_method.__doc__)  # first_method print 'AAAAA'
