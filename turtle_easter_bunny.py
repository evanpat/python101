from turtle import * 

myWindow = Screen()
myWindow.bgcolor("wheat")

myTurtle = Turtle()
myTurtle.speed("fastest")

def myRectangle(t, posx, posy, x, y, c):
  t.penup()
  t.color(c)
  t.setheading(0)
  t.goto(posx, posy)
  t.pendown()
  t.begin_fill()
  for i in range(2):
    t.forward(x)
    t.right(90)
    t.forward(y)
    t.right(90)
  t.end_fill()


def myCircle(t, posx, posy, r, c):
  t.penup()
  t.color(c)
  t.setheading(0)
  t.goto(posx, posy)
  t.pendown()
  t.begin_fill()
  t.circle(r)
  t.end_fill()

def myArc(t, posx, posy, r, angle, heading, c):
  t.penup()
  t.color(c)
  t.setheading(heading)
  t.goto(posx, posy)
  t.pendown()
  t.begin_fill()
  t.circle(r, angle)
  t.end_fill()

#left ear
myRectangle(myTurtle, -250, 50, 50, 100, "silver")
myCircle(myTurtle, -225, 25, 25, "silver")
myRectangle(myTurtle, -240, 50, 30, 90, "hot pink")
myCircle(myTurtle, -225, 35, 15, "hot pink")

#right ear
myRectangle(myTurtle, -180, 50, 50, 100, "silver")
myCircle(myTurtle, -155, 25, 25, "silver")
myRectangle(myTurtle, -170, 50, 30, 90, "hot pink")
myCircle(myTurtle, -155, 35, 15, "hot pink")

#head and body
myCircle(myTurtle, -190, -220, 100, "silver")
myCircle(myTurtle, -190, -500, 150, "silver")
myCircle(myTurtle, -190, -450, 100, "hot pink")

#eyes 
myCircle(myTurtle, -215, -110, 10, "navy")
myCircle(myTurtle, -165, -110, 10, "navy")

#mouth
myArc(myTurtle, -190, -150, 20, 150, -90, "hot pink")
myArc(myTurtle, -190, -150, -20, 150, -90, "hot pink")

#nose
myTurtle.penup()
myTurtle.goto(-200, -130)
myTurtle.color("hot pink")
myTurtle.pendown()
myTurtle.begin_fill()
myTurtle.goto(-180, -130)
myTurtle.goto(-190, -150)
myTurtle.goto(-200, -130)

#text
myTurtle.penup()
myTurtle.goto(100, 200)
myTurtle.color("navy")
myTurtle.pendown()
myTurtle.write("Happy", align="center", font=("Impact", 100, "bold"))
myTurtle.goto(100, 100)
myTurtle.pendown()
myTurtle.write("Easter!", align="center", font=("Impact", 110, "bold"))
myTurtle.hideturtle()

myWindow.mainloop()
