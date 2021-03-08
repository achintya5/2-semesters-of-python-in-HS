#Write a program to check if the minimum element of a tuple lies at the middle position
#of the tuple

n=int(input("Enter number of characters in tuple1: "))
t1=(tuple())
for i in range(0,n):
    a=int(input("Enter value for tuple: "))
    t1+=(a,)

length=len(t1)
if length%2==0:
    mid=length//2
else:
    mid=(length+1)/2

b=min(t1)
for i in t1:
    if t1[i]==int(b):
        print("Yes the minimum value lies in the middle")
        break
