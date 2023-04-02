# The program declares the variable TYPE_OS and two following classes:
#
# TYPE_OS = 1 # 1 - Windows; 2 - Linux
#
# class DialogWindows:
# name_class = "DialogWindows"
#
# class DialogLinux:
# name_class = "DialogLinux"
#
# It is necessary to declare a third class named Dialog, which would create objects with the command:
#
# dlg = Dialog(<name>)
# Here, <name> is a string that is stored in the local name property of the dlg object.
#
# The Dialog class should create objects of the DialogWindows
# class if the TYPE_OS variable is 1 and objects of the DialogLinux class if the TYPE_OS variable is not equal to 1.
# At the same time, the TYPE_OS variable can be changed in subsequent lines of the program.
# Keep this in mind when declaring the Dialog class.
#
# P.S. The program should not output anything to the screen. Only declare the Dialog class.

TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    obj = None

    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
        else:
            obj = super().__new__(DialogLinux)
        obj.name = args[0]
        return obj


dlg = Dialog(1)
