#constructor -initilize values to data members

class Student:
    def __init__(self,m1,m2,m3):
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def total(self):
        t=self.mark1+self.mark2+self.mark3
        print("Total marks of student",t)
st1=Student(23,24,25)
st2=Student(17,18,19)
st3=Student(22,22,23)
st1.total()
st2.total()
st3.total()