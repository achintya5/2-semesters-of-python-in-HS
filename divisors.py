#find divisors of a num
num=int(input("Enter an integer here: "))
d=1
while d<=num:
    if num%d==0:
        print(d)
        d=d+1
    else: d=d+1
    
