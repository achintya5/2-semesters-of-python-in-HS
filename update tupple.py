#A tuple t1 stores (11,21,31,42,51) where its second last element is mistyped.
#Write a program to correct its second last element as 41.

t1=(11,21,31,42,51)

"""t2=()
for i in range(0,len(t1)-2):
    t2+=(t1[i],)
t2+=(41,51)
print(t2)"""

#method 2
t1=list(t1)
t1[-2]=41
print(t1)
