# Create your classes here

class Student:
    
    def __init__(self, first_name, last_name, address):

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question:
    
    def __init__(self, question, correct_answer):

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):

        print(self.question)
        user_input = input("Your answer here: ")
        
        if user_input == self.correct_answer:
            return True
        else:
            return False

class Exam:
    
    def __init__(self, name):

        self.name = name
        self.questions = []

    def add_question(self, question):

       self.questions.append(question)

    def administer(self):

        score = 0
        q_num = 0
        
        for q in self.questions:
            if q.ask_and_evaluate():
                score += 1
            else:
                score += 0
            q_num += 1

        return print((score/q_num) * 100)













