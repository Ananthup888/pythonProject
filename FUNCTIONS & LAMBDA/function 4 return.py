def calc(a,b):
    s=a+b
    d=a-b
    m=a*b
    q=a/b
    return s,d,m,q
ans=calc(4,2)
print(ans)

#or

def calc(a,b):
    s=a+b
    d=a-b
    m=a*b
    q=a/b
    return s,d,m,q
sum,dif,mul,div=calc(4,2)
print("sum is",sum)
print("dif is",dif)
print("mul is",mul)
print("div is",div)
