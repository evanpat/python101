import turtle 
import time
import random

delay = 0.1
score = 0
high_score = 0
seg = []

w = turtle.Screen()
w.title("Snake Game")
w.bgcolor("black")
w.setup(width=700,height=700)
w.tracer(0) #Turns of screen update

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.home()
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.goto(0, 100)
food.shape("square")
food.color("red")
food.penup()
food.direction = "stop"

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write(F"Score:{score}  High Score:{high_score}", align="center", font= ("Courier", 24, "normal"))


def go_up():
    if head.direction !="down":
        head.direction = "up"

def go_down():
    if head.direction !="up":
        head.direction = "down"

def go_left():
    if head.direction !="right":
        head.direction = "left"

def go_right():
    if head.direction !="left":
        head.direction = "right"

def stop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

w.listen()
w.onkey(go_up, "Up")
w.onkey(go_down, "Down")
w.onkey(go_left, "Left")
w.onkey(go_right, "Right")
w.onkey(stop, "space")


while True:
    w.update()

    die = False
    print = False

    #snake eat food
    if head.distance(food) < 20:
        x = random.randint(-330, 330)
        y = random.randint(-330, 290)
        food.goto(x, y)
        score += 10
        print = True
        if score > high_score:
            high_score = score

        ns = turtle.Turtle()
        ns.speed(0)
        ns.shape("square")
        ns.color("yellow")
        ns.penup()
        seg.append(ns)

    #Move the end segments first in reverse order
    for i in range(len(seg) - 1, 0, -1):
        x = seg[i - 1].xcor()
        y = seg[i - 1].ycor()
        seg[i].goto(x, y)

    #Move segment 0 to where the head is 
    if len(seg) > 0:
        x = head.xcor()
        y = head.ycor()
        seg[0].goto(x, y)

    move()

    #snake die - self collision
    for s in seg:
        if s.distance(head) < 20:
            die = True

    #snake die - wall collision
    if head.xcor() > 340 or head.xcor() < -340 or head.ycor() > 310 or head.ycor() < -340:
        die = True

    if die:
        head.home()
        head.direction = "stop"
        score = 0
        print = True
        for s in seg:
            s.goto(1000, 1000)
        seg.clear()


    #print score finally
    if print:
        pen.clear()
        pen.write(F"Score:{score}  High Score:{high_score}", align="center", font= ("Courier", 24, "normal"))

    time.sleep(delay)

w.mainloop()