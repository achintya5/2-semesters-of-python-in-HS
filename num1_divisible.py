#write a python programme to accept two numbers from the user and
#check if the first number is divisible by second number
#then display a message

num1=int(input("Enter  a number here: "))
num2=int(input("Enter  another number here: "))

if num1%num2==0:
    print("num1 is divisible by num2")
else:
    print("num1 is not divisible by num2")
