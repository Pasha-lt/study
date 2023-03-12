# Declare a class named "Notes" and define the following attributes in it:
#
# uid: 1005435
# title: "Joke"
# author: "J.S. Bach"
# pages: 2
#
# Then, using the getattr() function, read and print the value of the author attribute.

class Notes:
    uid = 1005435
    title = "Joke"
    author = "J.S. Bach"
    pages = 2


print(getattr(Notes, "author"))