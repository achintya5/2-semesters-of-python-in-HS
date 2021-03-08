#ask user to display perimeter or area
#menu driven program

rad=int(input("Enter radius for the circle"))
choice=int(input("Enter 1 for perimeter or 2 for area"))
area=3.14*((rad)**2)
perimeter=2*3.14*rad
if choice==1:
    print("The perimeter is: ", perimeter)
elif choice==2:
    print("The area is: ", area)
else:
    print("Please enter either 1 or 2")
