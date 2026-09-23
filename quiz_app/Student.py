class Student:
    def getData(self):
        self.name = input("enter name")
        self.mobile = int(input("enter mobile"))
        self.mpin = input("enter mpin")
        
    def printData(self):
        print("Name   : ",self.name)
        print("Mobile : ",self.mobile)
        
    def setData(self, name, mobile, mpin):
        self.name = name
        self.mobile = mobile
        self.mpin = mpin
    
    def __str__(self):
        return f"{self.name} | {self.mobile} | {self.mpin}"