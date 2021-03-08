#read email id of n students and store in tuple
#create 2 more tupples, one for usernames and second to store domain names
#from email ids, print all three tupples
t=(tuple())
user=(tuple())
domain=(tuple())
n=int(input("How many email IDs do you want to input?"))
for i in range(0,n):
    a=input("Enter email here: ")
    t+=(a,)

t=list(t)
for k in range(0,len(t)):
    l=(str(t[k]).split("@"))
    user+=(l[0],)
    domain+=(l[1],)

print(user)
print(domain)
