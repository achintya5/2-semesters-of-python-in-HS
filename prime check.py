#check if prime number
n=int(input("Enter a number here: "))
d=2

if n==1:
    print("It is neither prime nor composite")
        
elif n==2:
     print("It is prime")
        
else:
      if  d<=n:
          if n%d==0:
             print("It is a composite number")
          while n%d!=0:
              d=d+1
              if n%d==0:
                  print("It is a composite number")
              elif n==d and n%d!=0:
                  print("It is a prime")
           
      
            
            
            
        
        
        
