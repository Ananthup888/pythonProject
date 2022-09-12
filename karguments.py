# def fun(name,age):
#      print("Name :",name)
#      print("Age :",age)
# fun(name='Anu',age=23)

# **karg
def fun(**karg):     #dictionary -type
     print(type(karg))
     for key,value in karg.items():
         print(key,"is =",value)
fun(name='anu',age=23,job='doctor')