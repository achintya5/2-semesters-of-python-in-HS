#Write a program to accept numbers from the user till they want and display their sum
s=0
c=0
while c>=0:
    n=int(input("Enter a number here: "))
    s=s+n
    a=input("Enter Y if you want to enter  more numbers: ")
    if a=='Y':
        c=c+1
    else:
        c=-1
print(s)

'''
sum=0
ans='y'
while ans=='y':
        n=int(input("Enter a number here: "))
        s=s+n
        ans=input("do you want to continue: y/n")
print(s)
'''


        
    
        
