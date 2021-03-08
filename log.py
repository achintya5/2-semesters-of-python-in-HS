#program to calculate log
a=int(input("Enter base for log here: "))
b=int(input("Enter number you want to calculate log for: "))
for i in range(0,100000000000000000,1):
    i/=100000
    if round(a**i,5)==b:
        log=i
        break
print("Log  of the number is: ", log)



