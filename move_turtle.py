from turtle import *
import random
import time

border = 360
screen_width, screen_height = 400, 400
screen = Screen()
#screen.setup(screen_width, screen_height)

# Border Creation
t0 = Turtle()
t0.speed(0)
t0.pensize(5)
t0.penup()
t0.goto(-screen_width / 2, -screen_height / 2)
t0.pendown()
t0.hideturtle()
for i in range(4):
  t0.forward(screen_width)
  t0.left(90)

# Turtle 1 Creation 
t1 = Turtle()
t1.shape('turtle')
t1.speed(10)
t1.color('red')
t1.penup();

# Orientation of the turtle (standard mode)
# 0   - East
# 90  - North
# 180 - West
# 270 - South

def red_up():
  t1.setheading(90)
  if t1.ycor() <= border/2:
    t1.fd(5)

def red_down():
  t1.setheading(270)
  if t1.ycor() >= -border/2:
    t1.fd(5)

def red_left():
  t1.setheading(180)
  if t1.xcor() >= -border/2:
    t1.fd(5)

def red_right():
  t1.setheading(0)
  if t1.xcor() <= border/2:
    t1.fd(5)

screen.onkeypress(red_up, 'Up')
screen.onkeypress(red_down, 'Down')
screen.onkeypress(red_left, 'Left')
screen.onkeypress(red_right, 'Right')

# Turtle 2 Creation 
t2 = Turtle()
t2.shape('turtle')
t2.speed(10)
t2.color('blue')
t2.penup();
t2.goto(0, -20)
#screen.onclick(t2.goto)

def blue_up():
  t2.setheading(90)
  if t2.ycor() <= border/2:
    t2.fd(5)

def blue_down():
  t2.setheading(270)
  if t2.ycor() >= -border/2:
    t2.fd(5)

def blue_left():
  t2.setheading(180)
  if t2.xcor() >= -border/2:
    t2.fd(5)

def blue_right():
  t2.setheading(0)
  if t2.xcor() <= border/2:
    t2.fd(5)

# define the callback
def gotopoint(x, y):
  t2.goto(x,y)

screen.onkeypress(blue_up, 'w')
screen.onkeypress(blue_down, 's')
screen.onkeypress(blue_left, 'a')
screen.onkeypress(blue_right, 'd')
#screen.onclick(gotopoint)

food = Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.direction = "stop"
x = random.randint(-180, 180)
y = random.randint(-180, 180)
food.goto(x, y)

score1, score2 = 0, 0

pen = Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 180)
pen.write("Score1:" + str(score1) + " Score2:" + str(score2), align="center", font=("Courier", 14, "normal"))

Screen().listen()

quit = False

while not quit:
  screen.update()

  if t1.distance(food) < 20 or t2.distance(food) < 20:
  
    if t1.distance(food) < 20:
      score1 += 1
      print(F"score1:{score1}, score2:{score2}")
      pen.clear();
      pen.write("Score1:" + str(score1) + " Score2:" + str(score2), align="center", font=("Courier", 14, "normal"))
    
    if t2.distance(food) < 20:
      score2 += 1
      print(F"score1:{score1}, score2:{score2}")
      pen.clear();
      pen.write("Score1:" + str(score1) + " Score2:" + str(score2), align="center", font=("Courier", 14, "normal"))

    x = random.randint(-180, 180)
    y = random.randint(-180, 180)
    food.goto(x, y)

  if score1 >= 10 or score2 >= 10:
    quit = True

  time.sleep(0.1)


#Screen().mainloop()

