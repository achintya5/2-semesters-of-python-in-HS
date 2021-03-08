num=int(input("Enter how many numbers do you want to see:"))
row=num
column=num
while row>=1 and row<=num+1:
    while column>=1 and column<=row+1:
        print(column, end="")
    print()
