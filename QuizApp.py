# ============================================
#           ONLINE QUIZ SYSTEM
# ============================================

class Student:

    def __init__(self, name, mobile, password):
        self.name = name
        self.mobile = mobile
        self.password = password
        self.scores = []


class Question:

    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer


class Quiz:

    def __init__(self, subject, questions):
        self.subject = subject
        self.questions = questions

    def start_quiz(self, student):

        score = 0

        print("\n==================================================")
        print("                 " + self.subject.upper() + " QUIZ")
        print("==================================================")
        print("Student :", student.name)
        print("Questions:", len(self.questions))
        print("--------------------------------------------------")

        for i, q in enumerate(self.questions, start=1):

            print("\nQuestion", i, "of", len(self.questions))
            print()
            print(q.question)

            for key, value in q.options.items():
                print(key + ".", value)

            answer = input("\nEnter your answer: ").upper()

            if answer == q.answer:
                score += 1

        percentage = (score / len(self.questions)) * 100

        if percentage >= 40:
            result = "PASS"
        else:
            result = "FAIL"

        student.scores.append({
            "subject": self.subject,
            "score": score,
            "total": len(self.questions),
            "percentage": percentage
        })

        print("\n==================================================")
        print("                 QUIZ COMPLETED")
        print("==================================================")

        print("Student          :", student.name)
        print("Subject          :", self.subject)
        print("Total Questions  :", len(self.questions))
        print("Correct Answers  :", score)
        print("Wrong Answers    :", len(self.questions) - score)
        print("Score            :", score, "/", len(self.questions))
        print("Percentage       :", percentage, "%")
        print("Result            :", result)

        print("==================================================")


# ============================================
#              QUIZ QUESTIONS
# ============================================

python_questions = [

    Question(
        "Which keyword is used to define a function in Python?",
        {
            "A": "function",
            "B": "def",
            "C": "fun",
            "D": "define"
        },
        "B"
    ),

    Question(
        "Which of the following is a mutable data type?",
        {
            "A": "tuple",
            "B": "string",
            "C": "list",
            "D": "integer"
        },
        "C"
    ),

    Question(
        "What is the output of print(10 + 20)?",
        {
            "A": "1020",
            "B": "30",
            "C": "10+20",
            "D": "Error"
        },
        "B"
    ),

    Question(
        "Which symbol is used for comments in Python?",
        {
            "A": "//",
            "B": "/*",
            "C": "#",
            "D": "--"
        },
        "C"
    ),

    Question(
        "Which collection stores data as key-value pairs?",
        {
            "A": "List",
            "B": "Tuple",
            "C": "Set",
            "D": "Dictionary"
        },
        "D"
    )
]


java_questions = [

    Question(
        "Which keyword is used to create a class in Java?",
        {
            "A": "class",
            "B": "Class",
            "C": "create",
            "D": "object"
        },
        "A"
    ),

    Question(
        "Which method is the starting point of a Java program?",
        {
            "A": "start()",
            "B": "run()",
            "C": "main()",
            "D": "execute()"
        },
        "C"
    ),

    Question(
        "Which company originally developed Java?",
        {
            "A": "Microsoft",
            "B": "Sun Microsystems",
            "C": "IBM",
            "D": "Google"
        },
        "B"
    ),

    Question(
        "Which keyword is used for inheritance in Java?",
        {
            "A": "inherits",
            "B": "implements",
            "C": "extends",
            "D": "inherit"
        },
        "C"
    ),

    Question(
        "Which data type is used to store true or false?",
        {
            "A": "bool",
            "B": "boolean",
            "C": "BooleanValue",
            "D": "bit"
        },
        "B"
    )
]


c_questions = [

    Question(
        "Which symbol is used to end a statement in C?",
        {
            "A": ".",
            "B": ":",
            "C": ";",
            "D": ","
        },
        "C"
    ),

    Question(
        "Which function is used to print output in C?",
        {
            "A": "print()",
            "B": "printf()",
            "C": "display()",
            "D": "cout"
        },
        "B"
    ),

    Question(
        "Which header file is commonly used for printf()?",
        {
            "A": "stdlib.h",
            "B": "string.h",
            "C": "math.h",
            "D": "stdio.h"
        },
        "D"
    ),

    Question(
        "Which operator is used to get the address of a variable?",
        {
            "A": "*",
            "B": "&",
            "C": "%",
            "D": "#"
        },
        "B"
    ),

    Question(
        "Which loop executes its body at least once?",
        {
            "A": "for",
            "B": "while",
            "C": "do-while",
            "D": "nested"
        },
        "C"
    )
]


dbms_questions = [

    Question(
        "Which language is used to query databases?",
        {
            "A": "HTML",
            "B": "SQL",
            "C": "CSS",
            "D": "XML"
        },
        "B"
    ),

    Question(
        "Which command is used to retrieve data?",
        {
            "A": "GET",
            "B": "FETCH",
            "C": "SELECT",
            "D": "RETRIEVE"
        },
        "C"
    ),

    Question(
        "Which command is used to remove a table?",
        {
            "A": "DELETE",
            "B": "REMOVE",
            "C": "DROP",
            "D": "CLEAR"
        },
        "C"
    ),

    Question(
        "Which key uniquely identifies a record?",
        {
            "A": "Foreign Key",
            "B": "Primary Key",
            "C": "Candidate Key",
            "D": "Alternate Key"
        },
        "B"
    ),

    Question(
        "Which command is used to add a new record?",
        {
            "A": "ADD",
            "B": "INSERT",
            "C": "CREATE",
            "D": "PUT"
        },
        "B"
    )
]


# ============================================
#              CREATE QUIZZES
# ============================================

quizzes = {

    "1": Quiz("Python", python_questions),

    "2": Quiz("Java", java_questions),

    "3": Quiz("C Programming", c_questions),

    "4": Quiz("DBMS", dbms_questions)
}


# ============================================
#              STUDENT DATA
# ============================================

students = []


# ============================================
#           STUDENT REGISTRATION
# ============================================

def register_student():

    print("\n==================================================")
    print("              STUDENT REGISTRATION")
    print("==================================================")

    name = input("Enter Student Name  : ")
    mobile = input("Enter Mobile Number : ")

    # Check mobile already exists

    for student in students:

        if student.mobile == mobile:
            print("\nMobile number already registered!")
            return

    password = input("Create Password     : ")
    confirm = input("Confirm Password    : ")

    if password != confirm:

        print("\nPassword does not match!")
        return

    student = Student(name, mobile, password)

    students.append(student)

    print("\nRegistration Successful!")
    print("Your account has been created successfully.")


# ============================================
#                 LOGIN
# ============================================

def login():

    print("\n==================================================")
    print("                 STUDENT LOGIN")
    print("==================================================")

    mobile = input("Enter Mobile Number: ")
    password = input("Enter Password     : ")

    for student in students:

        if student.mobile == mobile and student.password == password:

            print("\nLogin Successful!")
            print("Welcome,", student.name)

            dashboard(student)
            return

    print("\nInvalid mobile number or password!")


# ============================================
#             VIEW SUBJECTS
# ============================================

def view_subjects():

    print("\n==================================================")
    print("                 AVAILABLE SUBJECTS")
    print("==================================================")

    print("1. Python")
    print("2. Java")
    print("3. C Programming")
    print("4. DBMS")

    print("\nTotal Subjects Available :", len(quizzes))


# ============================================
#             PREVIOUS SCORES
# ============================================

def previous_scores(student):

    print("\n==================================================")
    print("                 MY PREVIOUS SCORES")
    print("==================================================")

    print("Student :", student.name)
    print("Mobile  :", student.mobile)

    if len(student.scores) == 0:

        print("\nNo previous quiz attempted.")

        return

    print("\n--------------------------------------------------")
    print("No.   Subject             Score       Percentage")
    print("--------------------------------------------------")

    for i, score in enumerate(student.scores, start=1):

        print(
            i,
            "    ",
            score["subject"],
            "       ",
            str(score["score"]) + "/" + str(score["total"]),
            "       ",
            str(score["percentage"]) + "%"
        )

    print("--------------------------------------------------")


# ============================================
#                 PROFILE
# ============================================

def profile(student):

    print("\n==================================================")
    print("                 MY PROFILE")
    print("==================================================")

    print("Name   :", student.name)
    print("Mobile :", student.mobile)

    print("Quizzes Attempted :", len(student.scores))


# ============================================
#              START QUIZ
# ============================================

def start_quiz(student):

    print("\n==================================================")
    print("                 SELECT SUBJECT")
    print("==================================================")

    for key, quiz in quizzes.items():

        print(key + ".", quiz.subject)

    print("5. Back to Dashboard")

    choice = input("\nEnter your choice: ")

    if choice in quizzes:

        quizzes[choice].start_quiz(student)

    elif choice == "5":

        return

    else:

        print("\nInvalid choice!")


# ============================================
#              STUDENT DASHBOARD
# ============================================

def dashboard(student):

    while True:

        print("\n==================================================")
        print("              STUDENT DASHBOARD")
        print("==================================================")

        print("Welcome", student.name)
        print()
        print("1. Start Quiz")
        print("2. My Previous Scores")
        print("3. View Subjects")
        print("4. My Profile")
        print("5. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            start_quiz(student)

        elif choice == "2":

            previous_scores(student)

        elif choice == "3":

            view_subjects()

        elif choice == "4":

            profile(student)

        elif choice == "5":

            print("\nYou have been successfully logged out.")
            return

        else:

            print("\nInvalid choice! Please try again.")


# ============================================
#                 MAIN MENU
# ============================================

def main():

    while True:

        print("\n==================================================")
        print("              ONLINE QUIZ SYSTEM")
        print("==================================================")

        print("1. Student Login")
        print("2. Student Registration")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            login()

        elif choice == "2":

            register_student()

        elif choice == "3":

            print("\n==================================================")
            print("Thank you for using Online Quiz System.")
            print("Goodbye!")
            print("==================================================")

            break

        else:

            print("\nInvalid choice! Please enter 1, 2 or 3.")


# ============================================
#              PROGRAM START
# ============================================

main()