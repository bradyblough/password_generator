# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import tkinter
from tkinter import messagebox
from tkinter import *
from random import choice, randint, shuffle
import pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    list_email = list(email)
    if len(website) == 0 or len(password) == 0 or len(email) == 0: # input validation
        messagebox.showinfo(message='Please enter at least 1 character for all fields')
    if '@' not in list_email:
        messagebox.showinfo(message='Please enter a valid email.')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'Email: {email}\n Password: {password}\n Save? ')
        if is_ok:
            with open('data.txt', 'a') as data_file: #write to file tp save input
                data_file.write(f'Website: {website} | Email/Username: {email} | Password: {password}\n')
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50, pady=20)
canvas = Canvas(height=200, width=200)

img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)



# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# buttons

generate = Button(text='Generate Password', command=generate_password)
generate.grid(row=3, column=2)
add = Button(text='Add', width=36, command=save)
add.grid(row=4, column=1)

tkinter.mainloop()
