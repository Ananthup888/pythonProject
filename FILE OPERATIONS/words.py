#to print the words in file

f1=open("new3",'r')
a=f1.read()
print(a)
for i in a.split():
    print(i)
