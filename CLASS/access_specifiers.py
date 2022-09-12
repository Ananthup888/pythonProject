#public - Inherited to all classes
#private (protected) -(eg:- _name) -Inherited to immidiated child
#strongly private - (eg :-__name ) - Cannot be inherited to child class
class Person:
    def __init__(self,n,v):
        self._name=n
        self.voterid=v
    def display(self):
        print("Name =",self._name)    #private
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
print(employee1._name)