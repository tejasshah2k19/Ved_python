class Question:
    def getQuestionDetail(self):
        self.subject = input("Enter subject name")
        self.question = input("Enter Question")
        self.option1 = input("Enter First Option")
        self.option2 = input("Enter Second Option")
        self.option3 = input("Enter Third Option")
        self.option4 = input("Enter Fourth Option")
        self.correctAns = input("Enter Correct Ans")
        
    def printQuestionDetail(self):
        print("Question : ",self.question)
        print("Subject  : ",self.subject)
        print("Option1  : ",self.option1)
        print("Option2  : ",self.option2)
        print("Option3  : ",self.option3)
        print("Option4  : ",self.option4)
        
    def printQuestionDetailWithAns(self):
            self.printQuestionDetail()
            print("Ans      : ",self.correctAns)
            
    def setQuestionDetail(self, subject, question, op1, op2, op3, op4, ans):
        self.subject = subject
        self.question = question
        self.option1 = op1
        self.option2 = op2
        self.option3 = op3
        self.option4 = op4
        self.correctAns = ans