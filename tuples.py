#Write a program to remove an element '3' from tuple t1=(1,2,3,4,5)
t1=(1,2,3,4,5)
l=list(t1)
l.remove(3)
t1=tuple(l)
print(t1)

#write a program to convert a number entered by the user into its corresponding number in words.
#For example, if the input is 985, then the output should be 'Nine Eight Five'
d={1:"one", 2:"two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8:"eight", 9: "nine", 0:"zero"}
k=''
num=str(input("enter a number here: "))
for i in num:
    i=int(i)
    k+= d[i]
    k+=' '
print(k)

#Write a program to check if a dictionary is empty.
d1={}
l=len(d1)
if l==0:
    print("Dictionary is empty")
