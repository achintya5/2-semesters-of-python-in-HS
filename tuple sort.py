#Write a program to check if the elements in the first half of a tuple
#are sorted in ascending order or not.
n=int(input("Enter number of characters in tuple: "))
t=(tuple())
for i in range(0,n):
    a=int(input("Enter value for tuple: "))
    t+=(a,)
    
mid1=0
t2=sorted(t)
if n%2==0:
    mid=int(n/2)
    mid1=int(mid+1)
elif n%2!=0:
    mid=int((n+1)/2)

c=0
for i in range(0,mid):
    if t[i]==t2[i]:
        c+=1

if c==mid or c==mid1:
    print("Yes the first half of the tuple is sorted")
