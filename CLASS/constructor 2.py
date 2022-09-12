class Student:
    def __init__(self,m1,m2,m3):
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def total(self):
        t=self.mark1+self.mark2+self.mark3
        return t
m1=int(input("Enter the mark1 of student 1"))
m2=int(input("Enter the mark2 of student 1"))
m3=int(input('Enter the mark3 of student 1'))
st1=Student(m1,m2,m3)
print("Total marks of student 1=",st1.total())