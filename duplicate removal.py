a=[1,2,3,4,8,6,3,2,5,6,7,8]
lst=[]
for i in a:
    if i not in lst:
        lst.append(i)
print(lst)