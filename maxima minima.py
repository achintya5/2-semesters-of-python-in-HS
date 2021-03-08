#Write a program to input three numbers and
#display the largest and smallest number.

x=int(input("Enter a number here"))
y=int(input("Enter another number here"))
z=int(input("Enter another number here"))

if x>y and x>z:
    maxima=x
    if y>z:
        mterm=y
        minima=z
    else:
        mterm=z
        minima=x
        
elif y>x and y>z:
    maxima=y
    if x>z:
        mterm=x
        minima=z
    else:
        mterm=z
        minima=x
    
elif z>x and z>y:
    maxima=z
    if y>x:
        mterm=y
        minima=x
    else:
        mterm=z
        minima=x


print("Largest number is:", maxima)
print("Smallest number is:", minima)
