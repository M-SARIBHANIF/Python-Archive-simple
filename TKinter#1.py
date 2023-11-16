from tkinter import *
window = Tk()
window.title("Ostrava GUI")
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)


def button_click_event():
    new_text = input.get()
    my_label2 = Label(text="Yes INDEED", font=("Arial", 24, "bold"))
    my_label2.pack()
    my_label.config(text="YOU Praised The Sun!!!")
    my_label3 = Label(text=new_text, font=("Arial", 24, "bold"))
    my_label3.pack()

my_label = Label(text="Praise The Sun",font=("Arial",24,"bold"))
my_label.config(text="Praise The Sun!!!")
my_label.pack()

input = Entry()
input.pack()
#input.place(x=0, y=0)
# input.grid(column=5, row=5)

button = Button(text="Praise", command=button_click_event)
button.pack()
window.mainloop()