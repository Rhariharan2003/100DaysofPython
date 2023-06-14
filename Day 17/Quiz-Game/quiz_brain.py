
class QuizzBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        s = input(f"Q:{self.question_number} {current_question.text}. (True/False)")
        self.check_answer(s, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it Right.")
            self.score += 1

        else:
            print("You got it Wrong.")
        print(f"Your Score is : {self.score} / {self.question_number}")
        print(f"the correct answer is : {correct_answer}")
        print("\n")