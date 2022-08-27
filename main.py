from tkinter import *
import pandas as pd
import random

LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn={}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_backround, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_backround, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# TODO: 2. Create Front Card with random word in german.
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_backround = canvas.create_image(400, 268, image=card_front_img)
card_title = canvas.create_text(400, 150, text="German", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
# # -----------------------------RANDOM WORD DISPLAYED IN CARD ----------------------------

# current_card = random.choice(to_learn)
# card_word = canvas.create_text(400, 263, text=current_card["German"], font=WORD_FONT)
# canvas.grid(column=0, row=0)

# TODO: 3. Create a button X
image_x = PhotoImage(file="images/wrong.png")
button_x = Button(image=image_x, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
button_x.grid(column=0, row=1)

# TODO: 4. Create a button V
image_v = PhotoImage(file="images/right.png")
button_x = Button(image=image_v, highlightthickness=0, command=is_known)
button_x.grid(column=1, row=1)

next_card()

window.mainloop()
