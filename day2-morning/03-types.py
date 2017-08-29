#!/usr/bin/env python

print "basic types..."

a_string = "This is a string"

an_integer = 7

i_as_s = str( an_integer)

a_real = float(5.689)

a_as_r = float( "5.689")




truthy = True
Falsy = False

for value in a_string, an_integer, a_real, truthy:
    print value, type( value )
    
    a_list = [ 1, 2, 3, 4, 5]
    a_tuple = (1, "foo", 3.2)
    
    print a_list, type( a_list)
    print a_tuple, type( a_tuple)
    
a_list[3] = 777
print a_list

#tuples are not mutable, cannot be edited with an equivilence
#a_tuple[3] = 777
#print a_tuple

another_list = list(a_list)

another_list[3] = 888
print another_list

print a_list

