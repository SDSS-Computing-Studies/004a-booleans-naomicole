#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"

import math 
a=input("Enter value for a: ")
a=float(a)

b=input("Enter value for b: ")
b=float(b)

c=input("Enter value for c: ")
c=float(c)

x=math.pow(b,2)-4*a*c
