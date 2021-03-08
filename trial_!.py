t=(tuple())
n=int(input("How many numbers do you want to input?"))
for i in range(0,n):
    a=int(input("Enter here: "))
    t+=(a,)
print(t)
l=list(t)
m=min(l)
le=len(l)
for i in range(0,le):
    if l[i]==m:
        print("yes")
