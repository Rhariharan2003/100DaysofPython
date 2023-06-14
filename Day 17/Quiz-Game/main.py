from data import question_data
from quiz_brain import QuizzBrain
from question_model import Question

question_bank = []

for q in question_data:
    text_q = q["text"]
    answer_q = q["answer"]
    new_question = Question(text_q, answer_q)
    question_bank.append(new_question)

a = QuizzBrain(question_bank)
while a.still_has_questions():
    a.next_question()

print("The Quiz Was Completed.")
print(f"The Final score is : {a.score}")