lst=[2,4,5,7,9,15,18,25,45]
result1=filter(lambda n:n%5==0,lst)
print(list(result1))
result2=filter(lambda n:n%5!=0,lst)
print(list(result2))