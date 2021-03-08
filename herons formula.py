#a triangle has three sides a, b, c as 17, 23, 30.
#calculate and display its area using heron's formula.

import math
a=17
b=23
c=30
s=(a+b+c)/2
a=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area is: ",a)

'''
import math
a=int(input("Enter one side of the triangle: "))
b=int(input("Enter another side of the triangle: "))
c=int(input("Enter another side of the triangle: "))
s=(a+b+c)/2
a=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area is: ",a)
'''
