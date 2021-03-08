#Write a program that accepts the mass of an object
#and determines its energy.
m=int(input("Enter the mass of the body in kgs:" ))
c=3*(10**8)
e=m*(c**2)
print(e)
#or
import math
m=int(input("Enter the mass of the body in kgs:" ))
c=3*pow(10,8)
e=m*pow(c,2)
print(e)
