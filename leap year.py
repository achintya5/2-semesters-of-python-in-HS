#leap year or not

year=int(input("Enter any year here: "))

if year%4==0 and year%100!=0:
    print("LEAP YEAR")
elif year%400==0:
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")
