from tkinter import messagebox

is_on = True
while is_on:
    answer = messagebox.askquestion(title="Your nightmare", message="Are you an idiot?")
    if answer == "no":
        messagebox.showinfo(message="Wrong")
    else:
        is_on = False
        messagebox.showinfo(message="I knew it")
