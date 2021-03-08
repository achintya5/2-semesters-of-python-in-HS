#Write a program to calculate the amount payable if money has been lent on simple interest.
p=int(input("Enter the principal amount you borrowed: "))
r=int(input("Enter the corresponding interest rate: "))
t=int(input("Enter the time for which you have borrowed in years: ")) 
i=(p*r*t)/100
a=p+i
print("The total payable amount is: ",a)
