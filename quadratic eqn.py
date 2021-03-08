#Q. Write a program to calculate and
#print roots of a quadratic equation: ax2+bx+c=0

print("The quadratic equation is: ax^2+bx+c=0 ")
a=float(input("Enter value of a"))
b=float(input("Enter value of b"))
c=float(input("Enter value of c"))

discriminant=((b**2)-(4*a*c))**(1/2)
root1=(b*(-1)+(discriminant))/2*a
root2=(b*(-1)-(discriminant))/2*a
       
print("The roots of the equation are: ",root1, "and", root2)



