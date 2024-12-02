class Students :
    def __init__(self , name):
        self.name = name
 
s1 = Students ("Ali")    
del s1
print(Students.name)

#public and private
class Account :
    def __init__(self , acc_num , acc_pass):
        self.acc_num = acc_num
        self.__acc_pass = acc_pass

acc1 = Account("ali123" , "abcd")
print(acc1.acc_num )
print(acc1.__acc_pass)

