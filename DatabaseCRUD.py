import mysql.connector 
#sql 


#python ---> mysql database 
#database connection 
#pip install mysql-connector-python 


#db connection --- mysql 

#url -> host : localhost 
#user 
#pwd
#dbName 

con = mysql.connector.connect(host="localhost",user="root",password="root",database="ved")

print(con)


cursor  = con.cursor() 

#create table 

#eid fname salary deptid higherdate email 

#add new employee 
#def -> 


insertQuery = """
        insert into users (firstName,email,city) values (%s,%s,%s)
    """
selectQuery = "select * from users"

selectQueryId = "select * from users where userId = "

def addUser():
    
    print("Enter FirstName ")
    firstName = input()
    print("Enter Email")
    email = input()
    print("Enter city")
    city =input()

    
    cursor.execute(insertQuery,(firstName,email,city))
    con.commit()
    userId = cursor.lastrowid
    # cursor.rowcount
    print("User added successfully with userId = "+userId)
    
def list_users():
        cursor.execute(selectQuery) #run 
        users = cursor.fetchall()
        
        for user in users:
            print(user)
     
def get_user_by_id(id):
        cursor.execute(selectQueryId+str(id)) #run 
        user  = cursor.fetchone()
        print(user)       

def delete_user_id():
    id = input("Enter id for delete student")
    cursor.execute("delete from users where userId = "+id)
    print("User Removed")



# addUser()
# list_users()
# get_user_by_id(1)


# list_users()
# delete_user_id(1)
# list_users()

print("1 For Add User\n2 For List all users\n3 For Get User by Id\n4 Delete user\n5 For Modify user")
print("enter choice")
choice  = int(input())

if choice == 1:
    addUser()
elif choice == 3:
    get_user_by_id(int(input("Enter id")))