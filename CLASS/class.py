class Vehicle:
    def getdata(self,n,a):
        self.name=n
        self.fuel_capacity=a
    def display(self):
        print("Name:",self.name)
        print("Fuel capacity:",self.fuel_capacity)
car=Vehicle()
bike=Vehicle()
bus=Vehicle()
car.getdata("Alto",100)
bike.getdata('Dominar',50)
car.display()
bike.display()
bus.getdata('Tata',200)
bus.display()
lorry=Vehicle()
lorry.getdata("Bharat benz",500)
lorry.display()