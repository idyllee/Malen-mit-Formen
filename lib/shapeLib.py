from turtle import *
import math
import random

"""
    Diese Funktion bewegt den Stift zu der Position (x, y)

    Parameter:
    x (int, float): X Kordination
    y (int, float): Y Kordination
"""
def teleport(x, y):
    penup()
    goto(x, y)
    pendown()


"""
    Diese Funktion malt ein Rechteck

    Parameter:
    x (int, float): X Kordination
    y (int, float): Y Kordination
    width(int, float): die Breite des Rechtecks
    height(int, float): die Höhe des Rechtecks
    pcolor(string): die Farbe des Stiftes
    fcolor(string): die Farbe zum Befüllen des Rechtecks
"""
def rectangle(x, y, width, height, pcolor, fcolor):
    penup()
    goto(x, y)
    pendown()
    pencolor(pcolor)
    begin_fill()
    fillcolor(fcolor)
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    left(90)
    end_fill()


"""
    Diese Funktion malt einen Kreis

    Parameter:
    x (int, float): X Kordination vom untersten Punkt des Kreises
    y (int, float): Y Kordination vom untersten Punkt des Kreises
    radius(int, float): der Radius des Kreises
    pcolor(string): die Farbe des Stiftes
    fcolor(string): die Farbe zum Befüllen des Kreises
"""
def myCircle(x, y, radius, myPencolor, myFillcolor):

    penup()
    goto(x, y)
    pendown()
    pencolor(myPencolor)
    begin_fill()
    fillcolor(myFillcolor)
    circle(radius, 360)
    end_fill()


"""
    Diese Funktion malt ein gleichseitiges Dreieck

    Parameter:
    x (int, float): X Kordination von der Mitte der untersten Seite des Dreiecks
    y (int, float): Y Kordination von der Mitte der untersten Seite des Dreiecks
    size(int, float): die Länge der Seite
    pcolor(string): die Farbe des Stiftes
    fcolor(string): die Farbe zum Befüllen des Dreiecks
"""
def myEquilateralTriangle(x, y, size, pcolor, fcolor):
    penup()
    goto(x, y)
    pendown()
    pencolor(pcolor)
    begin_fill()
    fillcolor(fcolor)
    forward(size/2)
    left(120)
    forward(size)
    left(120)
    forward(size)
    left(120)
    forward(size/2)
    end_fill()
    setheading(0)


"""
    Diese Funktion malt ein gleichschenkliges Dreieck, dessen Rechtwinkel links liegt

    Parameter:
    x (int, float): X Kordination von der linken Ecke
    y (int, float): Y Kordination von der linken Ecke
    base(int, float): die Länge der untersten Seite, auch als Basis genannt
    angle(int, float): die Größe der zwei gleichgroßen Winkel
    pcolor(string): die Farbe des Stiftes
    fcolor(string): die Farbe zum Befüllen des Dreiecks
"""
def myIsoscelesTriangle(x, y, base, angle, pcolor, fcolor):
    penup()
    goto(x, y)
    pendown()
    pencolor(pcolor)
    begin_fill()
    fillcolor(fcolor)
    """
    forward(base)
    left(180-angle)
    xpos = xcor()
    while int(xpos) >= x+base/2:
        xpos = xcor()
        forward(1)
    goto(x, y)
    """
    forward(base)
    left(180-angle)
    forward(base / (2 * math.cos(math.radians(angle))))
    goto(x,y)
    end_fill()
    setheading(0)


"""
    Diese Funktion malt ein rechtwinkliges Dreieck, dessen Rechtwinkel links liegt

    Parameter:
    x (int, float): X Kordination von der linken Ecke
    y (int, float): Y Kordination von der linken Ecke
    length1(int, float): die Länge der Seite, die nach rechts zeigt vom Rechtwinkel
    length2(int, float): die Länge der Seite, die nach oben zeigt vom Rechtwinkel
    pcolor(string): die Farbe des Stiftes
    fcolor(string): die Farbe zum Befüllen des Dreiecks
"""
def myRightAngeldTriangle_Left(x, y, length1, length2, pcolor, fcolor):
    penup()
    goto(x, y)
    pendown()
    pencolor(pcolor)
    begin_fill()
    fillcolor(fcolor)
    forward(length1)
    goto(x, y+length2)
    goto(x, y)
    end_fill()
    setheading(0)


"""
    Diese Funktion malt ein rechtwinkliges Dreieck, dessen Rechtwinkel rechts liegt

    Parameter:
    x (int, float): X Kordination von der linken Ecke
    y (int, float): Y Kordination von der linken Ecke
    length1(int, float): die Länge der Seite, die nach links zeigt vom Rechtwinkel
    length2(int, float): die Länge der Seite, die nach oben zeigt vom Rechtwinkel
    pcolor(string): die Farbe des Stiftes
    fcolor(string): die Farbe zum Befüllen des Dreiecks
"""
def myRightAngeldTriangle_Right(x, y, length1, length2, pcolor, fcolor):
    penup()
    goto(x, y)
    pendown()
    pencolor(pcolor)
    begin_fill()
    fillcolor(fcolor)
    forward(length1)
    left(90)
    forward(length2)
    goto(x, y)
    end_fill()
    setheading(0)


"""
    Diese Funktion malt ein Ballt, das nach rechts streckt

    Parameter:
    x (int, float): X Kordination vom Stiel des Blattes
    y (int, float): Y Kordination vom Stiel des Blattes
    angle(int, float): der Startwinkel des Blattes
    length(int, float): die Blattlänge
    pcolor(string): die Farbe des Stiftes
    fcolor(string): die Farbe zum Befüllen des Blattes
"""
def myLeaf_Right(x, y, angle, length, pcolor, fcolor):

    teleport(x, y)
    left(angle)
    penup()
    forward(length)
    vertexX = xcor()
    teleport(x,y)

    pencolor(pcolor)

    begin_fill()
    fillcolor(fcolor)
    setheading(angle+30)
    xpos = x
    size = math.pi * length * 2 / 360

    while int(xpos) <= vertexX+1:
        print("Heading: " + str(heading()))
        xpos = xcor()
        right(1)
        forward(size)

    setheading(180+angle+30)
    while int(xpos) >= x:
        xpos = xcor()
        right(1)
        forward(size)
    end_fill()
    setheading(0)


"""
    Diese Funktion malt ein Ballt, das nach links streckt

    Parameter:
    x (int, float): X Kordination vom Stiel des Blattes
    y (int, float): Y Kordination vom Stiel des Blattes
    angle(int, float): der Startwinkel des Blattes
    length(int, float): die Blattlänge
    pcolor(string): die Farbe des Stiftes
    fcolor(string): die Farbe zum Befüllen des Blattes
"""
def myLeaf_Left(x, y, angle, length, pcolor, fcolor):

    teleport(x, y)
    left(180-angle)
    forward(length)
    if (angle == 90 or angle == 270):
        vertexX = x
    else:
        vertexX = xcor()
    teleport(x,y)

    pencolor(pcolor)
    begin_fill()
    fillcolor(fcolor)
    setheading(180-angle+30)
    xpos = x
    size = math.pi * length * 2 / 360
    print("xpos " + str(xpos))
    print("vertexX " + str(vertexX))
    while int(xpos) >= vertexX:
        print("xpos " + str(xpos))
        print("vertexX " + str(vertexX))
        xpos = xcor()
        right(1)
        forward(size)

    #setheading(180-angle+30-180)
    setheading(360-angle+30)
    while int(xpos) <= x-1:
        xpos = xcor()
        right(1)
        forward(size)
    setheading(0)
    end_fill()

def halberKreis(x, y, radius, pcolor, fcolor):
    teleport(x, y)
    pencolor(pcolor)
    begin_fill()
    fillcolor(fcolor)
    forward(2*radius)
    setheading(90)
    circle(radius, 180)
    setheading(0)
    end_fill()

def viertelKreis(x, y, radius, pcolor, fcolor):
    teleport(x, y)
    pencolor(pcolor)
    begin_fill()
    fillcolor(fcolor)
    circle(radius, 90)
    left(90)
    forward(radius)
    left(90)
    forward(radius)
    setheading(0)
    end_fill()

def trapezoid(x, y, upSize, downSize, height, pcolor, fcolor):
    teleport(x, y)
    pencolor(pcolor)
    begin_fill()
    fillcolor(fcolor)
    forward(downSize)
    goto(x+downSize/2+upSize/2, y+height)
    goto(x+downSize/2-upSize/2, y+height)
    goto(x, y)
    setheading(0)
    end_fill()


#def draw_half_oval(start_x, start_y, width, height, aspect_ratio, orientation, pcolor, fcolor):
    """
    Zeichnet ein halbes Oval mit der Turtle-Grafikbibliothek an einer bestimmten Position.

    :param width: Breite des Ovals
    :param height: Höhe des Ovals
    :param aspect_ratio: Verhältnis zwischen Breite und Höhe (größer -> schmaler)
    :param orientation: 'up' für obere Hälfte, 'down' für untere Hälfte
    :param start_x: X-Koordinate der Startposition
    :param start_y: Y-Koordinate der Startposition
    """
"""    penup()
    goto(start_x - width / 2, start_y if orientation == "up" else start_y - height)
    pendown()

    pencolor(pcolor)
    begin_fill()
    fillcolor(fcolor)
    # Das halbe Oval wird durch kleine Liniensegmente genähert
    steps = 50
    for i in range(steps + 1):
        angle = math.pi * (i / steps)  # Werte zwischen 0 und Pi für eine Halbellipse
        x = (width / 2) * math.cos(angle) + start_x
        y = (height / (2 * aspect_ratio)) * math.sin(angle) + start_y
        if orientation == "down":
            y = start_y - (height / (2 * aspect_ratio)) * math.sin(angle)  # Spiegelt das halbe Oval nach unten
        goto(x, y)
    end_fill()

 """
