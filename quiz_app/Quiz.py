class Quiz:
    def getData(self):
        self.title = input("Enter Quiz Title")
        self.subject = input("Enter Subject")
        self.totalNumberOfQuestions = int(input("How Many Questions you want to add?"))
        self.questions = []
        
    def mapQuestionToQuiz(self,question):
        self.questions.append(question)
    
    def printQuizDetail(self):
        print("Title           : ",self.title)
        print("Subject         : ",self.subject)
        print("Total Questions : ",self.totalNumberOfQuestions)    
        print("************Questions**************")
        for question in self.questions:
            question.printQuestionDetail()
            print("*********************************")
    def setData(self, title, subject, totalNumberOfQuestions):
        self.title = title
        self.subject = subject
        self.totalNumberOfQuestions = totalNumberOfQuestions
        self.questions = []
