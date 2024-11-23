import pgzrun

TITLE = "GRAFICS"
WIDTH = 600
HEIGHT = 600

rows = 20
cols = 20
field_length = 30
board = [[Rect((row*field_length, col*field_length), (field_length, field_length)) for col in range(cols)] for row in range(rows)]

## Colors
grey = (50, 50, 50)
red = (255, 0, 0)
orange = (255, 128, 0)
yellow =(255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (75, 0, 130)
pink = (128, 0, 128)
colors = [red, orange, yellow, green, blue, purple, pink]
iter_colors = iter(colors)

check = 0
first = True
backwards = False

## Code
def rotate_colors():
    global colors, check, backwards
    if not backwards:
        first_color = colors.pop(0)
        colors.append(first_color)
        check += 1
        if check == 20:
            backwards = True
            check = 0
    else:
        last_color = colors.pop()
        colors.insert(0, last_color)
        check += 1
        if check == 20:
            backwards = False
            check = 0
    clock.schedule(rotate_colors, 0.1)
    
def on_key_down(key):
    if key == keys.ESCAPE:
        quit()
        
def draw():
    global iter_colors, first
    screen.clear()
    screen.fill("black")
    for row in range(rows):
        try:
            color = next(iter_colors)
        except StopIteration:
            iter_colors = iter(colors)
        for col in range(cols):        
            screen.draw.rect(board[row][col], color)
    if first:
        rotate_colors()
        first = False 

pgzrun.go()