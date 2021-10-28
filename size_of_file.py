import sys
val1="Python"
val2=100
#first solution we need import sys 
print(sys.getsizeof(val1)) #55
print(sys.getsizeof(val2)) #28

# second solution 
print(val1.__sizeof__()) #55
print(val2.__sizeof__()) #28
