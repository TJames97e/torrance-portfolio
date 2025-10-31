class QuizApp:
    def __init__(self):
        self.username = ""
    
    def startup(self):
        self.greeting()
        self.username = input("Enter your name: ")
        print(f"Welcome {self.username}!")
        print()

    def greeting(self):
        print("-----------------------------")
        print("~~~~~ Welcome to PyQuiz ~~~~~")
        print("_____________________________")
        print()

    def menu_header(self):
        print("Please choose an option")
        print( "(M): Repeat this menu option")
        print( "(L): List all available quizzes")
        print( "(T): Take a quiz")
        print( "(E): Exit the program")
    
    def menu_error(self):
        print("That is not an option please make a different selection")

    def goodby(self):
        print("______________________________")
        print("~~~~~ Thanks for playing ~~~~~")
        print("______________________________")
        
    def menu(self):
        self.menu_header()
        selection = ""
        while(True):
            selection = input("Selection? ")

            if len(selection) == 0:
                self.menu_error()
                continue
            selection = selection.capitalize()
            if selection[0] == 'E':
                self.goodby()
                break
            elif selection[0] == 'M':
                self.menu_header()
                continue
            elif selection[0] == "L":
                print("\nAvailable quizzes are: ")
                # TODO reminder to list the quizzes
                print("---------------------\n")
                continue
            elif selection[0] == 'T':
                try:
                    quiznum = int(input("Enter the Quiz Number"))
                    print(f"You have selected quiz {quiznum}")
                    # TODO start the quiz 
                except:
                    self.menu_error()
            else:
                self.menu_error()


    def run(self):
        #starts the startup routine
        self.startup()                                  
        #starts the main program
        self.menu()
if __name__ == "__main__":
    app = QuizApp()
    app.run()

