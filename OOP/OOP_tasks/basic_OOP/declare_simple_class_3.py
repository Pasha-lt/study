# Declare a class named TravelBlog and declare an attribute within it:
# total_blogs: 0
# Create an instance of this class named tb1, form two local properties in it:
# name: 'France'
# days: 6
# Increase the value of the total_blogs attribute of the TravelBlog class by one.
# Create another instance of the TravelBlog class named tb2, form two local properties in it:
# name: 'Italy'
# days: 5
# Increase the value of the total_blogs attribute of the TravelBlog class by one.

class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = "France"
tb1.days = 6

TravelBlog.total_blogs +=1

tb2 = TravelBlog()
tb2.name = "Italy"
tb2.days = 5

TravelBlog.total_blogs +=1