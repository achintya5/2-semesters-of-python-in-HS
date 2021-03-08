#print fibbonaci series
x=0
y=1
z=1
i=2
count=int(input("How many terms do you want to display: "))
print(x)
print(y)
print(z)
while i<count:
        x=y+z
        print(x)
        i=i+1
        y=x+z
        print(y)
        i=i+1
        z=x+y
        print(z)
        i=i+1
