#accept string with some digits and find sum of those digits
a=input("Enter a string with a few digits here: ")
s=0
for i in a:
    if i.isdigit():
        b=int(i)
        s+=b
print("Sum of the numbers is: ",s)
