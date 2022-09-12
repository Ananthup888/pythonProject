#digit sum
n=int(input("Enter the number"))
sum=0
while(n>0):       #1st   #123 >0       #2nd 12>0          #3rd 1>0
    d=n%10              #d=123%10=3      d=12%10=2           d=1%10=1
    sum=sum+d           #sum=0+3=3       s=3+2=5             s=5+1=6
    n=n//10             #n=123//10=12    n=12//10print(sum)
