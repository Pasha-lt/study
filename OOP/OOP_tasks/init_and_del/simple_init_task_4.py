# Declare a class called TriangleChecker, objects of which can be created with the following command:
#
# tr = TriangleChecker(a, b, c)
#
# Here, a, b, c are the lengths of the sides of the triangle.
#
# In the TriangleChecker class, you need to declare the is_triangle() method, which would return the following codes:
#
# 1 - if at least one side is not a number (not float or int) or at least one number is less than or equal to zero;
# 2 - the specified numbers a, b, c cannot be the lengths of the sides of a triangle;
# 3 - the sides a, b, c form a triangle.
#
# Check the parameters a, b, c in this order.
#
# Read a line from the input stream containing three numbers separated by spaces with the command:
#
# a, b, c = map(int, input().split())
#
# Then, create an object tr of the TriangleChecker class and pass it the read values a, b, c.
# Call the is_triangle() method from the tr object and print the result on the screen (the code it will return).
#
# Sample Input:
#
# 3 4 5
# Sample Output:
#
# 3

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
            return 1
        elif not all(map(lambda x: x > 0, (self.a, self.b, self.c))):
            return 1
        elif self.a + self.b < self.c or self.a + self.c < self.b or self.c + self.b < self.a:
            return 2
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
