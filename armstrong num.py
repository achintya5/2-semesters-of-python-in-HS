#check if num is armstrong num
num=int(input("Enter an integer here: "))
s=0
a=num
while a>0:
    b=a%10
    s=s+(b**3)
    b=b//10
if num==s:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
