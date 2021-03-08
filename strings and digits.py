a=input("Enter a string here: ")
d=0
s=len(a)
for i in a:
    if i.isdigit():
        d=d+1
s=s-d
print("No. of strings= ",s)
print("No. of digits= ",d)

