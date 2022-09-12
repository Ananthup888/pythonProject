#import functools
from functools import reduce
lst=[1,2,3,4]
#result=functools.reduce(lambda x,y:x+y,lst)
result=reduce(lambda x,y:x+y,lst)
print("Method 1 result is=",result)

#or

from functools import reduce
import operator
result=reduce(operator.add,lst)                #reduce(func,seq)
print("Method 2 result is=",result)