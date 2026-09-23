# custom -> exception class 


# try: 
#     pass 
# except ValueError:
#     pass 


# class A extends Exception {
    
# }

class A(Exception):
    pass 


try: 
    raise A() 
except A:
    print("A ERROR ")
    
    
    
#create your exception class and inherit with Exception 
