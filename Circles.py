import pgzrun
import math

## App
TITLE = "CIRCLES"
X, Y = 500, 500
WIDTH = X
HEIGHT = Y

## Board
rows, cols = int(X/25), int(Y/25)
field_length = int(X/20)
board = [[Rect((row*field_length, col*field_length), (field_length, field_length))for col in range(cols)]for row in range(rows)]
grey = (50, 50, 50)
red = (200, 0, 0)

## Circles
circles = 9 # ADJUST !!

c = X/2
arc = math.pi / 2
angle_radius_arc = (arc/circles)/2 # alpha
angle_center_to_radius = (180-angle_radius_arc)/2 # beta
radius = (X/2 * math.sin(angle_radius_arc)) / (math.sin(angle_radius_arc) + math.sin(angle_center_to_radius))

if circles <= 1 or type(circles) == float:
    quit()

def get_pos_upper_R(a):
    beta = arc - a*(arc / circles)
    x = X/2 + math.cos(beta)*c - radius
    y = Y/2 - math.sin(beta)*c + radius
    pos = (x, y)    
    return pos

def get_pos_upper_L(a):
    beta = arc - a*(arc / circles)
    x = X/2 - math.cos(beta)*c + radius
    y = Y/2 - math.sin(beta)*c + radius
    pos = (x, y)    
    return pos
        
def get_pos_lower_R(a):
    beta = arc - a*(arc / circles)
    x = X/2 + math.cos(beta)*c - radius
    y = Y/2 + math.sin(beta)*c - radius
    pos = (x, y)    
    return pos

def get_pos_lower_L(a):
    beta = arc - a*(arc / circles)
    x = X/2 - math.cos(beta)*c + radius
    y = Y/2 + math.sin(beta)*c - radius
    pos = (x, y)    
    return pos

def draw():
    screen.clear()
    for row in range(rows):
        for col in range(cols):
            screen.draw.rect(board[row][col], grey)
            
    for a in range(1, circles):
        pos = get_pos_upper_R(a)
        screen.draw.circle(pos, radius, red)
    for a in range(1, circles):
        pos = get_pos_upper_L(a)
        screen.draw.circle(pos, radius, red)
    for a in range(1, circles):
        pos = get_pos_lower_R(a)
        screen.draw.circle(pos, radius, red)
    for a in range(1, circles):
        pos = get_pos_lower_L(a)
        screen.draw.circle(pos, radius, red)
    
def on_key_down(key):
    if key == keys.ESCAPE:
        quit()
    
pgzrun.go()