from functools import reduce
lst=[1,2,3,4,5,6,8,7]
resut=reduce(max,lst)
print("Method 1 result is =",resut)

#or
result=reduce(lambda x,y:x if x>y else y,lst)
print("Method 2 result is =",result)