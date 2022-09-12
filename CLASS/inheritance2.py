class Person:
    def getdata(self):
        self.name=input("Enter the name")
        self.voterid=input("Enter the voter id")
    def display(self):
        print("Name =",self.name)
        print("Voter id =",self.voterid)
class Employee(Person):
    def getdata1(self):
        super().getdata()
        self.salary=int(input("Enter the salary"))
        self.desig=input("Enter the desigination")
    def display1(self):
        super().display()
        print("Salary =",self.salary)
        print("Desigination =",self.desig)
employee1=Employee()
employee1.getdata1()
employee1.display1()