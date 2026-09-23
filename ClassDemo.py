class Student:
     
    def getData(self):
        print("Enter name")
        self.name = input() #instance variable 
        #if we are not going to use self that it will consider local variable 
        
    def printData(self):
        print(self.name)    
        


#to access class property we need to create instance - object 


s = Student() 
s.getData() #==> Student.getData(s)
t = Student() 
t.getData()


s.printData()
t.printData()