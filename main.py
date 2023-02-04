import pandas as pd
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
FLIPPING_TIMER = 8000
current_card = {}
to_learn = {}
current_language = "en"
known_words = []

# #------------------------------------- Japanese version -------------------------------------#
# UI to check which vocabulary should be added
check_window = Tk()
check_window.geometry("350x200")
check_window.title("What do you want to learn?")
jlpt1 = IntVar()
jlpt1_c = Checkbutton(master=check_window, text="JLPT1", variable=jlpt1, onvalue=1, offvalue=0)
jlpt1_c.pack()

jlpt2 = IntVar()
jlpt2_c = Checkbutton(master=check_window, text="JLPT2", variable=jlpt2, onvalue=1, offvalue=0)
jlpt2_c.pack()

jlpt3 = IntVar()
jlpt3_c = Checkbutton(master=check_window, text="JLPT3", variable=jlpt3, onvalue=1, offvalue=0)
jlpt3_c.pack()

jlpt4 = IntVar()
jlpt4_c = Checkbutton(master=check_window, text="JLPT4", variable=jlpt4, onvalue=1, offvalue=0)
jlpt4_c.pack()

jlpt5 = IntVar()
jlpt5_c = Checkbutton(master=check_window, text="JLPT5", variable=jlpt5, onvalue=1, offvalue=0)
jlpt5_c.pack()

exit_button = Button(check_window, text="Start learning", command=check_window.destroy)
exit_button.pack(pady=20)

check_window.mainloop()
# Japanese word data
jlpt1_learn = ""
jlpt2_learn = ""
jlpt3_learn = ""
jlpt4_learn = ""
jlpt5_learn = ""

if jlpt1.get() == 1:
    data_jlpt1 = pd.read_csv("./data/n1.csv")
    jlpt1_learn = data_jlpt1.to_dict(orient="records")
if jlpt2.get() == 1:
    data_jlpt2 = pd.read_csv("./data/n2.csv")
    jlpt2_learn = data_jlpt2.to_dict(orient="records")
if jlpt3.get() == 1:
    data_jlpt3 = pd.read_csv("./data/n3.csv")
    jlpt3_learn = data_jlpt3.to_dict(orient="records")
if jlpt4.get() == 1:
    data_jlpt4 = pd.read_csv("./data/n4.csv")
    jlpt4_learn = data_jlpt4.to_dict(orient="records")
if jlpt5.get() == 1:
    data_jlpt5 = pd.read_csv("./data/n5.csv")
    jlpt5_learn = data_jlpt5.to_dict(orient="records")

selected_learn_list = [jlpt1.get(), jlpt2.get(), jlpt3.get(), jlpt4.get(), jlpt5.get()]
selectable_learn_list = [jlpt1_learn, jlpt2_learn, jlpt3_learn, jlpt4_learn, jlpt5_learn]
to_learn_list = [selectable_learn_list[num] for num in range(len(selectable_learn_list)) if selected_learn_list[num] == 1]
to_learn = []
for list in to_learn_list:
    to_learn.extend(list)
#------------------------------------- French version -------------------------------------#
# try:
#     data = pd.read_csv("./data/words_to_learn.csv")
# except FileNotFoundError:
#     original_data = pd.read_csv("./data/french_words.csv")
#     to_learn = original_data.to_dict(orient="records")
# else:
#     to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer, current_language
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_language = "jp"
    # canvas.itemconfig(card_title, text="French", fill="black")
    # canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    # Japanese
    canvas.itemconfig(card_title, text="Japanese", fill="black")
    canvas.itemconfig(card_expression, text=current_card["expression"], fill="black", font=("Ariel", 60, "bold"))
    canvas.itemconfig(card_reading, text=current_card["reading"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(FLIPPING_TIMER, func=flip_card)

def flip_card():
    global current_language
    current_language = "en"
    canvas.itemconfig(card_title, text="English", fill="white")
    # canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    # Japanese
    canvas.itemconfig(card_expression, text=current_card["meaning"], fill="white", font=("Ariel", 20, "bold"))
    canvas.itemconfig(card_reading, text="", fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    # known_words.append(current_card)
    to_learn.remove(current_card)
    # data = pd.DataFrame(to_learn)
    # data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def turn_card():
    global current_language
    if current_language == "en":
        canvas.itemconfig(card_title, text="Japanese", fill="black")
        canvas.itemconfig(card_expression, text=current_card["expression"], fill="black", font=("Ariel", 60, "bold"))
        canvas.itemconfig(card_reading, text=current_card["reading"], fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
        current_language = "jp"
    else:
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_expression, text=current_card["meaning"], fill="white", font=("Ariel", 20, "bold"))
        canvas.itemconfig(card_reading, text="", fill="white")
        canvas.itemconfig(card_background, image=card_back_img)
        current_language = "en"

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(FLIPPING_TIMER, func=flip_card)

canvas = Canvas(width= 800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image((400, 263), image=card_front_img)
# card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
# card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
# Japanese
card_title = canvas.create_text(400, 150, text="Japanese", font=("Ariel", 50, "italic"))
card_expression = canvas.create_text(400, 263, text="expression", font=("Ariel", 60, "bold"))
card_reading = canvas.create_text(400, 363, text="reading", font=("Ariel", 40, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

turn_button = Button(text="turn card", highlightthickness=0, command=turn_card)
turn_button.grid(row=1, column=1)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=2)

next_card()





window.mainloop()