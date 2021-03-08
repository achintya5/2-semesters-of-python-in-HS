#write a programme that reads 2 numbers and an arithmetic operator and displays the result

x=int(input("Enter a number here"))
y=int(input("Enter another number here"))
print(''' Enter + for addition
      Enter - for subtraction
      Enter * for multiplication
      Enter // for quotient
      Enter % for remainder'''
op=input("Enter the operator you want to use")
if op="+":
    print(num1+num2)
elif op="-":
    print(num1-num2)
elif op="*":
    print(num1*num2)
elif op="//":
    print(num1//num2)
elif op="%":
    print(num1%num2)
else:
    print("Please enter valid operator")
       
