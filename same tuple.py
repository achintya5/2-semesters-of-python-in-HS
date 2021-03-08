#Write a program to input a tuple and check if it contains all elements as same.
n=int(input("Enter number of characters in tuple: "))
t=(tuple())
for i in range(0,n):
    a=int(input("Enter value for tuple: "))
    t+=(a,)
c=t[1]
count=0
for k in range(0,len(t)):
    if t[k]==c:
        count+=1
if count==len(t):
    print("All the elements are same")
else:
    print("All elements aren't the same")
