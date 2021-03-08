#write a program that prints min and max of 5 nums
min=0
max=0
for i in range(1,6):
    a=int(input("Enter an integer here:"))
    if a>=max:
        max=a
    elif a<max:
        min=a

 

print("Largest number is:", max)
print("Smallest number is:", min)
