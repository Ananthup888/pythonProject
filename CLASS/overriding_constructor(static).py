#public - Inherited toall classes
class Person:
    def __init__(self,n,v):
        self.name=n
        self.voterid=v
    def display(self):
        print("Name =",self.name)
        print("Voter id =",self.voterid)
class Employee(Person):
    def __init__(self,n,v,s,d):
        super().__init__(n,v)
        self.salary=s 
        self.desig=d
    def display(self):
        super().display()
        print("Salary =",self.salary)
        print("Desigination =",self.desig)
employee1=Employee("Ram","34566",50000,"er")
employee1.display()