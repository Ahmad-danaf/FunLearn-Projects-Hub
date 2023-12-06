from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    file = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    file = pd.read_csv('data/English-words.csv')  # first time running the program
    words_to_learn = file.to_dict(orient="records")
else:
    words_to_learn = file.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)

    canvas.itemconfig(card_img, image=front_card_img)
    canvas.itemconfig(card_word, text=current_card['English'], fill='black')
    canvas.itemconfig(card_title, text='English', fill='black')
    flip_timer = window.after(3000, flip_card)


def is_known():
    words_to_learn.remove(current_card)
    next_card()


def flip_card():
    canvas.itemconfig(card_title, text="Hebrew", fill="white")
    canvas.itemconfig(card_word, text=current_card["Hebrew"], fill="white")
    canvas.itemconfig(card_img, image=back_card_img)


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

front_card_img = PhotoImage(file='images/card_front.png')
back_card_img = PhotoImage(file='images/card_back.png')
right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')

canvas = Canvas(width=800, height=526)
card_img = canvas.create_image(400, 526/2, image=front_card_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Titles & Words ->The text
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), width=780)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_btn = Button(image=right_img, highlightthickness=0, bd=0, command=is_known)
right_btn.grid(column=1, row=1)
wrong_btn = Button(image=wrong_img, highlightthickness=0, bd=0, command=next_card)
wrong_btn.grid(column=0, row=1)


next_card()


window.mainloop()

# create new file without the words that label as known
df = pd.DataFrame(words_to_learn)
df.to_csv('data/words_to_learn.csv', index=False)

