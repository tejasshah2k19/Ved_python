import math
class BasicCalc:
    def add(self,a,b):
        print(a+b)
        
    def sub(self,a,b):
        print(a-b)
        
    def mul(self,a,b):
        print(a*b)
        


class SciCalc: 
    def sqrt(self,num):
        print(math.sqrt(num))

    def power(self,a,b):
        print(math.pow(a,b))
        
#multiple inh         
class Calc(BasicCalc,SciCalc):
    pass 


c = Calc()
c.add(1,1)
c.sqrt(9)


        