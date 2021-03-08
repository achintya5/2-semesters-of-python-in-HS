#program to input a string and check if it is a palindrome using slicing

a=input("Enter a string here:")
r=a[::-1]

print(r)
if r==a:
    print("Its a palindrome.")
else:
    print("Not a palindrome")
