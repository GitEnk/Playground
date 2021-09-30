from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.pack()
canvas.grid(column=1, row=0)

lb_website = Label(text="Website:").grid(column=0,row=1)
en_website = Entry(width=35).grid(column=1, row=1, columnspan=2)

lb_account = Label(text="Email/Username:").grid(column=0, row=2)
en_account = Entry(width=35)
en_account.insert(0, "address@email.com")
en_account.grid(column=1, row=2, columnspan=2)

lb_pwd = Label(text="Password").grid(column=0, row=3)
en_pwd = Entry(width=21).grid(column=1, row=3)
btn_pwd = Button(text="Generate Password").grid(column=2, row=3)
btn_add = Button(text="Add", width=36).grid(column=1, row=4, columnspan=2)
window.mainloop()