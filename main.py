from tkinter import *
# the message box is not class that's why it needs to be imported
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().upper()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title=website,
        #                                message=f"These are the details entered: \n Email: {email}\nPassword: {password}\n \nIs it ok to save?")
        # if is_ok:
        # with open("pw_saved_file.txt", "a") as data_file:
            # data_file.write(f"{website} | {email} | {password}\n")
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4 )
        else:
            # Updating
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ----------------------------SEARCH FUNCTION--------------------------- #


def find_password():
    website = website_input.get().upper()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data Does not Exist!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for the {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

search_btn = Button(text="Search", width=14, command=find_password)
search_btn.grid(column=2, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_input = Entry(width=39)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "yong.s.choi2@gmail.com")
password_label = Label(text="Password:")
password_label.grid(column=0, row=4)

password_input = Entry(width=21)
password_input.grid(column=1, row=4)

password_generator_btn = Button(text="Generate Password", command=generate_password, width=14)
password_generator_btn.grid(column=2, row=4)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=5, columnspan=2)

window.mainloop()
