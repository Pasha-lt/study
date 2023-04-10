# Declare a class AppStore - an online store for iOS device applications.
# This class should implement the following methods:
#
# add_application(self, app) - adding a new app to the store;
# remove_application(self, app) - removing an app from the store;
# block_application(self, app) - blocking an app (sets the local property blocked of the app object to True);
# total_apps(self) - returns the total number of applications in the store.
#
# The AppStore class is intended to be used as follows (do not write these lines in the program):
#
# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# store.remove_application(app_youtube)
# Here, Application is a class describing the added application with the specified name.
# Each object of the Application class should contain local properties:
#
# name - the name of the application (string);
# blocked - a boolean value (True - the application is blocked; False - not blocked, initially False).
#
# How to store the list of applications in objects of the AppStore class is up to you.
#
# P.S. You only need to declare the classes with the specified functionality in the program.


class AppStore:
    def __init__(self):
        self._STORAGE = {}

    def add_application(self, app):
        self._STORAGE[app.name] = app

    def remove_application(self, app):
        self._STORAGE.pop(app.name)

    def block_application(self, app):
        self._STORAGE[app.name].blocked = True

    def total_apps(self):
        return len(self._STORAGE)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked
