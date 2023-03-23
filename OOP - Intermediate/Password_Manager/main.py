from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(3, 5))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(3, 5))]

    complete_password = password_letters + password_symbols + password_numbers
    random.shuffle(complete_password)
    complete_password = "".join([str(character) for character in complete_password])

    password_entry.delete(0, END)
    password_entry.insert(0, f"{complete_password}")
    # Copy the generated password to clipboard
    pyperclip.copy(complete_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()

    if website == "website.com" or user == "example@gmail.com" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        message = messagebox.askokcancel(title=website, message=f"These are the details entered:"
                                                                f"\nEmail: {user}\nPassword: {password}"
                                                                f"\nIs is ok to save?")

        if message:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {user} | {password} \n")
            website_entry.delete(0, END)
            handle_focus_out_website("")
            user_entry.delete(0, END)
            handle_focus_out_username("")
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


def handle_focus_in_username(_):
    if user_entry.get() == "example@gmail.com":
        user_entry.delete(0, END)
        user_entry.config(fg="black")


def handle_focus_out_username(_):
    if user_entry.get() == "":
        user_entry.config(fg="Gray")
        user_entry.insert(0, "example@gmail.com")


def handle_focus_in_website(_):
    if website_entry.get() == "website.com":
        website_entry.delete(0, END)
        website_entry.config(fg="black")


def handle_focus_out_website(_):
    if website_entry.get() == "":
        website_entry.config(fg="Gray")
        website_entry.insert(0, "website.com")


# Logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=52, fg="gray")
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.insert(0, "website.com")
website_entry.bind("<FocusIn>", handle_focus_in_website)
website_entry.bind("<FocusOut>", handle_focus_out_website)

# Email/Username
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
user_entry = Entry(width=52, fg="Gray")
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "example@gmail.com")
user_entry.bind("<FocusIn>", handle_focus_in_username)
user_entry.bind("<FocusOut>", handle_focus_out_username)

# Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
