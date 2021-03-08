#Write a program to print
# whether a given character is an uppercase or a lowercase character
#or a digit or any other character.

ch=input("Enter a character: ")
if ch<='Z' and ch>='A':
    print("You entered an uppercase character ")
elif ch<='z' and ch>='a':
    print("You entered a lowercase character ")
elif ch>='0' and ch<='9':
    print("You entered a digit ")
else:
    print("You entered a special character")


