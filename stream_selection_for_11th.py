#write a python program to accept the % score by student in class 10.
#if score is more than 90% print message that student is eligible for science#\
#if score b/w 70 to 90% print message that child is eligible for commerce
#else the child can opt for humanities

score=int(input("Enter your class 10 score in percentage here: "))
if score>=90:
    print("You are eligible for choosing science stream")
elif score>=70 and score<=90 :
    print("You are eligible for choosing commerce stream")
else :
    print("You are eligible for choosing humanities stream")
