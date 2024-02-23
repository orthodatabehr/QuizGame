from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for duma in question_data:
    new_question = Question(duma['text'], duma['answer'])
    question_bank.append(new_question)

duma = QuizBrain(question_bank)

while duma.still_has_questions():
    duma.next_question()

print("You've completed the quiz!")
print(f'Your final score was {duma.score}/{duma.question_number}.')
