#write a python program to calculate in how many days a work will be calculated by three persons
#a, B and C together. A, B, C take x days,y days and z days respectively to do the job alone.
#the formula to calculate the number of days if they work together
#is xyz/(xy+yz+xz) days where x,y and z are given as input to the program.

a=int(input('Enter days taken by A: ' ))
b=int(input('Enter days taken by B: ' ))
c=int(input('Enter days taken by C: ' ))

x=a+b+c
y=a*b+b*c+c*a
print('days taken by a,b and c together= ' , x/y)
