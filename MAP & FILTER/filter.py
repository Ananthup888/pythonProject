#filter
def even(n):
    if(n%2==0):
        return True
    else:
        return False
lst=[1,2,3,4,5,6,7,8,9,10]
result=filter(even,lst)
print(list(result))