#read integer, greater than 1000 and reverse it
n=int(input("Enter a 4 digit number greater than 1000: "))
if n>9999 or n<=1000:
    print("Please enter an appropriate number")
else:
    a=n//1000
    b=(n-1000)//100
    c=((n-1000)-(b*100))//10
    d=(((n-1000)-(b*100))-(c*10))//1
    reverse=(d*1000)+(c*100)+(b*10)+a
    print(reverse)
        
        
