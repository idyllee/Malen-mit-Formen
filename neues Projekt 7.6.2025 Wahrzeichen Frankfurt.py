
import math
import random
from shapeLib import *
from turtle import *
from decimal import Decimal
shape("turtle")


speed(0)
#Kopf
fillcolor("black")
begin_fill()
penup()
goto(-7, 130)
pendown()
circle(43)

end_fill()



begin_fill()
pensize(6)
forward(30)
right(157)
forward(45)
right(80)
forward(63)
right(54)
forward(20)
right(124)
forward(68)
end_fill()

setheading(0)
penup()
goto(20, 132)
begin_fill()
circle(19)
end_fill()
penup()
goto(37, 137)
pendown()
setheading(93)
forward(30)
penup()
goto(37, 137)
pendown()
setheading(205)
forward(5)
left(145)

#Nacken

fillcolor("black")
begin_fill()
for i in range(3):
    forward(13)
    right(19)

#anfang rücken
right(26)
forward(86)
left(12)
forward(90)
right(27)


#(bein)
faktor = 1.5
faktor2 = 1.2
faktor3 = 1.7

for i in range(43):
    forward(3*faktor)
    left(1)

setheading(180)
forward(40*faktor2)

#Beine

right(63)

for i in range(31):
    forward(3*faktor3)
    right(1)
right(190)

for i in range(17):
    forward(3*faktor3)
    right(1)

left(14)

for i in range(16):
    forward(3*faktor)
    left(1)

setheading(0)
right(180)
forward(40*faktor2)
right(87)

for i in range(34):
    forward(3*faktor)
    right(1)

for i in range(8):
    forward(12)
    left(6)

for i in range(45):
    forward(1)
    left(2)
#ARM
pensize(10)
forward(50)





pensize(7)
forward(45)
right(180)
forward(10)
left(90)
forward(2)
right(90)
forward(7)
left(90)
forward(3)
right(90)
forward(28)
left(15)
forward(20)
left(69)
forward(10)
right(90)
forward(3)
left(90)
forward(50)
left(90)
forward(20)
right(35)
forward(5)
setheading(90)
forward(4)
right(40)
forward(5)
right(37)
forward(17)
left(85)
forward(5)
right(50)
forward(3)
right(60)
forward(3)
setheading(284)
forward(5)
left(90)
forward(10)
right(90)
forward(10)
right(90)
forward(5)
left(90)
forward(50)
left(80)
forward(6)
"""
left(47)
forward(103)
right(28)
forward(60)
end_fill()
"""
for x in range(18):
    forward(7)
    left(5)

right(64)
forward(52)
left(135)
forward(20)





hideturtle()


end_fill()

"""
def kopf(color1,x1, y1, radius1, psize, ):
"""
"""
for i in range(43):
    forward(3)
    left(1)

setheading(180)
forward(40)

#Beine

right(63)

for i in range(31):
    forward(3)
    right(1)
right(190)

for i in range(15):
    forward(3)
    right(1)

left(14)

for i in range(16):
    forward(3)
    left(1)

setheading(0)
right(180)
forward(40)
right(90)

for i in range(32):
    forward(3)
    right(1)
"""
"""
for i in range(8):
    forward(12)
    left(6)

for i in range(27):
    forward(1)
    left(2)
#ARM

"""

