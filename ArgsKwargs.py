def sum(*args):
    sum = 0 
    for data in args:
        sum = sum + data
    print("Sum = ",sum) 
    
def sum2(*values):
    sum = 0 
    for data in values:
        sum = sum + data
    print("Sum = ",sum) 
        
def addStudent(**kwargs):
    print(kwargs)
    print(kwargs.get("name"))
    

sum(11,22)
sum(22,11,23,4)

addStudent(name="ram",age=12)
addStudent(name="ram",age=12,city="Ayodhya")
