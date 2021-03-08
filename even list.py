#write a program to delete all odd and negative no.s from list
list=[1,2,3,4,-5,6,-77,32,66,88,-32,-4,-8];
list2=[];
for i in list:
    if i%2==0 and i>=0:
        list2.append(i)
print("The updated list is: ",list2)
