n=int(input("Enter the number"))
l=len(str(n))
print(l)
s=0
num=n
while(n>0):
    d=n%10
    s=s+d**l
    n=n//10
if(num==s):
    print("Armstrong")
else:
    print("Not armstrong")
