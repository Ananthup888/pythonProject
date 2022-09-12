class Student:
    def __init__(self,rollnum,name,course):
        self.rollnum=rollnum
        self.name=name
        self.course=course
    def __str__(self):
        return self.name
st=Student(23,"Ravi","Mechanical")
print(st) 
