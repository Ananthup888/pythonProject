lst=[x for x in range (0,5) ]
print(lst)

lst=['apple','orange','banana','kiwi','cherry']
newlist=[ x if x!='banana'else 'strawberry' for x in lst] #oru condition matram
print(newlist)

newlist=['jackfruit' if x!='banana'else 'strawberry' for x in lst] #rand condition matram
print(newlist)