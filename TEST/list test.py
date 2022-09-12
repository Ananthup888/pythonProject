# lst=[1,2,3,4,5,6,7,8]
# n=int(input("Enter the number"))
# if n in lst:
#     print("found")
# else:
#     print("Not found")

#or  linear search

lst=[1,2,3,4,5,6,7,8]
n=int(input("Enter the number"))
for i in lst:
    if(i==n):
        flag=1
        break
    else:
        flag=0
if(flag==1):
       print("Found")
else:
    print("Not found")

