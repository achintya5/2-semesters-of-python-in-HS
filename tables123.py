#table of a number by for loop
a=int(input("Enter an integer here:"))
s=1
for i in range(1,11):
    s=i*a
    print(a, "multiplied by ",i, "equals to: ",s)
