import pickle
import random 
class Student:
    def __init__(self):
        self.rollNum = random.randint(1000,9999)
        self.name = ""
        self.email = ""
        self.password = "" 
        
    def getData(self):
        print("Enter name")
        self.name= input()
        print("Enter email and password")
        self.email = input()
        self.password = input()
    
    def display(self):
        print("RollNum = ",self.rollNum)
        print("Name = ",self.name)
        print("Email = ",self.email) 
        

# s = Student()
# s.getData()

#serialization 

# f = open("data.txt","wb")
# pickle.dump(s,f)
# f.close()



t = Student()
with open("data.txt","rb") as f:
    t = pickle.load(f)  
    t.display()
    
