#accept num and see if its a perfect num
#perfect num=sum of divisors

num=int(input("Enter an integer here: "))
d=1
s=0
while d<num:
    if num%d==0:
        s=s+d
        d=d+1 
    else: d=d+1

if (s)==num:
    print("Perfect num")
else:
    print("Imperfect number")
    
