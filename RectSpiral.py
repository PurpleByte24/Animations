import pgzrun

TITLE = "TRY"
X = 500
Y = 500
HEIGHT = X
WIDTH = Y

length = 10# adjust for line length

x1 = X/2
y1 = Y/2
x2 = X/2
y2 = Y/2 - length 
x3 = X/2 + length
y3 = Y/2 - length
x4 = X/2 + length
y4 = Y/2 + length 
x5 = X/2 - length
y5 = Y/2 + length

lines = 20 # adjust for more lines

def on_key_down(key):
    if key == keys.ESCAPE:
        quit()
        
def draw():
    global x1, y1, x2, y2, x3, y3, x4, y4, x5, y5
    screen.clear()
    screen.fill((150, 150, 150))
    for line in range(lines):
        screen.draw.line((x1, y1), (x2, y2), "red")
        screen.draw.line((x2, y2), (x3, y3), "red")
        screen.draw.line((x3, y3), (x4, y4), "red")
        screen.draw.line((x4, y4), (x5, y5), "red")
        x1, y1 = x1-length, y1+length
        x2, y2 = x2-length, y2-length
        x3, y3 = x3+length, y3-length
        x4, y4 = x4+length, y4+length
        x5, y5 = x1-length, y1+length

pgzrun.go()