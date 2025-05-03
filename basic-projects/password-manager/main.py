from tkinter import messagebox
from tkinter import *
import pyperclip
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)  # make sure that the password is copied

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = entry_website.get()
    email = entry_email_uname.get()
    password = entry_password.get()
    res = {
        web: {
            'email': email,
            'password': password,
        }
    }

    if web and email and password:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email} \n"
                                                          f"Password: {password}\nIs it ok to save?"
                                                          f"\nNote:The password will copied")

        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(res, data_file, indent=4)
            else:
                data.update(res)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_email_uname.delete(0, END)
                entry_password.delete(0, END)

    else:
        messagebox.showerror(title="Oops", message="Please don't leave fields empty!")

    entry_website.focus()


# ---------------------------- Search ------------------------------- #


def search_data():
    web = entry_website.get()
    if web:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title='Error',
                                 message='Not data file found.')
        else:
            try:
                web_info = data[web]
            except KeyError:
                messagebox.showerror(title='Error',
                                     message=f'No details for {web} exists.')
            else:
                messagebox.showinfo(title=web, message=f"Email: {web_info['email']}\nPassword: {web_info['password']}")
    else:
        messagebox.showerror(title='Error',
                             message='Website box empty.')


# ---------------------------- UI SETUP ------------------------------- #
# my_email =
window = Tk()
window.title("Password Generator")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
Label(text="Website:").grid(column=0, row=1)
Label(text="Email/Username:").grid(column=0, row=2)
Label(text="Password:").grid(column=0, row=3)

# Entry
entry_website = Entry()
entry_website.grid(column=1, row=1, sticky="EW")
entry_website.focus()
entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")
# entry_email_uname.insert(END, my_email)
entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

# Buttons
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")
add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
search_btn = Button(text='Search', command=search_data)
search_btn.grid(column=2, row=1, sticky='EW')

mainloop()
