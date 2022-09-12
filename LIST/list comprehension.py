#list comprehention

lst=['apple','orange','banana','kiwi','cherry']
newlist=[x for x in lst if 'apple'!=x in x]
print(newlist)

newlist=[x for x in lst if 'a' in x]
print(newlist)

newlist=[x.upper() for x in lst ]
print(newlist)