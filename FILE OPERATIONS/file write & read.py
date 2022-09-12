f1=open('new1','r+')
f1.write("where are you")
print(f1.tell())      #tell() - returns  current position of file pointer
f1.seek(0)           #seek - change the location of the file pointer
print(f1.read())