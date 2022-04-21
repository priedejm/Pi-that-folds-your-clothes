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
from Greetings import *

#from PIL import ImageTk, Image 
  
LARGEFONT =("Verdana", 20)
ARCADEFONT = ("ArcadeClassic", 16)
LARGEARCADEFONT = ("ArcadeClassic", 24)

#####################
# Helper Functions
#####################
#
#
# Print shirt method 
#
shirtCount = 0
def printShirt():
    print("Shirt mode")
    shirtCount += 1
    print(shirtCount)
    
#
# Print Pants method
#
def printPants():
    print("Pants mode")
    pantsCount = pantsCount + 1





pathHome = "C:\\Users\justin\Desktop\pi\Pi-that-folds-your-clothes\laundryArcade.png"
pathFold = "C:\\Users\justin\Desktop\pi\Pi-that-folds-your-clothes\laundrySide.png"
  
#####################
# Main Method
#####################
#
# Entire Frame, holds each screen tab
#
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        #Gridding the tkinter window
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
         
        # creating a container
        container = tk.Frame(self) 
        container.grid(row=0, column=0, sticky = 'nsew')
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Home, FoldClothes, Joke):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # Home, FoldClothes, Joke respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Home)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#####################
# Home Screen
#####################
#
# Responsible for Welcome Screen
#
class Home(tk.Frame):
    def printShirt():
        print("Shirt mode")
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Frame.configure(self, background="#3a4466",  )
        
        # Background Image
        img=PhotoImage(file=pathHome)
        img = img.zoom(50) 
        img = img.subsample(43) 
        imgLabel = Label(self,image=img, borderwidth=0)
        imgLabel.photo = img
        imgLabel.grid(column=0, row=0)

        
        #Creating a frame exclusively for the Bottom tab buttons
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

        # Beginning of bottom tab buttons
        button1 = ttk.Button(self.frame_buttons ,text ="Let's Fold some Clothes" ,command = lambda : controller.show_frame(FoldClothes),width=23 ,style="home.TButton",   )
        button1.grid(row = 0, column = 0, ipady=38 )

        button2 = ttk.Button(self.frame_buttons, text ="Tell me a joke", command = lambda : controller.show_frame(Joke), width=23, style="home.TButton" ) 
        button2.grid(row = 0, column = 1, ipady=38)

        button3 = ttk.Button(self.frame_buttons, text ="Object Detection", command = lambda : controller.show_frame(FoldClothes), width=23, style="home.TButton" )
        button3.grid(row = 0, column = 2,ipady=38)
        # End of bottom tab buttons
        
    def tkraise(self):
        self.frame_buttons.grid()
        self.frame_buttons.tkraise()
        tk.Frame.tkraise(self)
    
    

#####################
# Fold Clothes Screen
#####################
class FoldClothes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Frame.configure(self, bg="#3a4466")
       
        # Beginning of Image
        img=PhotoImage(file=pathFold)
        img = img.zoom(50) 
        img = img.subsample(43) 
        imgLabel = Label(self,image=img, borderwidth=0)
        imgLabel.photo = img
        imgLabel.place(x=0,y=0, )
        # End of Image

        # Styles for shirt and pants mode buttons
        style = ttk.Style()
        style.map("shirtPants.TButton",
          background = [("active", "#F60081"), ("!active", "#c0cbdc")],
          foreground = [("active", "white"), ("!active", "#F60081")], )
        style.configure("shirtPants.TButton", font=ARCADEFONT)
        # Styles for shirt and pants mode buttons

        # Beginning of buttons, shirt and pants
        shirtButton = ttk.Button(self, text= "Shirt Mode",padding=15,command= lambda: [printShirt()], style='shirtPants.TButton')
        shirtButton.place(x=140, y=75)
        pantsButton = ttk.Button(self, text= "Pants Mode",padding=15,command= lambda: [printPants()], style='shirtPants.TButton')
        pantsButton.place(x=320, y=75)
        # End of buttons, shirt and pants

        # Beginning of Current Session on right side of display
        statshere = ttk.Label(self, text ="Current Session", font = LARGEARCADEFONT, background="#3a4466", foreground="white", )
        statshere.place(x=500, y=15)

        shirtsFolded = ttk.Label(self, text ="shirts folded:", font = ARCADEFONT, background="#3a4466", foreground="white")
        shirtsFolded.place(x=500, y=65)

        pantsFolded = ttk.Label(self, text ="pants folded:", font = ARCADEFONT, background="#3a4466", foreground="white")
        pantsFolded.place(x=500, y=100)

        totalFolded = ttk.Label(self, text ="Total:", font = ARCADEFONT, background="#3a4466", foreground="white")
        totalFolded.place(x=500, y=135) 
        # End of Current Session on right side of display

        timeSaved = ttk.Label(self, text ="Time Saved:", font = LARGEARCADEFONT, background="#3a4466", foreground="white", )
        timeSaved.place(x=500, y=200)


        
        #Creating a frame exclusively for the bottom tab buttons
        self.frame_buttons = tk.Frame(parent)
        self.frame_buttons.grid(row = 1, column = 0, columnspan = 3)
        self.frame_buttons.grid_remove() 
        #Gridding self.frame_buttons
        self.frame_buttons.grid_columnconfigure((0,1), weight = 1)
        self.frame_buttons.grid_rowconfigure(0, weight = 1)
        
        # Styles for buttons
        style = ttk.Style()
        style.theme_use("default")
        style.configure("clothes.TButton",  font=ARCADEFONT,foreground="white", background="#3a4466",  )
        # End of Styles for buttons

        # Beginning of bottom tab buttons
        button1 = ttk.Button(self.frame_buttons ,text ="Home" ,command = lambda : controller.show_frame(Home),width=23 ,style="clothes.TButton",  )
        button1.grid(row = 0, column = 0, ipady=38 )

        button2 = ttk.Button(self.frame_buttons, text ="Tell me a joke", command = lambda : controller.show_frame(Joke), width=23, style="clothes.TButton" ) 
        button2.grid(row = 0, column = 1, ipady=38)

        button3 = ttk.Button(self.frame_buttons, text ="Object Detection", command = lambda : controller.show_frame(FoldClothes), width=23, style="clothes.TButton" )
        button3.grid(row = 0, column = 2,ipady=38)
        # End of bottom tab buttons
        
    def tkraise(self):
        self.frame_buttons.grid()
        self.frame_buttons.tkraise()
        tk.Frame.tkraise(self)
        
    
#####################
# Joke Screen
#####################
class Joke(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#3a4466")
        

        # Styles for joke button
        style = ttk.Style()
        style.map("joke.TButton",
          background = [("active", "#F60081"), ("!active", "white")],
          foreground = [("active", "white"), ("!active", "#F60081")], )
        style.configure("joke.TButton", font=ARCADEFONT)
        # Styles for joke button
       
       # Beginning of buttons, Tell me a joke
        jokeButton = ttk.Button(self, text= "Tell me a Joke",padding=15,command= lambda: [self.jokeMode()], style='joke.TButton')
        jokeButton.place(x=275, y=50)



        #Creating a frame exclusively for the buttons
        self.frame_buttons = tk.Frame(parent)
        self.frame_buttons.grid(row = 1, column = 0, columnspan = 3)
        self.frame_buttons.grid_remove()
        
        #Gridding self.frame_buttons
        self.frame_buttons.grid_columnconfigure((0,1), weight = 1)
        self.frame_buttons.grid_rowconfigure(0, weight = 1)
        
        # Styles for buttons
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Joke.TButton", foreground="#F60081", background="white",  font=ARCADEFONT, )
        # End of Styles for buttons

        button1 = ttk.Button(self.frame_buttons ,text ="Let's Fold some Clothes" ,command = lambda : controller.show_frame(FoldClothes),width=23 ,style="Joke.TButton",  )
        button1.grid(row = 0, column = 0, ipady=38 )

        button2 = ttk.Button(self.frame_buttons, text ="Home", command = lambda : controller.show_frame(Home), width=23, style="Joke.TButton" ) 
        button2.grid(row = 0, column = 1, ipady=38)

        button3 = ttk.Button(self.frame_buttons, text ="Object Detection", command = lambda : controller.show_frame(FoldClothes), width=23, style="Joke.TButton" )
        button3.grid(row = 0, column = 2,ipady=38)

        
    def tkraise(self):
        self.frame_buttons.grid()
        self.frame_buttons.tkraise()
        tk.Frame.tkraise(self)

    def jokeMode(self):
        text = aJokeFunction()
        jokeTextBox = ttk.Label(self, background="#272933", foreground="white")
        jokeTextBox.grid(row=3, column=4)
        jokeTextBox.configure(text=text)
    
        
# Driver Code
app = tkinterApp()
app.title("The Pi that Folds your Clothes")
app.geometry("800x425")
app.mainloop()