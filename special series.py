#Write python code to print pattern
#1
#1 3
#1 3 5
#1 3 5 7

a=1
n=int(input("How many numbers do you want to print:"))
i=1
print(a)
b=a+2
x=a,b
print(x)
    
while i<n:
    b=b+2
    x=x,b
    print(x)
    i=i+1
    
    
    
