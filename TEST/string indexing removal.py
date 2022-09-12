str=input("Enter the string")
n=int(input("Enter the index to be removed"))
str1=str[0:n]+str[n+1:]
print(str1)