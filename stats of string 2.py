a=input("Enter a string here: ")
l=len(a)
d=0
s=l
c=0
uc=0
lc=0

for i in a:
    if i.isalpha:
            print(i)
            if i.isdigit():
                d+=1
            elif i.isupper():
                uc+=1
            elif i.islower():
                lc+=1
    elif i.isalpha==False:
        c+=1
s=s-(d+c)

print("Special characters- ",c)
print("Alphabets- ",s)
print("Numbers- ",d)
print("Upper case letters- ",uc)
print("Lower case letters- ",lc)
        
