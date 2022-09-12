f1=open("new3",'r')
lst=f1.readlines()
lst.reverse()
print(lst)
for i in lst:
    print(i.strip())