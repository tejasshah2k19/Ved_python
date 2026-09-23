import math
class BasicCalc:
    def add(self,a,b):
        print(a+b)
        
    def sub(self,a,b):
        print(a-b)
        
    def mul(self,a,b):
        print(a*b)
        


class SciCalc(BasicCalc): 
    def sqrt(self,num):
        print(math.sqrt(num))

    def power(self,a,b):
        print(math.pow(a,b))
        
        

s = SciCalc()

s.sqrt(9)
s.power(2,3)    

#inheritance => is the mechanish by which object of one class can access property of another class 
s.add(5,5)
s.sub(5,6)
s.mul(5,6)


"""
    class -> gives -> parent super base
    class -> takes -> child  sub   derived 

    single level inheritance 
    A 
    B(A) 
    
    
    multi level inheritance 
    A 
    B(A)
    C(B)
    
    
    multiple inheritance 
    A B
    C(A,B) 
   
    
    hirerchical inheritance 
        A
    B(A)  C(A)
 C(B)
    
    hybrid inheritance
    
    A       D
    
    B(A,D)
    
    C(B)
    
    
      D

 A(D)    B(D)
  
    C(A,B) 
   
"""
