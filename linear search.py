#linear search using functions
def linearsearch(list1,key):       #list1=[11,12,13,14,15]
    n=len(list1)                    #n=5     key=13
    for i in range(0,n):            #i=0     #i=1      #i=2
        if(list1[i]==key):          #11=13   12=13     13=13
            return i
    return -1
lst=input('Enter the list').split()
key=input('Enter the key')
res=linearsearch(lst,key)
if(res==-1):
    print('Item not found')
else:
    print('item found at index',res)