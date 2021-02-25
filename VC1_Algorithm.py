from tkinter import *
import random
# Create an empty window
windows = Tk()
# Set TK window size w & h
windows.geometry("800x800")

windows.title("WELCOMENEW GAME")
# CONSTANT
COLORS_OF_CANDIES = ["#18ffff", "#b388ff", "#90caf9", "#00695c"] #color of candy

# GLOBALVARIABLES


# WINDOWS

wid =  800
hei = 600
posX = int(wid/2)
posY = int(hei/2)
my_canvas = Canvas(windows, width = wid, height = hei , bg="#37474f")
my_canvas.pack(pady=20)
my_circle = my_canvas.create_rectangle(posX,posY,posX+50,posY+50 ,fill=random.choice(COLORS_OF_CANDIES))


def moveLeft(event):
    posX = -10
    posY  = 0
    my_canvas.move(my_circle,posX,posY)


def moveRight(event):
    
    posX = 10
    posY  = 0
    my_canvas.move(my_circle,posX,posY)

def moveUp(event):
    posX = 0
    posY  = -10
    my_canvas.move(my_circle,posX,posY)


def moveDown(event):
    posX = 0
    posY  = 10
    my_canvas.move(my_circle,posX,posY)




windows.bind("<Left>", moveLeft)
windows.bind("<Right>", moveRight)
windows.bind("<Up>", moveUp)
windows.bind("<Down>", moveDown)
# Display all
windows.mainloop()