import tkinter as tk

root = tk.Tk()
# Set TK window size to width 600 px and height 200 px
root.geometry("600x600")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame()
canvas = tk.Canvas(frame)
# Set the title of the frame
frame.master.title("Hello PNC")
# constants
oval=canvas.create_rectangle(0,0,50,50,fill="red")
# movement in x direction
x=1
# movement in y direction
y=0
def moveSnake():
    canvas.move(oval,x,y)
    canvas.after(500,lambda:moveSnake())
def moveLeft(event):
    global x,y
    x=-10
    y=0
 
    

def moveRight(event):
    global x,y
    x=10
    y=0
    
   
def moveUp(event):
    global x,y
    x=0
    y=-10
    
  
def moveDown(event):
    global x,y
    x=0
    y=10
   
    
root.bind("<Left>",moveLeft)
root.bind("<Right>",moveRight)
root.bind("<Up>",moveUp)
root.bind("<Down>",moveDown)
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
moveSnake()
# Display all
root.mainloop()