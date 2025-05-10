import turtle

def draw_lamp_base():
    turtle.penup()
    turtle.goto(-30, -100)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.goto(30, -100)
    turtle.goto(40, -80)
    turtle.goto(-40, -80)
    turtle.goto(-30, -100)
    turtle.end_fill()

def draw_lamp_stand():
    turtle.penup()
    turtle.goto(0, -80)
    turtle.pendown()
    turtle.color("gray")
    turtle.width(6)
    turtle.goto(0, 50)

def draw_lamp_shade():
    turtle.penup()
    turtle.goto(-40, 50)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.goto(-30, 90)
    turtle.circle(40, 180)
    turtle.goto(40, 50)
    turtle.goto(-40, 50)
    turtle.end_fill()

def draw_lamp():
    screen = turtle.Screen()
    screen.bgcolor("white")
    turtle.speed(3)

    draw_lamp_base()
    draw_lamp_stand()
    draw_lamp_shade()

    turtle.hideturtle()
    turtle.done()

# Zeichne die Lampe
draw_lamp()
