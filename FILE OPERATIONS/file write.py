#write
f1=open('new1','w')
f1.write("where are you")
f1.close()
f1=open("new1","r")
print(f1.read())

