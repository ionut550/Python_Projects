class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        user_choise = input(f"Q. {self.question_number +1 } {self.question_list[self.question_number].text} (True/False): ").lower()
        self.question_number += 1
        self.check_answer(user_choise, self.question_list[self.question_number - 1].answer)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_choise, correct_answer):
        if user_choise == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}\n\n\n")