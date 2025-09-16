import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'cyan', 'brown']
NUM_OBSTACLES = 10  # number of obstacles
OBSTACLES = [
    (random.randint(-WIDTH//2 + 50, WIDTH//2 - 50), 
     random.randint(-HEIGHT//2 + 50, HEIGHT//2 - 50))
    for _ in range(NUM_OBSTACLES)
]

def get_number_of_racers ():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try Again!')
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2-10.')

def celebrate(racer):
    for _ in range(36):
        racer.right(10)

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()

            for ox, oy in OBSTACLES:
                if abs(x - ox) < 15 and abs(y - oy) < 15:  # check both x and y
                    distance = max(0, distance - 10)      # strong slowdown
                    if random.random() < 0.3:
                        distance = 0

            racer.forward(distance)

            if y>= HEIGHT // 2 - 10:
                celebrate(racer)
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacing, - HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def draw_obstacles():
    obs = turtle.Turtle()
    obs.hideturtle()
    obs.penup()
    obs.color('brown')
    for ox, oy in OBSTACLES:
        obs.setpos(ox, oy)
        obs.pendown()
        obs.forward(20)
        obs.penup()

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Race')

racers = get_number_of_racers()
init_turtle()
draw_obstacles()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(winner)