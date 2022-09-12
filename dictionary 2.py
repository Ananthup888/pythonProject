d1={}
d1['No']=1
d1['Name']='Ananthu'
d1['Place']='Thiruvalla'
print(d1)
d2={'Job':'Engineer','Hobby':'Movies'}
d1.update(d2)
print(d1)                        #to add multiple values

#copy
d2=d1.copy()      #or d2=d1                #to copy
print(d2)

#get function - to get a particular element    (#dictionar name- .get -(key)
print(d1.get('Name'))       #or [key]
