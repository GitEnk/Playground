import tkinter

window = tkinter.Tk()
window.title("GUIGUIGUI")

window.minsize(width=400, height=300)

label1 = tkinter.Label(text="My label")
label2 = tkinter.Label(text="A second label")

label1.pack()
label2.pack()
window.mainloop()