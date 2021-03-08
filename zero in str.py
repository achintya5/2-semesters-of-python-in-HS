#Write a program to input an integer and check if it contains any 0 in it.
a=int(input("Enter a number here:"))
s=str(a)
for i in s:
    if i=="0":
        print("Yes there is a zero")
        break
    

        
