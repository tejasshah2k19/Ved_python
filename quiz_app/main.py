import  seed
from Student import Student


while True:
    print("==================================================")
    print("               ONLINE QUIZ SYSTEM                 ")
    print("==================================================")

    print("1. Student Login\n2. Student Registration\n3. Exit")

    choice = int(input("\nEnter Choice : "))

    if choice == 1:
        mobile = input("enter mobile num")
        mpin = input("enter mpin")
        found = False
        currentUser = None  
        for student in seed.students:
            if(student.mobile == mobile and student.mpin == mpin):
                currentUser = student 
                found = True
                break 
        
        if found :
            pass
        else:
            print("Invalid Credentials.....")
    elif choice == 2:
        s = Student()
        s.getData()
        seed.students.append(s)
    elif choice == 3:
        break 