import pgzrun

WIDTH =  100
HEIGHT = 100

b1 = Actor('00.jpg'); b1.x = 150
b2 = Actor('01.jpg'); b2.x = 250
_ = 2
__ = 0

def b1_change():
    global b1, _, __
    b1 = Actor(f'{__}{_}.jpg')
    b1.x = 150
    if _ == 9:
        __ += 1
        _ = 0
    else:
        _ += 1
def b2_change():
    global b2, _, __
    b2 = Actor(f'{__}{_}.jpg')
    b2.x = 150
    if _ == 9:
        __ += 1
        _ = 0
    else:
        _ += 1

def draw():
    screen.clear()
    b1.draw()
    b2.draw()

def update():
    if b1.x > -50:
        b1.x -= 1
    if b2.x > -50:
        b2.x -= 1
    if b1.x == -49:
        b1_change()
    if b2.x == -49:
        b2_change()


pgzrun.go()