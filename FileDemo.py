# # f = open("numbers.txt","w") # if file does not exists file will be created , if exists then data will be overwrite 
# # f.write("royal education")
# # f.close()


# # f = open("c:\\tmp\\numbers.txt","w") # if file does not exists file will be created , if exists then data will be overwrite 
# f = open(r"c:\tmp\numbers.txt","w") # if file does not exists file will be created , if exists then data will be overwrite 
# f.write("royal education")


# list = ["John","rock","salt"]

# f.writelines(list)
# f.close()




# f = open("myCalc.c")

# data =f.read() # read entire file 
# data =f.read(10) # number of bytes 


# data = f.readline() # read single line 
# print(data)

# data = f.readline() # read single line 
# print(data)

# data = f.readlines()
# print(data)


# while True:
#     data = f.readline()
#     if data == "":
#         break
#     print(data)
     
# f.close()



with open("myCalc.c") as file :
    for line in file:
        print(line)
        
#close 
