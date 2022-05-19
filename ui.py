from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizUI ():
    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.minsize(320, 300)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.quiz = quiz
        self.feedback_id = None
        
        # score
        self.score_display = Label(text="Score: 0", font=("Arial", 15, "italic"), fg="white", bg=THEME_COLOR)
        self.score_display.grid(column=1, row=0)
        
        # q? display
        self.display = Canvas(width=300, height=250)
        self.display_text = self.display.create_text(150, 125, text="Hello World",font=("Arial", 20, "italic"), width=250)
        self.display.grid(column=0, row=1, columnspan=2, pady=40)
        
        # buttons
        false_img = PhotoImage(file="./images/false.png")
        true_img = PhotoImage(file="./images/true.png")
        
        self.true_btn = Button(image=true_img, pady=50, command=self.is_true)
        self.true_btn.grid(column=0, row=2)
        
        self.false_btn = Button(image=false_img,pady=20, command=self.is_false)
        self.false_btn.grid(column=1, row=2)
        self.show_next_question()
        self.window.mainloop()
        
    def show_next_question(self):
        self.display.config(bg="white")
        if self.quiz.still_has_questions():
            q = self.quiz.next_question()
            self.display.itemconfig(self.display_text, text=q)
        else:
            self.display.itemconfig(self.display_text, text=f"End of Quiz\nYour score: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            self.score_display.config(text="")
            
            
    def is_true(self):
        ans = self.quiz.check_answer("True")
        self.score_display.config(text=f"Score: {self.quiz.score}")
        self.color_indication(ans=ans)
        
    def is_false(self):
        ans = self.quiz.check_answer("False")
        self.score_display.config(text=f"Score: {self.quiz.score}")
        self.color_indication(ans=ans)
    
    def color_indication(self, ans: bool):
        if ans:
            self.display.config(bg="green")
        else:
            self.display.config(bg="red")

        self.window.after(1000, self.show_next_question)
            