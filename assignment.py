# #menu driven program
# 1.add
# 2.subtract
# 3.multiplication
# 4.division
# 5.Exit
#
# enter your choice
# read two numbers
# sum display
#
# enter your choice=2
# read two numbers
# difference display
#
# enter your choice=5
#
# while True:
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')
print('5.Exit')
n=int(input('Enter the choice'))
sum=0
diff=0
prod=0
quo=0

if(n==1):
    a1=int(input("enter the first number"))
    a2=int(input("enter the second number"))
    sum=a1+a2
    print("Sum is",sum)
elif(n==2):
    a1=int(input("enter the first number"))
    a2=int(input("enter the second number"))
    diff=a1-a2
    print("Difference is",diff)
elif(n==3):
    a1=int(input("enter the first number"))
    a2=int(input("enter the second number"))
    prod=a1*a2
    print("Product is",prod)
elif(n==4):
    a1=int(input("enter the first number"))
    a2=int(input("enter the second number"))
    quo=a1/a2
    print("Quotient is",quo)
else:
    print("No value")


