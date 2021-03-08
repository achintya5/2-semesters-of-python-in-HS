#dictionary to store phone numbers and print key-value pair

d1={'Atharv': 12345, 'Arnav': 123456}
for i in d1:
    print(i,d1[i])
#or
    print(dict.keys(d1), d1[i])

#write a program to read roll numbers and marks of four students
#and create a dictionary from it having roll numbers as keys

d2={}
for i in range(0,4):
    n=input("Enter your name here: ")
    m=input("Enter your marks here: ")
    d2[n]=m
print(d2)

