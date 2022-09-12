str=input("Enter the string")
v=0
s=0
c=0
lst1=[]
lst2=[]
for i in str:
    if i in("aeiouAEIOU"):
     v=v+1
     lst1.append(i)
    elif i in(" "):
     s=s+1
    else:
      c=c+1
      lst2.append(i)
     
print("no of vowels=", v)
print("Vowwels are",lst1)
print("no of space=", s)
print("no of consonants=",c)
print("Consonants are",lst2)














