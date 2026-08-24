import os 
import datetime 
 


print(os.path.exists("c:\\tmp")) # true 
# print(os.mkdir("c:\\tmp\\ved"))  # 
# os.rmdir(r"c:\tmp\ved")


print(datetime.datetime.now())
print(datetime.datetime.today())

print(datetime.datetime.today().year)

print(datetime.datetime.today().hour)
print(datetime.datetime.today().minute)
print(datetime.datetime.today().second)


birthYear  = int(input("enter birth year"))
currentYear = datetime.datetime.now().year 

print(currentYear-birthYear)



