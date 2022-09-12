#Check the number is divisible by 5 and 7
#Check the number is divisible by 5 only
#Check the number is divisible by 7 only
#Not divisible by 7 and 5

n=int(input("Enter the number"))
if(n%7==0 and n%5==0):
    print("Divisible by 5 and 7")
elif(n%7==0):
    print("Divisble by 7 only")
elif(n%5==0):
    print("Divisble by 5 only")
else:
    print("Not divisible by 7and 5")




