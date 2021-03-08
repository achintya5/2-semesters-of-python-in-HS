#accept no.s from user upto limit by user,
#if the number is even then add to list
n=int(input("How many numbers do you want to enter? "))
list=[];
for i in range(0,n):
    a=int(input("Enter the number here: "))
    if a%2==0:
        list.append(a)

print(list)

