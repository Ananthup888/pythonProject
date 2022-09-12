# *arg       Nonkeyword arguments
# **karg      keyword arguments
def fun(*num):    #num=10,20,30,40
    sum=0
    for i in num:
        sum=sum+i
    print("Sum is =",sum)

fun(10,20,30,40)
