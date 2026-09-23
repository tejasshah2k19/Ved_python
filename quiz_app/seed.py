from Student import Student 
from Question import Question
from Quiz import Quiz 


#initial data for app 


data = [
    ("Amit Shah",      9825012345, "1234"),
    ("Priya Patel",    9898023456, "2345"),
    ("Rohan Mehta",    9712034567, "3456"),
    ("Sneha Desai",    9033045678, "4567"),
    ("Karan Joshi",    9825056789, "5678"),
    ("Neha Trivedi",   9998067890, "6789"),
    ("Vivek Chauhan",  9426078901, "7890"),
    ("Aarti Solanki",  9909089012, "8901"),
    ("Manish Rana",    9662090123, "9012"),
    ("Kavita Bhatt",   9737001234, "0123"),
]


#student 
students = []
for name, mobile, mpin in data:
    s = Student()
    s.setData(name, mobile, mpin)
    students.append(s)


data = [
    # ---------------- Java ----------------
    ("Java", "Which keyword is used to inherit a class in Java?",
     "implements", "extends", "inherits", "super", "extends"),

    ("Java", "What is the size of int in Java?",
     "2 bytes", "4 bytes", "8 bytes", "Depends on OS", "4 bytes"),

    ("Java", "Which package is imported by default in every Java program?",
     "java.util", "java.io", "java.lang", "java.awt", "java.lang"),

    ("Java", "Which of these is NOT a valid access modifier in Java?",
     "public", "private", "protected", "friend", "friend"),

    # ---------------- C ----------------
    ("C", "Which header file is required to use printf()?",
     "conio.h", "stdio.h", "stdlib.h", "string.h", "stdio.h"),

    ("C", "What is the index of the first element of an array in C?",
     "0", "1", "-1", "Depends on declaration", "0"),

    ("C", "Which loop is guaranteed to execute at least once?",
     "for", "while", "do-while", "nested for", "do-while"),

    ("C", "Which function is used to allocate memory dynamically in C?",
     "alloc()", "malloc()", "new", "create()", "malloc()"),

    # ---------------- Ruby ----------------
    ("Ruby", "Which keyword is used to define a method in Ruby?",
     "func", "def", "method", "sub", "def"),

    ("Ruby", "What is the file extension of a Ruby source file?",
     ".ru", ".rb", ".ruby", ".rbx", ".rb"),

    ("Ruby", "Which method prints output followed by a newline in Ruby?",
     "print", "puts", "write", "echo", "puts"),

    # ---------------- Python ----------------
    ("Python", "Which keyword is used to define a function in Python?",
     "function", "def", "fun", "define", "def"),

    ("Python", "Which of the following data types is immutable in Python?",
     "list", "dict", "set", "tuple", "tuple"),

    ("Python", "Which method adds an element at the end of a list?",
     "add()", "append()", "insert()", "extend()", "append()"),

    ("Python", "What is the output of print(type(10/2)) in Python 3?",
     "<class 'int'>", "<class 'float'>", "<class 'double'>", "Error",
     "<class 'float'>"),
]
extraData = [
    ("Java", "Which method is the entry point of a Java program?",
     "start()", "main()", "run()", "init()", "main()"),
    ("Java", "Which of these is used to handle exceptions in Java?",
     "try-catch", "if-else", "switch", "for", "try-catch"),

    ("C", "Which operator is used to access the value at an address?",
     "&", "*", "->", "#", "*"),
    ("C", "What is the correct way to declare a constant in C?",
     "final int a=10;", "const int a=10;", "constant a=10;", "static a=10;",
     "const int a=10;"),

    ("Ruby", "Which symbol is used for a comment in Ruby?",
     "//", "#", "--", "/* */", "#"),
    ("Ruby", "Which keyword ends a method definition in Ruby?",
     "endif", "stop", "end", "}", "end"),
    ("Ruby", "In Ruby, everything is treated as a...",
     "function", "object", "variable", "pointer", "object"),

    ("Python", "Which symbol is used for single line comment in Python?",
     "//", "#", "--", "/*", "#"),
    ("Python", "Which function returns the length of a list?",
     "size()", "count()", "len()", "length()", "len()"),
]

data = data + extraData      # data = your earlier 15-question list

questions = []
for row in data:
    q = Question()
    q.setQuestionDetail(*row)
    questions.append(q)

#question 
questions = []

for row in data:
    q = Question()
    q.setQuestionDetail(*row)      # unpack the tuple into the setter
    questions.append(q)

#quiz 
quizzes = []

quizTitles = {
    "Java":   ["Java Basics - Set 1",   "Java Basics - Set 2"],
    "C":      ["C Fundamentals - Set 1", "C Fundamentals - Set 2"],
    "Ruby":   ["Ruby Basics - Set 1",   "Ruby Basics - Set 2"],
    "Python": ["Python Basics - Set 1", "Python Basics - Set 2"],
}
 

for subject, titles in quizTitles.items():
    subjectQuestions = [q for q in questions if q.subject == subject]
    half = len(subjectQuestions) // 2
    parts = [subjectQuestions[:half], subjectQuestions[half:]]

    for title, part in zip(titles, parts):
        quiz = Quiz()
        quiz.setData(title, subject, len(part))
        for q in part:
            quiz.mapQuestionToQuiz(q)
        quizzes.append(quiz)


# print("Quiz App Initialized.........") 
 
 