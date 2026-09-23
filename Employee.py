class Employee:
    #variables
    #methods 

    #default values 
    # def __init__(self):
    #     print("Constructor called ")
    #     self.name = ""
    #     self.age = 18 
    code = 123 #class variable #share  #if modify by objects -> independant copy 
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        self._salary = 5000  #protected --- internal use --> but you can access outside class 
        self.__tax = 1000    #private --- internal use --> direct access restricted {we can bypass}
        print("TAX = ",self.__tax)                                
    def getData(self):
        self.name = input("Enter the name")
        self.age = input("Enter the age")
    
    def printData(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
    
    @classmethod
    def printCode(cls):
        print(cls.code)
    
    @staticmethod    
    def validCode(code):
         return code > 0
    
    @property 
    def full_data(self):
         return self.name,self.age,self._salary,self.__tax 
         
    @property      
    def tax(self):
        return self.__tax        
   
    @tax.setter 
    def tax(self,taxVal):
        self.__tax = taxVal         
        
        
e1  = Employee("royal",18)#name , age     

#e1.getData()
#e2.getData()

e1.printData()

e2  = Employee("ram",50)#name , age 
e2.printData()


print(e1.code)
print(e2.code)
Employee.code =111
print(e1.code)
print(e2.code)
print(e1._salary)

#class => variable + methods 
#object 

#instance variable 

#Bank  --> class ----> balance, wid() , dep()
#customers -> object{balance,wid(),dep()}    
#bankCode --> remain same --> 

#constructor --> initialize instance 

Employee.printCode()
e1.printCode()

print(Employee.validCode(111))
print(e1.validCode(222))
print(e1._salary)
# print(e1.__tax)
print(e1._Employee__tax)
e1._Employee__tax =111 


print(e1.full_data)


print(e1.tax) 
e1.tax = 111111 
print(e1.tax) 
