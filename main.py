from tkinter import *
import pandas
from random import randint, choice

BACKGROUND_COLOR = "#B1DDC6"

try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data=pandas.read_csv('data/french_words.csv')

data_dic=data.to_dict(orient='records')
card={}

def new_card():
    global card,timer
    card=choice(data_dic)
    window.after_cancel(timer)
    canvas.itemconfig(image, image=card_front)
    canvas.itemconfig(title,fill='black', text="French")
    canvas.itemconfig(word,fill='black',text=card["French"])
    timer=window.after(3000, flip_card)

def checked():
    data_dic.remove(card)
    new_data=pandas.DataFrame(data_dic)
    new_data.to_csv("data/words_to_learn.csv",index=False)
    window.after_cancel(timer)
    new_card()


def flip_card():
    global card
    canvas.itemconfig(image,image=card_back)
    canvas.itemconfig(title,fill='white', text="English")
    canvas.itemconfig(word,fill='white', text=card["English"])


window=Tk()
window.title("Flashy Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
timer=window.after(3000, flip_card)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)

card_front=PhotoImage(file='images/card_front.png')
card_back=PhotoImage(file="images/card_back.png")
tick=PhotoImage(file="images/right.png")
cross=PhotoImage(file="images/wrong.png")

image=canvas.create_image(400,263,image=card_front)
title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

wrong=Button(image=cross,highlightthickness=0,command=new_card)
wrong.grid(column=0,row=1)
right=Button(image=tick,highlightthickness=0,command=checked)
right.grid(column=1,row=1)


new_card()

window.mainloop()
