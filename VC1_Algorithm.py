import tkinter as tk
import random
windows = tk.Tk()
windows.title('Game Snake')
# 
# Row Is the number of cells in the high direction
# Column Is the number of cells in the rectangle up
# Unit_size Is the side length of a single unit
# Height Is the overall height
# Width Is the overall length
#
global Row, Column
Row = 25
Column = 25
size = 25
Height = Row * size
Width = Column * size
global Direction
Direction = 2
global FPS
FPS = 150    # Frame per second
global HaveCandy
HaveCandy = 0
global candyCoord
candyCoord = [0, 0]
global Score
Score = 0
global snakeList
snakeList = [[11,10],
             [10,10],
             [9,10]]
global game_map
game_map = []
# bg=tk.PhotoImage(file="background.png") #image bg
     # Direction is the global variable of forward direction - 1, 1, - 2, 2 for Up,Down
def draw_a_unit(canvas, col, row, snake_color = "SlateBlue") :
     # Draw a (c, r) square with the upper left corner as the reference
    x0 = col * size
    y0 = row * size
    x1 = (col + 1) * size
    y1 = (row + 1) * size

    # canvas.create_image(25,25,image=bg)# image background      /
    # Draw with components in canvas object, a rectangle formed by diagonal(ongkot trong) lines from (x0, y0) to (x1, y1)


    canvas.create_rectangle(x0, y0, x1, y1, fill = snake_color, outline = "white")

def put_a_background(canvas, color = "grey") :
            # Building  grid on canvas
    for x in range(Column) :
        for y in range(Row) :
            draw_a_unit(canvas, x, y, snake_color = color)
            game_map.append([x, y])
    print(game_map)


def draw_the_snake (canvas, snakeList, color = "green") :
    
                        # description: Snake function(REAB RAB)
                        # (type) snake_list Integer list, default element is list(x, y)
                        # return: None
                        # 
    
    for index in snakeList :
        draw_a_unit(canvas, index[0], index[1], snake_color = color)
def snake_move(snakeList, dire) :
                                    #Change of direction through external event binding of event
                                    #Or the default direction calls the implementation
                                    #return a new Snake list
    global Row, Column
    global HaveCandy
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
        #Carry out a mold taking treatment to form the effect of crossing the boundary
    for coord in snakeList :
        if coord[0] not in range(Column) :
            coord[0] =  coord[0]%Column
            
            break
        elif coord[1] not in range(Row) :
             coord[1] = coord[1]% Row
            
             break
    if snakeList[0] == candyCoord:
        draw_a_unit(canvas, snakeList[0][0], snakeList[0][1], )
        HaveCandy = 0
        Score += 1
        str_score.set("Your Score:" + str(Score))
    else :
                   
                   #Order is also very important, otherwise there will be mistake s in the snake's head

        draw_a_unit(canvas, snakeList[-1][0], snakeList[-1][1], snake_color = "grey") # put color same board
        draw_a_unit(canvas, snakeList[0][0], snakeList[0][1], )
        snakeList.pop()
    return snakeList
         # that the snake head cannot move in the direction of the original snake. Event is the (chong) keyboard event

def callback (event) :
         #limit whether it can operate up and down ,right,left
    global Direction
    char = event.keysym
    if  char == "Up":
        if snakeList[0][0] != snakeList[1][0] :
            Direction = -1
    elif char == "Down" :
        if snakeList[0][0] != snakeList[1][0] :
            Direction = 1
    elif char == "Left" :
        if snakeList[0][1] != snakeList[1][1] :
            Direction = -2
    elif char == "Right" :
        if snakeList[0][1] != snakeList[1][1] :
            Direction = 2
    return None #no something display
        # whether the snake hit itself in the current state

def snake_death (snakeList) :
        #return 0 means no death
        #return 1 for death
        #Methods of list duplicate(pton) checking
    setList = snakeList[1:]
    if snakeList[0] in setList:
        return 1
    else :
        return 0


def food(canvas, snakeList) :
         #Randomly generated position (x1, y1)
    global Column, Row, HaveCandy, candyCoord
    global game_map
    if HaveCandy:
        return
    candyCoord[0] = random.choice(range(Column))
    candyCoord[1] = random.choice(range(Row))
    while candyCoord in snakeList :
        candyCoord[0] = random.choice(range(Column))
        candyCoord[1] = random.choice(range(Row))
    draw_a_unit(canvas, candyCoord[0], candyCoord[1], snake_color = "orange")
    HaveCandy = 1


def game_loop() :
    global FPS
    global snakeList
    windows.update()
    food(canvas, snakeList)
    snakeList = snake_move(snakeList,Direction)
    flag = snake_death(snakeList)
    if flag :
        over_lavel = tk.Label(windows, text = 'Game Over', font = ('Regular script', 25), width = 15, height = 1)
        over_lavel.place(x = 40, y = Height / 2)
        return 
    windows.after(FPS, game_loop) #LOOP GAME SPEED 150
    

canvas = tk.Canvas(windows, width = Width, height = Height + 2 * size)
canvas.pack()

str_score = tk.StringVar()
score_label = tk.Label(windows, textvariable = str_score, font = ('Regular script', 20), width = 15, height = 1)
str_score.set('Your Score:' + str(Score))
score_label.place(x = 50, y = Height)
put_a_background(canvas)
draw_the_snake(canvas, snakeList)

canvas.focus_set()
canvas.bind("<KeyPress-Left>",  callback)
canvas.bind("<KeyPress-Right>", callback)
canvas.bind("<KeyPress-Up>",    callback)
canvas.bind("<KeyPress-Down>",  callback)
game_loop()
windows.mainloop()