from cgitb import text
from cmath import exp
from re import X
from textwrap import fill
import tkinter as tk
from tkinter import LEFT, NW, Frame, Image, Label, PhotoImage, ttk, Button
#from PIL import ImageTk, Image
from tkinter import font
from tkinter.messagebox import YES
from turtle import bgcolor, color, width

pathHome = "C:\\Users\justin\Desktop\pi\pi-3b+\laundryArcade.png"
pathFold = "C:\\Users\justin\Desktop\pi\pi-3b+\laundrySide.png"
LARGEFONT =("Verdana", 20)
ARCADEFONT = ("ArcadeClassic", 16)
LARGEARCADEFONT = ("ArcadeClassic", 24)

class Home(tk.Frame):
    def printShirt():
        print("Shirt mode")
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Frame.configure(self, background="#3a4466",  )
        
       #
        img=PhotoImage(file=pathHome)
        img = img.zoom(50) #with 250, I ended up running out of memory
        img = img.subsample(43) #mechanically, here it is adjusted to 32 instead of 320
        imgLabel = Label(self,image=img, borderwidth=0)
        imgLabel.photo = img
        imgLabel.grid(column=0, row=0)


        
        
        # label of frame Layout 2
        #welcome = ttk.Label(self, text ="The Pi that Folds your Clothes",foreground='white',background="#272933" ,font = LARGEFONT, padding=40,  )
        #sub = ttk.Label(self, text ="  Choose a mode below \n       to get started", foreground='white',background="#272933",font = ("Verdana", 28), anchor="e",  )
        #welcome.grid(row = 0, column = 1, )
        #sub.grid(row = 2, column = 1,  )
        
        #Creating a frame exclusively for the buttons
        self.frame_buttons = tk.Frame(parent)
        self.frame_buttons.grid(row = 1, column = 0, columnspan = 3,)
        self.frame_buttons.grid_remove()
        
        #Gridding self.frame_buttons
        self.frame_buttons.grid_columnconfigure((0,1), weight = 2)
        self.frame_buttons.grid_rowconfigure(0, weight = 1)

        # Styles for buttons
        style = ttk.Style()
        style.theme_use("default")

        style.configure("home.TButton", foreground="white", background="#3a4466", font=ARCADEFONT,)
        # End of Styles for buttons

        button1 = ttk.Button(self.frame_buttons ,text ="Let's Fold some Clothes" ,command = lambda : controller.show_frame(FoldClothes),width=23 ,style="home.TButton",   )
        button1.grid(row = 0, column = 0, ipady=38 )

        button2 = ttk.Button(self.frame_buttons, text ="Tell me a joke", command = lambda : controller.show_frame(Joke), width=23, style="home.TButton" ) 
        button2.grid(row = 0, column = 1, ipady=38)

        button3 = ttk.Button(self.frame_buttons, text ="Object Detection", command = lambda : controller.show_frame(FoldClothes), width=23, style="home.TButton" )
        button3.grid(row = 0, column = 2,ipady=38)
        
    def tkraise(self):
        self.frame_buttons.grid()
        self.frame_buttons.tkraise()
        tk.Frame.tkraise(self)