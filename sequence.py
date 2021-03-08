#Write a program to generate the sequence: -5, 10, -15, 20, -25,...... upto n,
#where n is entered by user

n=int(input("Enter an integer here:"))
for i in range(1,n+1):
    a=5*i*((-1)**i)
    print(a)
