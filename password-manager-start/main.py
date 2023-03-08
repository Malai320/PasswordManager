import json.decoder
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy
from json import dump, load
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = ''.join(password_list)

    copy(password)
    password_entry.delete(0, END)
    password_entry.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def search_password():
    website = website_entry.get().title()
    if len(website) == 0:
        messagebox.showinfo(title="Error", message="Please fill in the website entry")
    else:
        try:
            with open("passwords.json", "r") as file:
                data = load(file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="There are no passwords saved")
        else:
            if website in data:
                messagebox.showinfo(title=website, message=f"Email : {data[website]['email']}\nPassword : {data[website]['password']}")
            else:
                messagebox.showinfo(title="Sorry", message=f"No site with the name {website} was found")



def add_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website.title(): {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please fill all of the fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            try:
                file = open("passwords.json", "r")
            except FileNotFoundError:
                file = open("passwords.json", "w")
            finally:
                file.close()
            with open("passwords.json", "r") as file:
                # method: we open as read, load the entire dictionary of passwords from json file
                # and then we just update it to add a new data to it
                try:
                    data = load(file)
                except json.decoder.JSONDecodeError:
                    data = new_data
                else:
                    data.update(new_data)
            with open("passwords.json", "w") as file:
                dump(data, file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_email_username = Label(text="Email/Username:")
label_password = Label(text="Password:")

label_website.grid(row=1, column=0)
label_email_username.grid(row=2, column=0)
label_password.grid(row=3, column=0)

website_entry = Entry(width=35)
email_username_entry = Entry(width=53)
password_entry = Entry(width=35)

website_entry.grid(row=1, column=1)
email_username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate password", width=14, command=generate_password)
add_button = Button(text="Add", width=45, command=add_password)
search_button = Button(text="Search", width=14, command=search_password)

generate_password_button.grid(row=3, column=2)
search_button.grid(row=1, column=2)
add_button.grid(row=4, column=1, columnspan=2)

website_entry.focus()
email_username_entry.insert(END, string="quluzadea73@gmail.com")

window.mainloop()
