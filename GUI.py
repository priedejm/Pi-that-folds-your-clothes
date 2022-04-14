from cgitb import text
from re import X
from textwrap import fill
import tkinter as tk
from tkinter import Frame, Image, Label, PhotoImage, ttk, Button
#from PIL import ImageTk, Image
from tkinter import font
from turtle import bgcolor, color, width
from Greetings import *
from PIL import ImageTk, Image 
  
LARGEFONT =("Verdana", 35)

#####################
# Helper Functions
#####################
#
#
# Print shirt method 
#
def printShirt():
    print("Shirt mode")

#
# Print Pants method
#
def printPants():
    print("Pants mode")





path = "C:\\Users\priedejm\Desktop\pi\Pi-that-folds-your-clothes\Laundry.png"
  
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

     
class Home(tk.Frame):
    def printShirt():
        print("Shirt mode")
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Frame.configure(self, background="#272933",  )
        
        #Image
        image = Image.open(path)
        image = image.resize((600, 310))
        photo = ImageTk.PhotoImage(image)

        label = Label(self, image = photo)
        label.image = photo
        label.grid(row=1)
        

        
        
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

        style.configure("Other.TButton", foreground="#F60081", background="white", font=("Verdana", 15), )
        # End of Styles for buttons

        button1 = ttk.Button(self.frame_buttons ,text ="Let's Fold some Clothes" ,command = lambda : controller.show_frame(FoldClothes),width=20 ,style="Other.TButton",  )
        button1.grid(row = 0, column = 0, ipady=38 )

        button2 = ttk.Button(self.frame_buttons, text ="Tell me a joke", command = lambda : controller.show_frame(Joke), width=20, style="Other.TButton" ) 
        button2.grid(row = 0, column = 1, ipady=38)

        button3 = ttk.Button(self.frame_buttons, text ="Object Detection", command = lambda : controller.show_frame(FoldClothes), width=20, style="Other.TButton" )
        button3.grid(row = 0, column = 2,ipady=38)
        
    def tkraise(self):
        self.frame_buttons.grid()
        self.frame_buttons.tkraise()
        tk.Frame.tkraise(self)
    
    

# second window frame page1
class FoldClothes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Frame.configure(self, bg="#272933")


        # Beginning of statistics on right side of display
        statshere = ttk.Label(self, text ="Current Session", font = ("Verdana", 20), background="#272933", foreground="white", padding=20)
        statshere.grid(row = 3, column = 2, )

        shirtsFolded = ttk.Label(self, text ="shirts folded:", font = ("Verdana", 13), background="#272933", foreground="white")
        shirtsFolded.grid(row = 4, column = 2, )

        pantsFolded = ttk.Label(self, text ="pants folded:", font = ("Verdana", 13), background="#272933", foreground="white")
        pantsFolded.grid(row = 5, column = 2, )

        totalFolded = ttk.Label(self, text ="Total:", font = ("Verdana", 13), background="#272933", foreground="white")
        totalFolded.grid(row = 6, column = 2, )  
        # End of labels on left side of display 


        # Styles for shirt and pants mode buttons
        style = ttk.Style()
        style.map("shirtPants.TButton",
          background = [("active", "#F60081"), ("!active", "white")],
          foreground = [("active", "white"), ("!active", "#F60081")], )
        style.configure("shirtPants.TButton", font=("Verdana", 20))
        # Styles for shirt and pants mode buttons

        # Beginning of buttons, shirt and pants
        shirtButton = ttk.Button(self, text= "Shirt Mode",padding=20,command= lambda: [printShirt()], style='shirtPants.TButton')
        shirtButton.grid(row = 4, column = 1, )
        pantsButton = ttk.Button(self, text= "Pants Mode",padding=20,command= lambda: [printPants()], style='shirtPants.TButton')
        pantsButton.grid(row = 6, column = 1, )
        # End of buttons, shirt and pants
        shirtpaddingLabel = ttk.Label(self, text ="Fold a shirt", font = ("Verdana", 20), background="#272933", foreground="white")
        shirtpaddingLabel.grid(row = 4, column = 0)
        pantspaddingLabel = ttk.Label(self, text ="Fold a pair of pants", font = ("Verdana", 20), background="#272933", foreground="white", padding=10)
        pantspaddingLabel.grid(row = 6, column = 0)
        # End of labels on left side of display 
       

        
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

        style.configure("Other.TButton", foreground="#F60081", background="white", font=("Verdana", 15), )
        # End of Styles for buttons

        button1 = ttk.Button(self.frame_buttons ,text ="Home" ,command = lambda : controller.show_frame(Home),width=20 ,style="Other.TButton",  )
        button1.grid(row = 0, column = 0, ipady=38 )

        button2 = ttk.Button(self.frame_buttons, text ="Tell me a joke", command = lambda : controller.show_frame(Joke), width=20, style="Other.TButton" ) 
        button2.grid(row = 0, column = 1, ipady=38)

        button3 = ttk.Button(self.frame_buttons, text ="Object Detection", command = lambda : controller.show_frame(FoldClothes), width=20, style="Other.TButton" )
        button3.grid(row = 0, column = 2,ipady=38)
        
    def tkraise(self):
        self.frame_buttons.grid()
        self.frame_buttons.tkraise()
        tk.Frame.tkraise(self)
        
    
# third window frame Joke
class Joke(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#272933")
        
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

        style.configure("Other.TButton", foreground="#F60081", background="white", font=("Verdana", 15), )
        # End of Styles for buttons

        button1 = ttk.Button(self.frame_buttons ,text ="Let's Fold some Clothes" ,command = lambda : controller.show_frame(FoldClothes),width=20 ,style="Other.TButton",  )
        button1.grid(row = 0, column = 0, ipady=38 )

        button2 = ttk.Button(self.frame_buttons, text ="Home", command = lambda : controller.show_frame(Home), width=20, style="Other.TButton" ) 
        button2.grid(row = 0, column = 1, ipady=38)

        button3 = ttk.Button(self.frame_buttons, text ="Object Detection", command = lambda : controller.show_frame(FoldClothes), width=20, style="Other.TButton" )
        button3.grid(row = 0, column = 2,ipady=38)

         # Styles for shirt and pants mode buttons
        style = ttk.Style()
        style.map("shirtPants.TButton",
          background = [("active", "#F60081"), ("!active", "white")],
          foreground = [("active", "white"), ("!active", "#F60081")], )
        style.configure("shirtPants.TButton", font=("Verdana", 20))
        # Styles for shirt and pants mode buttons

        # Beginning of buttons, Tell me a joke
        jokeButton = ttk.Button(self, text= "Tell me a Joke",padding=20,command= lambda: [self.jokeMode()], style='shirtPants.TButton')
        jokeButton.grid(row = 2, column = 4, )
        jokePadding = ttk.Label(self, text="PaddingPaddingPaddingPadding", font=24)
        jokePadding.grid(row = 1, column = 2, )
        
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