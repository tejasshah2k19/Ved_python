#python -> file .py -> module 


import SciCalc
import BasicCalc 
import BasicCalc as b 
from  BasicCalc import add
from  BasicCalc import add,sum,mul
from BasicCalc import * 

import calculator.CivilCalc as c 
from calculator.CivilCalc import * 

from calculator import * 



print("1 For Add\n2 For Sum\n3 For Mul\n4 For Sqrt\n5 For Floor\n6 For Ceil\n7 For Var to Feet")
print("Enter choice")
choice = int(input())


if choice == 1:
     print(BasicCalc.add(50,60))
     print(b.add(11,11))
     add(55,66)
elif choice == 2:
   print( BasicCalc.sum(10,20,30,40,50))
elif choice == 3:
    print(BasicCalc.mul(2,3))
elif choice == 4:
    print(SciCalc.sqrt(9))
elif choice == 5:
    print(SciCalc.floor(5.9))
elif choice == 6:
    print(SciCalc.ceil(5.9))
elif choice == 7:
    print(c.varToSqFeet(100))
else:
    print("\nInvalid Choice....")
    
    