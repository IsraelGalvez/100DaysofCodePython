from question_model import *
from data import  *
from quiz_brain import *

question_bank = []

for data in question_data:
    question_text = data["question"]
    question_answer = data["correct_answer"]
    new_question = Questions(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()