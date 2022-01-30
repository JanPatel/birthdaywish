import turtle
import random
#name = input('Enter your name')
# sets background
bg = turtle.Screen()
bg.bgcolor("black")



# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 100)
pen.write("HAPPY BIRTHDAY",  align= "center", font=("Courier", 40, "normal"))

#Line 1
turtle.penup()
turtle.goto(-170,-170)
turtle.color("magenta")
turtle.pendown()
turtle.forward(300)
turtle.speed(1.2)

#Line 2
turtle.penup()
turtle.goto(-160,-160)
turtle.color("white")
turtle.pendown()
turtle.forward(280)

#Line 3
turtle.penup()
turtle.goto(-150,-150)
turtle.color("cyan")
turtle.pendown()
turtle.forward(260)

#Line 4
turtle.penup()
turtle.goto(-140,-140)
turtle.color("brown")
turtle.pendown()
turtle.forward(240)

#Line 5 
turtle.penup()
turtle.goto(-130,-130)
turtle.color("red")
turtle.pendown()
turtle.forward(220)

#Line 6 
turtle.penup()
turtle.goto(-120,-120)
turtle.color("orange")
turtle.pendown()
turtle.forward(200)

#Line 7 
turtle.penup()
turtle.goto(-110,-110)
turtle.color("yellow")
turtle.pendown()
turtle.forward(180)

# Cake
turtle.penup()
turtle.goto(-95,-95)
turtle.color("pink")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Candles
turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-70,0)
turtle.color("pink")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-50,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-30,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-10,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(10,0)
turtle.color("orange")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30,0)
turtle.color("white")
turtle.pendown()
turtle.forward(20)

# Decoration
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)