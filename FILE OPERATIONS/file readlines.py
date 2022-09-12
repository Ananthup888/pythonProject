f1=open("new",'r')           #foobject=open('file name','mode')
lst=f1.readlines()
c=0
for i in lst:
    c=c+1
    print(i.strip())
f1.close()
print(c)


# print(f1.name)
# print(f1.mode)
# print(f1.closed)
