#accumulate

import itertools
s=[1,2,3,4,5,6]
res=itertools.accumulate(s,lambda x,y:x+y)      #acccumulate(seq,func)
print(list(res))