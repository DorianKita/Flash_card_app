from tkinter import *
import pandas
import random

from numpy.ma.core import filled

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text= "French", fill="black")
    canvas.itemconfig(card_word, text= current_card["French"], fill="black")
    canvas.itemconfig(card_image, image= french_card)
    flip_timer = window.after(3000, flip_side)


def flip_side():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text= current_card['English'], fill="white")
    canvas.itemconfig(card_image, image= english_card)

def right():
   if current_card in to_learn:
       to_learn.remove(current_card)

   new_df = pandas.DataFrame(to_learn)
   new_df.to_csv("data/words_to_learn.csv", index=False)
   next_card()



window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_side)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness= 0)
french_card = PhotoImage(file="images/card_front.png")
english_card = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400,263, image= french_card)
canvas.grid(row=0, column=0, columnspan= 2)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth= 0,
                      command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth= 0,
                      command=right)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()