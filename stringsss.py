#Write a program to accept two strings. if string1 is contained in string2,
#then create a third string with first four characters of string2 added with word "Restore".


a=input("Enter a string here: ")
b=input("Enter a string here: ")
if b in a:
    for b in a:
        c=b[0:4:1]
        print(c,' ',"Restore")
        break
else:
    print("Condition not fulfilled")
