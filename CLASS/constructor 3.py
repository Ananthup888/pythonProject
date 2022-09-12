class Student:
    def __init__(self):
        self.mark1=int(input('Enter mark1'))
        self.mark2=int(input('Enter mark2'))
        self.mark3=int(input('Enter mark3'))
    def total(self):
        t=self.mark1+self.mark2+self.mark3
        print('Total marks of student=',t)
st1=Student()
st2=Student()
st3=Student()
st1.total()
st2.total()
st3.total()