#overriding -Both parent and childhaving the functions of the same name
# when we call that fn,the fn in the child class will execute
#in order to execute parent fn, either you have to create object for parent or
#use super().getdata()
#eg:
class Person:
    def getdata(self):
        self.name=input("Enter the name")
        self.voterid=input("Enter the voter id")
    def display(self):
        print("Name =",self.name)
        print("Voter id =",self.voterid)
class Employee(Person):
    def getdata(self):
        super().getdata()
        self.salary=int(input("Enter the salary"))
        self.desig=input("Enter the desigination")
    def display(self):
        super().display()
        print("Salary =",self.salary)
        print("Desigination =",self.desig)
employee1=Employee()
employee1.getdata()
employee1.display()