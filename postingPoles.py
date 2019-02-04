from tkinter import *
import random
import csv

fields = []
rows = []
window = Tk()
window.title("Carrion Crown Posting Poles")
window.geometry('700x400')

with open("postingPoleData.csv","r") as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        rows.append(row)

max = len(rows) - 1

rand0 = random.randint(1,max)
rand1 = random.randint(1,max)
rand2 = random.randint(1,max)
rand3 = random.randint(1,max)

lbl = Label(window, text="Generate Poles")
lbl.place(x=350, y=10, anchor="center")

def generate_button():
    rand0 = random.randint(1,max)
    rand1 = random.randint(1,max)
    while( rand1 == rand0 ):
        rand1 = random.randint(1,max)

    rand2 = random.randint(1,max)
    while( rand2 == rand1 or rand2 == rand0 ):
        rand2 = random.randint(1,max)

    rand3 = random.randint(1,max)
    while( rand3 == rand2 or rand3 == rand2 or rand3 == rand1):
        rand3 = random.randint(1,max)

    txt1.config(text=rows[rand0][0])
    txt2.config(text=rows[rand1][0])
    txt3.config(text=rows[rand2][0])
    txt4.config(text=rows[rand3][0])

    Tk.update

btn = Button(window, text="Generate", command=generate_button)
btn.place(x=350, y=40, anchor="center")

txt1 = Label(window,width=100,text=rows[rand0][0])
txt1.place(x=350, y=75, anchor="center")

txt2 = Label(window,width=100,text=rows[rand1][0])
txt2.place(x=350, y=100, anchor="center")

txt3 = Label(window,width=100,text=rows[rand2][0])
txt3.place(x=350, y=125, anchor="center")

txt4 = Label(window,width=100,text=rows[rand3][0])
txt4.place(x=350, y=150, anchor="center")

window.mainloop()