def add():
    a = 10
    b = 20
    c = a+b 
    print("add = ",c)
    
# def add(a,b):
#     print(a+b)
    
def sub(a,b):
    c = a+b
    print("add = ",c)

sub(1,22)  #positional arguments 

def mul(a,b):
    return a*b

#args 
def sumOfNum(*nums):
    print(nums) 
    sum = 0 
    for data in nums:
        sum = sum + data 
    print(sum)
    
#kwargs     

def profile(**data):
    print(data)

    
sumOfNum(1)
sumOfNum(1,2)
sumOfNum(1,2,3)

profile(name="ram",age="18")
profile(name="ram",age="18",salary=11111)

#find out max from n number of args





g = 10 
def modify():
    global g 
    g = 29 
    
modify()
print(g) #  29  


ans = lambda x : x*x 


def multiReturn():
    a =10 
    b = 20 
    return a,b  #you can return more than 1 value.  -> tuple 

print(multiReturn())



def santa(n1,n2):
    print(n1*n2)
    
    
santa(n2=20,n1=30) #keyword argument 
santa(20,30)



#default argument 

def addition(a=10,b=20):
    print(a+b)


addition(30)
addition(30,40)
addition()



#a,b=10,c=22,d=2

def sub(a,b=20):
    print(a+b)








