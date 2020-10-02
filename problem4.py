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

a=input("A value for a: ")
a=float(a)

b=input("A value for b: ")
b=float(b)

c=input("A value for c: ")
c=float(c)

a1=a**2
b1=b**2
c1=c**2

d=a1+b1

x=math.sqrt(a1+b1)
tolerance=x**0.02
z=x
x2=x+tolerance
x1=x-tolerance

if x1 <= x and x <= x2:
    print("that is a right triangle")

elif d<c1:
    print("that is an acute triangle")

elif d>c1:
    print("that is an obtuse triangle")