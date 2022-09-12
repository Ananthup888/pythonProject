#reverse of number
n=int(input("Enter the number"))
rev=0
num=n
while(n>0):
    d=n%10          #  d=123%10=3
    rev=rev*10+d    # rev=3*10+
    n=n//10
print(rev)
if(rev==num):
    print("Palindrome")
else:
    print("Not palindrome")
