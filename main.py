from tkinter import *
from tkinter import messagebox
from random import  choice, randint, shuffle
import  pyperclip
############### save Email and pssword #####



########Password Generator #######

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    random.shuffle(password_list)


    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)






def save():
    website = websit_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message= 'maad galin password iyo website toona ee fadlna gali labadaba ')
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"macluumaadkani sax mayihiin: \Email: {email}" f"\npassword: {password} \n mayahay mid saxa")

        if is_ok:
            with open('data.txt', "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n ")
                websit_entry.delete(0, END)
                password_entry.delete(0, END)










window = Tk()
window.title('Password ganerator')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file = 'al.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


#labels

website_label = Label(text="website")

website_label.grid(row=1, column=0)
email_label = Label(text="Email/username")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)


#Enteries


websit_entry = Entry(width=35)
websit_entry.grid(row =1, column=1, columnspan=2)
websit_entry.focus()
email_entry = Entry(width = 35)
email_entry.grid(row=2, column = 1, columnspan = 2)
email_entry.insert(0, "mizaajuhaa@gmail.com")
password_entry = Entry(width =21)
password_entry.grid(row = 3, column =1)


#buttons

generate_password_button = Button(text="Generate Password", command = generate_password)
generate_password_button.grid(row =3, column = 2)
add_button = Button(text = "Add", width= 36, command =save)
add_button.grid(row = 4, column = 1, columnspan = 2)

window.mainloop()
