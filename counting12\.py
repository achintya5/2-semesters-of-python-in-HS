#write a program to display factorial of a number

n=int(input("Enter a number here: "))
f=1
if n<0:
    print("Enter a positive value:")
elif n==0 or n==1:
    print(1)
else:
    for i in range(1,n+1):
        f=f*i
    print(f)
    
