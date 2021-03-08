#Write a program that reads a string and then prints a string
#that capitalizes every other letter in the string eg.. passion becomes pAsSiOn

a=input("Enter a string here: ")

for i in range(0,len(a)):
    if i%2!=0:
        b=str(a[i].capitalize())
        c=a.replace(a[i],b)

print(c)
