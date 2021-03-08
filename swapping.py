#swap three numbers

a=int(input('Enter number 1: '))
b=int(input('Enter number 2: '))
c=int(input('Enter number 3: '))

print('Numbers before swapping are: ',a,b,c)
a,b,c=b,c,a
print('Numbers after swapping are: ' , a,b,c)
