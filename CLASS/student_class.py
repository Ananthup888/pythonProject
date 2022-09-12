class Student:
    def getdata(self,n,a,r):
        self.name=n
        self.age=a
        self.roll_number=r
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Roll number:",self.roll_number)
student1 =Student()
student2 =Student()
student3 =Student()
student1.getdata('Ananthu',23,32)
student2.getdata('Muhammad',24,51)
student3.getdata('Jijo',22,38)
student1.display()
student2.display()
student3.display()



