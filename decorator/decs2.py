
lst=[1,2,3,4,'hello','hi']          #abstraction
str_list=[str(data) for data in lst ]
num_list=[data for data in str_list if data.isdigit()]
number_list=[int(data) for data in num_list]
print(number_list)

#or

num_list=[data for data in lst if isinstance(data,int)]
print(num_list)  