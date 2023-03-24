import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for index in data.question_data:
    question_bank.append(Question(index["question"], index["correct_answer"]))

quizz = QuizBrain(question_bank)
while quizz.still_has_questions():
    quizz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quizz.score}/{quizz.question_number}")