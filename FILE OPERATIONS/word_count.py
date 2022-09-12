#to print the wordcount in file

f1=open("new3",'r')
a=f1.read()
wordcount={}
for word in a.split():
    if word not in wordcount:
        wordcount[word]=1
    else:
        wordcount[word]+=1
print(wordcount)
for k,v in wordcount.items():
    print(k,v)
