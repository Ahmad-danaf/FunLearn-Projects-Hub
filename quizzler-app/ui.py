from quiz_brain import QuizBrain
import tkinter

THEME_COLOR = "#375362"
SCORE_FONT_INFO = ('Arial', 12)
Q_FONT_INFO = ('Arial', 20, 'italic')

class QuizInterface:
    
    def __init__(self, quiz_brain : QuizBrain) -> None:
        self.quiz_brain = quiz_brain
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_text = tkinter.Label(text='score: 0', font=SCORE_FONT_INFO, bg=THEME_COLOR, fg='white')
        self.score_text.grid(column=1, row=0)
        
        self.canvas = tkinter.Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 250/2, text='Q text goes here', width=280, font=Q_FONT_INFO, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        # Buttons
        true_img = tkinter.PhotoImage(file='images/true.png')
        false_img = tkinter.PhotoImage(file='images/false.png')
        self.true_btn = tkinter.Button(image=true_img,
                                       highlightthickness=0,
                                       bg=THEME_COLOR,
                                       bd=0,
                                       command=self.pressed_true)
        self.false_btn = tkinter.Button(image=false_img,
                                        highlightthickness=0,
                                        bg=THEME_COLOR,
                                        bd=0,
                                        command=self.pressed_false)
        self.true_btn.grid(column=1, row=2)
        self.false_btn.grid(column=0, row=2)
      
        self.get_next_question()
        
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_text.config(text=f'Score: {self.quiz_brain.score}')
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.buttons_state(tkinter.ACTIVE)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've completed the quiz\n\
                                       Your final score is: {self.quiz_brain.score}/{self.quiz_brain.question_number}")
            self.buttons_state(tkinter.DISABLED)

    
    def pressed_true(self):
        res = self.quiz_brain.check_answer('True')
        self.give_feedback(res)
        
    
    def pressed_false(self):
        res = self.quiz_brain.check_answer('False')
        self.give_feedback(res)
        
        
    def give_feedback(self, is_right:bool):
        self.buttons_state(tkinter.DISABLED)
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
            
        self.window.after(1000, self.get_next_question)
        
        
    def buttons_state(self,state:str):
        self.true_btn.config(state=state)
        self.false_btn.config(state=state)