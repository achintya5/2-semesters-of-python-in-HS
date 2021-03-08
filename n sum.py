#write a program to calculate and print sums of even and odd n natural numbers

num=int(input("Enter upper limit to calculate sum for: "))
os=0
es=0
count=1
while count<=num:
    if count%2==0:
        es=es+count
        count=count+1
    else:
        os=os+count
        count=count+1
print("Odd sum is: ",os)
print("Even sum is: ",es)
        
        
    
    

    

        
