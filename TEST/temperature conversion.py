#Temperature conversion
print('Temperature conversion')
print('1.Celcius to Fahrenheat')
print('2.Fahrenheat to celcius')
ch=int(input("Enter the choice"))
if(ch==1):
    cel=float(input("Enter the temperature in celcius"))
    f=(9/5)*cel+32
    print("Temperature in farhenheat=",round(f,2))
elif(ch==2):
    fah=float(input("Enter the temperature in fahrenheat"))
    c=(5/9)*fah-32
    print("Temperature in celcius=",round(c,2))
else:
    print("Wrong Input")