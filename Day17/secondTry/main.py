from question_model import question_bank
from question import Question
from quiz_brain import QuizBrain

def main():
    QuizBrain.next_question(question_bank)

main()
