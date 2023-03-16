# Declare a class named Person with attributes:
#
# name: 'Pavlo Kostyshen'
# job: 'Programmer'
# city: 'Kyiv'
# Create an instance p1 of this class and check if it has a local property named job.
# Print True if it's present in the object p1 and False if it's not.

class Person:
    name = 'Pavlo Kostyshen'
    job = 'Programmer'
    city = 'Kyiv'


p1 = Person()
print("job" in p1.__dict__)
