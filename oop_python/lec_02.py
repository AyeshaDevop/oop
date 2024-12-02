class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")
car1.start()  

class Fortuner(ToyotaCar):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type


car1 = Fortuner("Toyota", "diesel")
car1.start() 

class A:
    VarA = "welcome to class A"

class B:
    VarB = "welcome to class B"

class C(A, B):
    VarC = "welcome to class C"

c1 = C()
print(c1.VarC)
print(c1.VarA) 
print(c1.VarB)  

        