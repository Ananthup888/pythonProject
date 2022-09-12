#copy content of one file to another
f1=open('new3','r')
contents=f1.read()
f2=open('new','w')
f2.write(contents)
f1.close()
f2.close()