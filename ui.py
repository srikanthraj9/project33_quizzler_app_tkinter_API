THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from tkinter import *
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.configure(padx=20,pady=20,bg=THEME_COLOR)

        self.score_lable = Label(text="score: 0",fg="white",bg=THEME_COLOR)
        self.score_lable.grid(row=0,column=1)

        self.canvas =Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125 ,width=280,text="some question text",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.True_button =Button(image=true_image,highlightthickness=0,command= self.true_preessed)
        self.True_button.grid(row = 2,column=0)
        false_image = PhotoImage(file="images/false.png")

        self.false_button = Button(image=false_image, highlightthickness=0,command= self.flase_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lable.config(text=f"score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="you've reached the end of the question")
            self.True_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_preessed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def flase_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)