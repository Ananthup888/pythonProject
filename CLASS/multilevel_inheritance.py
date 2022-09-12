#parent --> inherits child -->inherits grandchild -->...
class Student:
    def __init__(self):
        self.name=input("Enter the name")
        self.roll=int(input("Enter the roll number"))
    def display(self):
        print("Name :", self.name)
        print("Roll number :",self.roll)
class Mark(Student):
    def __init__(self):
        super().__init__()
        self.mark1=input("Enter mark 1")
        self.mark2=input("Enter mark 2")
        self.mark3=input("enter mark 3")
    def display1(self):
        print("Mark 1(100) :",self.mark1)
        print("Mark 1(100) :",self.mark2)
        print("Mark 1(100) :",self.mark3)
class Grade(Mark):
    def __init__(self):
        super().__init__(self):
    def printgrade(self):
        t=self.mark1+self.mark2+self.mark3
        p=t/300*100
        if(p>+80):
            print("A grade")
        elif(p>=60):
            print("B grade")
        elif(p>=45):
            print("C grade")
        else:
            print("FAIL")
g1=Grade()
g1.display()
g1.display1()
g1.printgrade()

