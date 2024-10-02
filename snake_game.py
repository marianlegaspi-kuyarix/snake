import tkinter 
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT =  TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#game window 
game_window = tkinter.Tk()
game_window.title("Snake")
game_window.resizable(False, False)

canvas = tkinter.Canvas(game_window, bg = "magenta", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
game_window.update()

#center the game window
window_width = game_window.winfo_width()
window_height = game_window.winfo_height()
screen_width = game_window.winfo_screenwidth()
screen_height = game_window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+h+x+y"t
game_window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#initialize the game
snake = Tile(5* TILE_SIZE, 5*TILE_SIZE) #single tile for the snake's head
snake_food =Tile(10* TILE_SIZE, 10*TILE_SIZE) 
snake_vel_x = 0
snake_vel_y = 0

def change_direction(e): #e = event
    #print(e)
    #print(e.keysym)
    global snake_vel_x, snake_vel_y

    if (e.keysym == "Up"):
        snake_vel_x = 0
        snake_vel_y = -1
    elif (e.keysym == "Down"):
        snake_vel_x = 0
        snake_vel_y = 1
    elif (e.keysym == "Left"):
        snake_vel_x = -1
        snake_vel_y = 0
    elif (e.keysym == "Right"):
        snake_vel_x = 1
        snake_vel_y = 0
            
def move():
    global snake

    snake.x += snake_vel_x * TILE_SIZE
    snake.y += snake_vel_y * TILE_SIZE

def draw():
    global snake
    move()

    #draw the snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "cyan")

    #draw the snake's food
    canvas.create_rectangle(snake_food.x, snake_food.y, snake_food.x + TILE_SIZE, snake_food.y + TILE_SIZE, fill = "yellow")

    game_window.after(100, draw) #100ms = 1/10 second, 10 frames/second

draw()    

game_window.bind("<KeyRelease>", change_direction)
game_window.mainloop()


