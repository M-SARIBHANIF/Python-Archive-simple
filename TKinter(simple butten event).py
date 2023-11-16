from tkinter import *
def tokens_to_Blessing():
        n = int(token_input.get())
        temp.config(text = f"{n} Blessings")

window = Tk()
window.title("GODDES STATUE")
window.config(padx=5,pady=5)
token_input = Entry(width=7)
token_input.grid(column=1,row=0)
token_lable = Label(text="Tokens")
token_lable.grid(column=2,row=0)

Gift_Recieved = Label(text="Gift Recieved")
Gift_Recieved.grid(column=0,row=1)
temp = Label(text="--")
temp.grid(column=1,row=1)
Gift = Label(text="BISTWOED")
Gift.grid(column=2,row=1)
PRAISE = Button(text="PRAISE",command=tokens_to_Blessing)
PRAISE.grid(column=1,row=2)

window.mainloop()