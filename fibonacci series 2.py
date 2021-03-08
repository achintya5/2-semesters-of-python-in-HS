#print fibonaaci series

a=0
b=1
count=int(input("How many numbers do you want to print: "))

for i in range(0,count):
    print(a)
    print(b)
    a=a+b
    b=a+b
  
