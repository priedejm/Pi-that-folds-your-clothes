
from cgitb import text
from cmath import exp
from lib2to3.pygram import pattern_symbols
from re import X
from textwrap import fill
import tkinter as tk
from tkinter import LEFT, NW, Frame, Image, Label, PhotoImage, ttk, Button
#from PIL import ImageTk, Image
from tkinter import font
from tkinter.messagebox import YES
from turtle import bgcolor, color, width
from Greetings import *
import os



#from PIL import ImageTk, Image 
  
LARGEFONT =("Verdana", 20)
ARCADEFONT = ("ArcadeClassic", 16)
LARGEARCADEFONT = ("ArcadeClassic", 24)

jokeCount = 0
shirtCount = 0
pantsCount = 0
totalCount = 0
file = open("lifeCount.txt")
content = file.readlines()
lifeShirtCount = content[0]
lifePantsCount = content[1]
lifeTotalCount = content[2]

pathHome = "C:\\Users\justin\Desktop\pi\Pi-that-folds-your-clothes\laundryArcade.png"
pathFold = "C:\\Users\justin\Desktop\pi\Pi-that-folds-your-clothes\laundrySide.png"

#####################
# Helper Functions
#####################
def writeFile():
    global lifeShirtCount
    global lifePantsCount
    global lifeTotalCount
    f = open("lifeCount.txt", "w")
    f.write(str(lifeShirtCount))
    f.write("\n")
    f.write(str(lifePantsCount))
    f.write("\n")
    f.write(str(lifeTotalCount))
    f.close()

def enableObjDetection():
    os.system('python c:/Users/Justin/Desktop/object-detection/LabelImg/labelImg.py')
    print('Enabled Object Detection')

  
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
        for F in (Home, FoldClothes, Joke, ObjectDetection):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # Home, FoldClothes, Joke respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Home)
        print("LifeShirtCount: " + lifeShirtCount)
        print("LifePantsCount: " + lifePantsCount)
        print("LifeTotalCount: " + lifeTotalCount)

    
  
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

        button3 = ttk.Button(self.frame_buttons, text ="Object Detection", command = lambda : controller.show_frame(ObjectDetection), width=23, style="home.TButton" )
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
        shirtButton = ttk.Button(self, text= "Shirt Mode",padding=15,command= lambda: [self.shirtStats(), self.totalStat(), writeFile()], style='shirtPants.TButton')
        shirtButton.place(x=140, y=75)
        pantsButton = ttk.Button(self, text= "Pants Mode",padding=15,command= lambda: [self.pantsStats(), self.totalStat(), writeFile()], style='shirtPants.TButton')
        pantsButton.place(x=320, y=75)
        # End of buttons, shirt and pants

        # Beginning of Current Session on right side of display
        statshere = ttk.Label(self, text ="Current Session", font = LARGEARCADEFONT, background="#3a4466", foreground="white", )
        statshere.place(x=500, y=15)

        shirtsFolded = ttk.Label(self, text ="shirts folded:", font = ARCADEFONT, background="#3a4466", foreground="white")
        shirtsFolded.place(x=500, y=55)
        shirtZero = ttk.Label(self, text ="0", font = LARGEARCADEFONT, background="#3a4466", foreground="white")
        shirtZero.place(x=675, y=50)

        pantsFolded = ttk.Label(self, text ="pants folded:", font = ARCADEFONT, background="#3a4466", foreground="white")
        pantsFolded.place(x=500, y=90)
        pantsZero = ttk.Label(self, text ="0", font = LARGEARCADEFONT, background="#3a4466", foreground="white")
        pantsZero.place(x=675, y=85)

        totalFolded = ttk.Label(self, text ="Total Folded:", font = ARCADEFONT, background="#3a4466", foreground="white")
        totalFolded.place(x=500, y=125) 
        totalZero = ttk.Label(self, text ="0", font = LARGEARCADEFONT, background="#3a4466", foreground="white")
        totalZero.place(x=675, y=120)
        # End of Current Session on right side of display

        allTime = ttk.Label(self, text ="All time:", font = LARGEARCADEFONT, background="#3a4466", foreground="white", )
        allTime.place(x=500, y=150)
        
        allTimeShirts = ttk.Label(self, text ="Shirts Folded:", font = ARCADEFONT, background="#3a4466", foreground="white")
        allTimeShirts.place(x=500, y=190)
        allTimeShirtZero = ttk.Label(self, text ="0", font = LARGEARCADEFONT, background="#3a4466", foreground="white")
        allTimeShirtZero.place(x=675, y=185)

        allTimePants = ttk.Label(self, text ="Pants Folded:", font = ARCADEFONT, background="#3a4466", foreground="white")
        allTimePants.place(x=500, y=225)
        allTimePantsZero = ttk.Label(self, text ="0", font = LARGEARCADEFONT, background="#3a4466", foreground="white")
        allTimePantsZero.place(x=675, y=220)
        
        allTimeFolded = ttk.Label(self, text ="Total Folded:", font = ARCADEFONT, background="#3a4466", foreground="white")
        allTimeFolded.place(x=500, y=260)
        allTimeFoldedZero = ttk.Label(self, text ="0", font = LARGEARCADEFONT, background="#3a4466", foreground="white")
        allTimeFoldedZero.place(x=675, y=255)


        
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
    
    def shirtStats(self):
        global shirtCount
        global lifeShirtCount
        lifeShirtCount = int(lifeShirtCount) + 1
        shirtCount = shirtCount + 1
        text = shirtCount
        lifeText = lifeShirtCount
        shirtStatBox = ttk.Label(self,text=text ,background="#3a4466", foreground="white", font = LARGEARCADEFONT)
        shirtStatBox.place(x=675, y=50)
        lifeshirtStatBox = ttk.Label(self,text=lifeText ,background="#3a4466", foreground="white", font = LARGEARCADEFONT)
        lifeshirtStatBox.place(x=675, y=185)
    
    def pantsStats(self):
        global pantsCount
        global lifePantsCount
        lifePantsCount = int(lifePantsCount)+ 1
        pantsCount = pantsCount + 1
        text = pantsCount
        lifeText = lifePantsCount
        pantsStat = ttk.Label(self, text = text,background="#3a4466", foreground="white", font = LARGEARCADEFONT)
        pantsStat.place(x=675, y=85)
        lifesPantsStatBox = ttk.Label(self,text=lifeText ,background="#3a4466", foreground="white", font = LARGEARCADEFONT)
        lifesPantsStatBox.place(x=675, y=220)
    
    def totalStat(self):
        global totalCount
        global lifeTotalCount
        global lifePantsCount
        global lifeShirtCount
        totalCount = pantsCount + shirtCount
        lifeTotalCount = int(lifePantsCount) + int(lifeShirtCount)
        text = totalCount
        lifeText = lifeTotalCount
        totalCount = ttk.Label(self, text = text,background="#3a4466", foreground="white", font = LARGEARCADEFONT)
        totalCount.place(x=675, y=120)
        lifesTotalStatBox = ttk.Label(self,text=lifeText ,background="#3a4466", foreground="white", font = LARGEARCADEFONT)
        lifesTotalStatBox.place(x=675, y=255)
    
  
    


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
        style.configure("home.TButton", foreground="white", background="#3a4466", font=ARCADEFONT,)
        # End of Styles for buttons

        # Beginning of bottom tab buttons
        button1 = ttk.Button(self.frame_buttons ,text ="Let's Fold some Clothes" ,command = lambda : controller.show_frame(FoldClothes),width=23 ,style="home.TButton",   )
        button1.grid(row = 0, column = 0, ipady=38 )

        button2 = ttk.Button(self.frame_buttons, text ="Home", command = lambda : controller.show_frame(Joke), width=23, style="home.TButton" ) 
        button2.grid(row = 0, column = 1, ipady=38)

        button3 = ttk.Button(self.frame_buttons, text ="Obhect Detection", command = lambda : controller.show_frame(ObjectDetection), width=23, style="home.TButton" )
        button3.grid(row = 0, column = 2,ipady=38)
        # End of bottom tab buttons

        self.jokeTextBox = ttk.Label(self, background="#3a4466", foreground="white", font=("ArcadeClassic", 20), width=75 )
        self.jokeTextBox.place(x=75, y=150)

        
    def tkraise(self):
        self.frame_buttons.grid()
        self.frame_buttons.tkraise()
        tk.Frame.tkraise(self)

    def jokeMode(self):
        global jokeCount
        text = aJokeFunction()
        self.jokeTextBox.config(text=text,)

    
#####################
# Object Detection
#####################
#
# Enables / Disabvles Object Detection
#
class ObjectDetection(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Frame.configure(self, background="#3a4466",  )
        
          # Beginning of buttons, Tell me a joke
        jokeButton = ttk.Button(self, text= "Object Detection",padding=15,command= lambda: [enableObjDetection()], style='joke.TButton')
        jokeButton.place(x=275, y=50)

        
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

        button3 = ttk.Button(self.frame_buttons, text ="Home", command = lambda : controller.show_frame(Home), width=23, style="home.TButton" )
        button3.grid(row = 0, column = 2,ipady=38)
        # End of bottom tab buttons
        
    def tkraise(self):
        self.frame_buttons.grid()
        self.frame_buttons.tkraise()
        tk.Frame.tkraise(self)
    
        
# Driver Code
app = tkinterApp()
app.title("The Pi that Folds your Clothes")
app.geometry("800x425")
app.mainloop()