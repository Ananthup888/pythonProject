def binarysearch(lst,key):
    start=0
    end=len(lst)-1
    mid=0
    while(start<=end):
        mid=(start+end)//2
        if((lst[mid]>key)):
            end=mid-1
        elif(lst[mid]<key):
            start=mid+1
        else:
            return mid
    return -1

list1=input("Enter the list").split()
key=input("enter the key")
res=binarysearch(list1,key)
if(res==-1):
    print("Item not found")
else:
    print("Item found at index",res)

