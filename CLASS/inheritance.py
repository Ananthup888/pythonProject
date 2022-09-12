#inheritance -inherit the properties of parent class
#single inheritance
class Parent:               #Parent class
    def displayP(self):
        print("I am Parent")
class Child(Parent):         #Child
    def displayC(self):
        print("I am Child")
child1=Child()
child1.displayP()
child1.displayC()