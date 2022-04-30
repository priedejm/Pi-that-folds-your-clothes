from tkinter import *
import random

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')



joke = Button(text="Disable", command=ws.destroy, background='pink') 
joke.place(x=75, y=50)
#create an empty label for joke here 
jokeTextBox = Label(ws)
jokeTextBox.place(x=25, y=150)

ws.mainloop()

