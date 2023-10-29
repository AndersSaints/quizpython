from tkinter import *
import tkinter as tk
import pandas as pd
import random

# load questions
df = pd.read_excel('questions.xlsx')
questions = df.sample(n=10).values.tolist()

# global variables
score = 0
current_question = 0

# functions
def check_answer(answer):
    global score, current_question
    
    if answer == correct_answer.get():
        score+=1
        
    current_question +=1

    if current_question < len(questions):
        next_question()
    else:
        pass
        #show_result()


def next_question():
    question, option1, option2, option3, option4, answer = questions[current_question]
    question_label.config(text=question)
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda:check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda:check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda:check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda:check_answer(4))

    correct_answer.set(answer)



window = tk.Tk()
window.title('Quiz')
window.geometry("400x450")
bg_color = "#ECECEC"
text_color = "#333333"
button_color = "#cf811b"
button_text_color = "#ffffff"

window.config(bg=bg_color)
window.option_add("*Font", "Arial")

# icon
app_icon = PhotoImage(file="qmark.png")
app_label = tk.Label(window, image=app_icon, bg=bg_color)
app_label.pack(pady=10)

# interface components
question_label = tk.Label(window, text="Question", wraplength=380, bg=bg_color, fg=text_color, font=("Arial", 12, "bold"))
question_label.pack(pady=20)

correct_answer = tk.IntVar()

option1_btn = tk.Button(window, text="Option 1", width=30, bg=button_color, fg=button_text_color, font=("Arial", 10, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(window, text="Option 2", width=30, bg=button_color, fg=button_text_color, font=("Arial", 10, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(window, text="Option 3", width=30, bg=button_color, fg=button_text_color, font=("Arial", 10, "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(window, text="Option 4", width=30, bg=button_color, fg=button_text_color, font=("Arial", 10, "bold"))
option4_btn.pack(pady=10)

play_again_btn = tk.Button(window, text="Play again!", width=30, bg=button_color, fg=button_text_color, font=("Arial", 10, "bold"))
#play_again_btn.pack(pady=20)


next_question()
window.mainloop()
