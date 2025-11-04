class Quiz:
    def __init__(self):
        self.name = ""
        self.description = "" 
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0
    def print_header(self):
        print("\n\n*********************************")
        print(f"Quiz Name {self.name}")
        print(f"Quiz Description {self.description}")
        print(f"Quiz Questions {len(self.questions)}")
        print(f"Quiz Total Points {self.total_points}")
        print("**********************************\n")

    def print_results(self):
        print("\n\n*********************************")
        print("**********************************\n")
    
    def take_quiz(self):
        self.score = 0
        self.correct_count = 0
        for j in self.questions:
            j.is_correct = False

        self.print_header()
        for j in self.questions:
            j.ask()
            if(j.is_correct):
                self.correct_count += 1
                self.score += j.points
        print("-----------------\n")

        return(self.score, self.correct_count, self.total_points)
    
class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ''
        self.is_correct = False

class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while(True):
            print(f'(T)rue or (F)alse: {self.text}')
            response = input("?")

            if len(response) == 0:
                print("Sorry that is not a valid response please try again")
                continue 

            response  = response.lower()

            if response[0] != "t" and response[0] != "f":
                print("Sorry that is not a valid response please try again")
                continue

            if response[0] == self.correct_answer:
                self.is_correct = True
            break
class QuestionMC(Question):
    def __init__(self):
        super().__init__()
        self.answer = []

    def ask(self):
        while(True):
            print(self.text)

            for i in self.answer:
                print(f"{i.name} {i.text}")
            response = input("?")

            if len(response) == 0:
                print("Sorry that is not a valid response please try again")
                continue 
                        
            response  = response.lower()
            if response[0] == self.correct_answer:
                self.is_correct =True 
            break 

class Answer:
    def __init__(self):
        self.text = ''
        self.name = ''


# if __name__ == "__main__":
#     qz = Quiz()
#     qz.name = "Sample Quiz"
#     qz.description = "This is a sample quiz!"

#     q1 = QuestionTF()
#     q1.text = "Broccoli is good for you"
#     q1.points = 5
#     q1.correct_answer = "t"
#     qz.questions.append(q1)

#     q2 = QuestionMC()
#     q2.text = "What is 2+2?"
#     q2.points = 10
#     q2.correct_answer = "b"
#     ans = Answer()
#     ans.name = "a"
#     ans.text = "3"
#     q2.answer.append(ans)
#     ans = Answer()
#     ans.name = "b"
#     ans.text = "4"
#     q2.answer.append(ans)
#     ans = Answer()
#     ans.name = "c"
#     ans.text = "5"
#     q2.answer.append(ans)
#     qz.questions.append(q2)

#     qz.total_points = q1.points + q2.points
#     result = qz.take_quiz()
#     print(result)