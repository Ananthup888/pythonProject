class Student:
    def getdata(self,a,b,c):
        self.mark1=a
        self.mark2=b
        self.mark3=c
    def display(self):
        print('Marks of subject 1 =',self.mark1)
        print('Marks of subject 2 =',self.mark2)
        print('Marks of subject 3 =',self.mark3)
    def total(self):
        t=self.mark1+self.mark2+self.mark3
        print('Total =',t)
stud1=Student()
stud1.getdata(23,24,25)
stud1.display()
stud1.total()
stud2=Student()
stud2.getdata(17,18,19)
stud2.display()
stud2.total()
stud3=Student()
stud3.getdata(20,22,24)
stud3.display()
stud3.total()