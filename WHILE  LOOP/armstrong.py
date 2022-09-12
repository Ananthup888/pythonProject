#armstrong

n=int(input("Enter the number"))
sum=0
num=n
while(n>0):
    d=n%10
    sum=sum+(d*d*d)
    n=n//10
if(sum==num):
      print("Armstrong number")
else:
     print("Not armstrong")