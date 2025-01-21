yr=int(input("enter yr"))
if(yr%4==0 or yr%400==0 or yr%100==0):
    print("it is a leap yr")
else:
    print("it is not a leap yr")
