#exception -MULTIPLE ERRORS
try:
    a=int(input("Enter the first number"))       # error varunnath eth line ano athellam try ude ullil varanam
    b=int(input("Enter the second number"))

    div=a/b
    print(x)        #NAME ERROR      ith just kanikan vendi aanu program
    print(div)
except NameError:
    print("Varible is not assigned")
except ZeroDivisionError:
    print("Divison by zero is not possible")
except ValueError:
    print("Expecting numeric values")