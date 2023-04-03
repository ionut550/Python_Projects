from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.quote_text = self.canvas.create_text(
            150,
            125,
            width=290,
            text="Text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        check_img = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_img, highlightthickness=0, command=self.true_button)
        self.check_button.grid(row=2, column=0)

        x_img = PhotoImage(file="images/false.png")
        self.x_button = Button(image=x_img, highlightthickness=0, command=self.false_button)
        self.x_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.quote_text, text="You've reached the end of the quiz")
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def true_button(self):
        self.get_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        self.get_feedback(self.quiz.check_answer("False"))

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
