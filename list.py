

#accept list and display largest number in the list
n=int(input("How many numbers due you want to print"))
list=[]
for i in range(0, n): 
    b = int(input("Enter the number here:")) 
    list.append(b)


max=list[0]
for i in list:
    if i>max:
        max=i
print(max)

        
