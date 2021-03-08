#accept list and display average of numbers
list1=list(input("Enter numbers separated by space here: "))
s=0
c=0
l=len(list1)
for i in range(0,l):
    s+=int(list1[i])
    c+=1

av=s/c
print("Average of the numbers is: ",av)
