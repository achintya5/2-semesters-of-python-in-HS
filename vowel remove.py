#Write a program to remove vowels from a string
v="aeiouAEIOU"
a=input("Enter a string here: ")
for i in a:
    if i in v:
        a=a.replace(i,"")


print("Updated string is: ",a)
