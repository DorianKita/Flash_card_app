from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text= "French")
    canvas.itemconfig(card_word, text= current_card['French'])


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness= 0)
image = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image= image)
canvas.grid(row=0, column=0, columnspan= 2)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth= 0,
                      command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth= 0,
                      command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()