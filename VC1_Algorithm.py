import tkinter as tk
import random
windows = tk.Tk() 
windows.title('Game Snake') 
str_score = tk.StringVar() 
global Row, Column
Row = 25
Column = 25
size = 35
Height = Row * size
Width = Column * size
global direction
direction = 2
global haveCandy
haveCandy = 0
global candyCoord
#Carry out a mold taking  to form the effect of
candyCoord = [0,0] 
global Score
Score = 0
global snakeList
snakeList = [[1,1,1,1,1,1,],
             [1,1,1,1,1,1],
             [1,1,1,1,1,1],
             [1,1,1,1,1,1],
             [1,1,1,1,1,1]]
global game
game = []

     # direction is the global variable of forward direction - 1, 1, - 2, 2 for Up,Down
def drawSnake(canvas,col, row, snake_color = "#9e9e9e") :
     # draw a (c, r) square with the upper left corner as the reference
    x0 = col * size
    y0 = row * size
    x1 = (col + 1) * size
    y1 = (row + 1) * size


    canvas.create_rectangle(x0, y0, x1, y1, fill = snake_color, outline = "white")

def createBackground(canvas, color = "#fafafa") :
            # Building  grid on canvas
    for x in range(Column) :
        for y in range(Row) :
            drawSnake(canvas, x, y, snake_color = color)
            game.append([x, y])
    print(game)


def draw_the_snake (canvas, snakeList, color = "green") :
    
    for index in snakeList :
        drawSnake(canvas, index[0], index[1], snake_color = color)
def snake_move(snakeList, dire) :
                                
    global Row, Column
    global haveCandy
    global candyCoord
    global Score
    new_coord = [0, 0]
    
    if dire % 2 == 1:
        new_coord[0] = snakeList[0][0]
        new_coord[1] = snakeList[0][1] + dire
    else :
        new_coord[0] = snakeList[0][0] + (int(dire / 2))
        new_coord[1] = snakeList[0][1]
    snakeList.insert(0, new_coord)
        # crossing the boundary
    for coord in snakeList :
        if coord[0] not in range(Column) :
            coord[0] =  coord[0]%Column
            
            break
        elif coord[1] not in range(Row) :
             coord[1] = coord[1]% Row
            
             break
    print(coord)
    if snakeList[0] == candyCoord:
        drawSnake(canvas, snakeList[0][0],snakeList[0][1])
        haveCandy = 0
        Score += 1
        str_score.set("Your Score:" + str(Score))
       
    else:
                   
             #Order is also very important, otherwise there will be mistake s in the snake's head

        drawSnake(canvas, snakeList[-1][0], snakeList[-1][1], snake_color = "#fafafa") 
        drawSnake(canvas, snakeList[0][0], snakeList[0][1])
        snakeList.pop()
    return snakeList
         # that the snake head cannot move in the direction of the original snake. Event is the (chong) keyboard event

def callback (event) :
    global direction
    char = event.keysym
    if  char == "Up":
        if snakeList[0][0] != snakeList[1][0] :
            direction = -1
    elif char == "Down" :
        if snakeList[0][0] != snakeList[1][0] :
            direction = 1
    elif char == "Left" :
        if snakeList[0][1] != snakeList[1][1] :
            direction = -2
    elif char == "Right" :
        if snakeList[0][1] != snakeList[1][1] :
            direction = 2
    return None #no something display
        # whether the snake hit itself in the current state

def snake_death (snakeList) :
        
    setList = snakeList[1:]
    if snakeList[0] in setList:
        return 1
    else :
        return 0


def food(canvas, snakeList) :
         #Random generated position (x1, y1)
    global Column, Row, haveCandy, candyCoord
    global game
    if haveCandy:
        return None
    candyCoord[0] = random.choice(range(Column))
    candyCoord[1] = random.choice(range(Row))
    while candyCoord in snakeList :
        candyCoord[0] = random.choice(range(Column))
        candyCoord[1] = random.choice(range(Row))
    drawSnake(canvas, candyCoord[0], candyCoord[1], snake_color = "orange")
    haveCandy = 1


def game_loop():
  
    global snakeList
    windows.update()
    food(canvas, snakeList)
    snakeList = snake_move(snakeList,direction)
    flag = snake_death(snakeList)
    if flag:
        over_lavel = tk.Label(windows, text = 'Game Over', font = ('Regular script', 25))
        over_lavel.place(x = 40, y = Height / 2)
        return None
    windows.after(200, game_loop) #LOOP GAME SPEED 150
    

canvas = tk.Canvas(windows, width = Width, height = Height + 2 * size)
canvas.pack()

score_label = tk.Label(windows, textvariable = str_score, font = ('Regular script', 20))
str_score.set('Your Score:' + str(Score))
score_label.place(x = 50, y = Height)
createBackground(canvas)
draw_the_snake(canvas, snakeList)

canvas.focus_set()
canvas.bind("<Left>",  callback)
canvas.bind("<Right>", callback)
canvas.bind("<Up>",    callback)
canvas.bind("<Down>",  callback)
game_loop()
windows.mainloop()