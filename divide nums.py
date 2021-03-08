#Write a program to input a 6 digit number and
#divide it into three 2 digit numbers.

x=int(input("Enter a six digit number here: "))
if x>=100000 and x<=999999:
    num1=int(x/10000)
    num2=int(x//12345)
    num3=int(x%123)
else:
    print("Please enter a 6 digit number ONLY")
print("The divided numbers are :", num1, num2, num3)
