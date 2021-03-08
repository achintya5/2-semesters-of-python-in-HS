#Write a program to calculate BMI of a person after inputting its weight in kgs and height in metres and
#then print the nutritional status as per following table:

#Nutritional status       BMI cut-oo
#Underweight             <18.5
#Normal                      18.5 - 24.9
#Overweight                25-29.9
#Obese                         >=30

w=float(input("Enter your weight in kgs"))
h=float(input("Enter your height in metres"))

bmi=w/(h**2)
if bmi<18.5:
    print("UNDERWEIGHT")
elif bmi<24.9 and bmi>18.5:
    print("NORMAL")
elif bmi<29.9 and bmi>25:
    print("NORMAL")
else:
    print("OBESE")
