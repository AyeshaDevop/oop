class Person:
    name = "abcd"

    def changeName(self, name):
        Person.name = name

p1 = Person()
p1.changeName("Ayesha")
print(p1.name)  
class Students:
    def __init__(self, phy, che, bio):
        self.phy = phy
        self.che = che
        self.bio = bio
        self.percentage = str((self.phy + self.che + self.bio) / 3) + "%"

    def calcPercentage(self):
        return str((self.phy + self.che + self.bio) / 3) + "%"

stu1 = Students(45, 34, 39)
print(stu1.percentage)           
print(stu1.phy)              
print(stu1.calcPercentage())     