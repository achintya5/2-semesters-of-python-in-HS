#count no. of times a character occurs in a string
s=input("Enter a string here: ")
c=input("Enter a single character here: ")
t=0
for i in s:
    if i==c:
        t+=1
print(t)
