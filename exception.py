#exception handling mechanism- 1.try-except
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
try:                                           #suspected code
    div=a/b
    print(div)
except:                                       #code to handle exception
    print("Divison by zero is not possible")
else:                                          #execute when there is no exception
    print("I am in else block")
#finally:                                      #execute for there or both execution and no execution
    #print("I am in else block")
