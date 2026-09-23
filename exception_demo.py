import traceback
# try:
#     a = int(input("enter num1"))
#     b = int(input("enter num2"))

#     c = a/b 
#     print(c)
# except ValueError:
#     print("Please Enter only whole numbers")
# except ZeroDivisionError:
#     print("please do not enter zero in second number")


try:
    a = int(input("enter num1"))
    b = int(input("enter num2"))
    c = a/b 
    print(c)

except ValueError:
    print("Please Enter only whole numbers")
# except ZeroDivisionError:
#     print("please do not enter zero in second number")
except Exception as e:
    print("something went wrong.....")
    print(e)
    #sendMailToDeveloper
    traceback.print_exc()
else: 
    print("code is clean and perfect.........")
    
finally:
    print("i am always executes.....")
    
