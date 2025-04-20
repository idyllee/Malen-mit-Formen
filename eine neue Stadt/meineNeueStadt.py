# meine neue Stadt

import sys
import os


# Absoluten Pfad zum lib-Ordner ermitteln
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))

# Den lib-Ordner zum Suchpfad hinzufügen
sys.path.append(lib_path)

# Nun kannst du die Datei aus dem lib-Ordner importieren
from shapeLib import *
from turtle import *
import math

bgcolor("mistyrose")
setup(1200, 1000)


# size ist die Länge der untere Kante von dem Berg
def mountain(x, y, size):
    myEquilateralTriangle(x, y, size, "mediumblue", "mediumblue")

def bird(x, y, size, color):
    pencolor(color)
    if (size < 50 ):
        pensize(size/3)
    else:
        pensize(10)
    teleport(x, y)
    left(180)
    forward(size)
    teleport(x, y)
    right(180)
    forward(size)
    teleport(x, y)
    setheading(0)
    left(90)
    circle(-size, 90)
    teleport(x, y)
    setheading(0)
    left(90)
    circle(size, 90)
    setheading(0)

def baum(x, y, size):
    rectangle(x-size*10, y-size*50, size*20, size*50, "DarkGoldenrod4", "DarkGoldenrod4")
    viertelKreis(x, y, size*60, "PaleGreen4", "PaleGreen4")
    myRightAngeldTriangle_Left(x, y+size*60, size*60, size*200, "PaleGreen3", "PaleGreen3")
    setheading(270)
    viertelKreis(x-size*60, y+size*60, size*60, "PaleGreen3", "PaleGreen3")
    myRightAngeldTriangle_Right(x-size*60, y+size*60, size*60, size*200, "PaleGreen4", "PaleGreen4")



# Straßen #
rectangle(-600, -500, 1200, 200, "BurlyWood", "BurlyWood")
rectangle(-600, -300, 1200, 300, "wheat", "wheat")

#Berg#
mountain(0, -100, 600)

#Vögel#
angle_radians = math.radians(15)  # Winkel in Bogenmaß umrechnen
for i in range(8):
    # Berechne die Position jedes Vogels
    x = -70 + i * 20 * math.cos(angle_radians)
    y = 200 + i * 20 * math.sin(angle_radians)
    bird(x, y, 7, "white")

for i in range(8):
    # Berechne die Position jedes Vogels
    x = -70 + i * 20 * math.cos(angle_radians)
    y = 200 - i * 20 * math.sin(angle_radians)
    bird(x, y, 7, "white")

#Bäume#
baum(-320, -200, 0.5)
baum(-240, -175, 0.7)


#Schloss#

#Pfahl#
def Pfahl(x, y, size):
    trapezoid(x, y, 40*size, 50*size, 200*size, "pink", "pink")
    trapezoid(x+size, y+200*size, 60*size, 50*size, 50*size, "pink", "pink")
    rectangle(x+5*size, y+250*size, 40*size, 60*size, "pink", "pink")
    myIsoscelesTriangle(x, y+310*size, 50*size, 75, "pink", "pink")
    rectangle(x+25*size, y+403.3*size, 1*size, 30*size, "pink", "pink")
    setheading(270)
    myIsoscelesTriangle(x+25*size, y+473.3*size, 40*size, 75, "pink", "pink")

def Turm(x, y , size, pColor, fColor):
    #Mauer
    pencolor(pColor)
    fillcolor(fColor)
    begin_fill()
    teleport(x, y)
    left(90)
    forward(120*size)
    right(90)
    for i in range(3):
        forward(15*size)
        right(90)
        forward(15*size)
        left(90)
        forward(15+size)
        left(90)
        forward(15*size)
        right(90)
    forward(15*size)
    right(90)
    forward(120*size)
    goto(x, y)
    end_fill()

    rectangle(x+20*size, y+120*size+40*size-15*size, 40*size, 60*size, pColor, fColor)

    draw_roof(top_width=70*size, bottom_width=90*size, height=50*size, start_x=x+100*size/2, start_y=y+195*size,
         curve_factor=0.7, num_inner_curves=4, roof_color="PaleVioletRed", curve_color="white")


def Tor(width=100, height=50, aspect_ratio=1.0, orientation="up",
                    start_x=0, start_y=0, line_thickness=2, line_spacing=10):
    """
    Zeichnet ein halbes Oval mit senkrechten Strichen.

    :param width: Breite des Ovals
    :param height: Höhe des Ovals
    :param aspect_ratio: Verhältnis zwischen Breite und Höhe (größer -> schmaler)
    :param orientation: 'up' für obere Hälfte, 'down' für untere Hälfte
    :param start_x: X-Koordinate der Startposition
    :param start_y: Y-Koordinate der Startposition
    :param line_thickness: Dicke der senkrechten Striche
    :param line_spacing: Abstand zwischen den senkrechten Strichen
    """

    speed(3)  # Zeichnet mit mittlerer Geschwindigkeit
    penup()
    goto(start_x - width / 2, start_y if orientation == "up" else start_y - height)
    pendown()
    pencolor("white")

    # Das halbe Oval wird durch kleine Liniensegmente genähert
    steps = 50
    points = []
    for i in range(steps + 1):
        angle = math.pi * (i / steps)  # Werte zwischen 0 und Pi für eine Halbellipse
        x = (width / 2) * math.cos(angle) + start_x
        y = (height / (2 * aspect_ratio)) * math.sin(angle) + start_y
        if orientation == "down":
            y = start_y - (height / (2 * aspect_ratio)) * math.sin(angle)  # Spiegelt das halbe Oval nach unten
        points.append((x, y))

    # Zeichne die Kontur des Ovals
    begin_fill()
    fillcolor("purple")
    penup()
    for x, y in points:
        goto(x, y)
        pendown()
    penup()
    end_fill()
    # Zeichne senkrechte Striche innerhalb des Ovals
    pensize(line_thickness)
    for x in range(int(start_x - width / 2), int(start_x + width / 2), line_spacing):
        # Berechne die obere und untere Grenze des Ovals für die gegebene x-Koordinate
        rel_x = (x - start_x) / (width / 2)  # Normiertes x im Bereich [-1, 1]
        if -1 <= rel_x <= 1:  # Nur innerhalb des Ovals zeichnen
            y_top = (height / (2 * aspect_ratio)) * math.sqrt(1 - rel_x**2) + start_y
            y_bottom = start_y if orientation == "up" else (start_y - (height / (2 * aspect_ratio)))
            penup()
            goto(x, y_bottom)
            pendown()
            goto(x, y_top)
            penup()


def draw_roof(top_width=100, bottom_width=200, height=100, start_x=0, start_y=0,
              curve_factor=0.6, num_inner_curves=4, roof_color="purple", curve_color="white"):
    """
    Zeichnet ein gefülltes Dach mit weißen inneren Bézier-Kurven, aber ohne äußere Randlinien.

    :param top_width: Breite der oberen Linie (kleiner)
    :param bottom_width: Breite der unteren Linie (größer)
    :param height: Höhe des Dachs
    :param start_x: X-Koordinate der Startposition (Mitte der oberen Linie)
    :param start_y: Y-Koordinate der Startposition (obere Linie)
    :param curve_factor: Krümmungsfaktor für die Seitenkurven (höher = stärkere Krümmung)
    :param num_inner_curves: Anzahl der weißen Bézier-Kurven
    :param roof_color: Farbe für das gefüllte Dach
    :param curve_color: Farbe der mittleren Bézier-Kurven
    """
    penup()

    # Koordinaten berechnen
    half_top = top_width / 2
    half_bottom = bottom_width / 2
    bottom_y = start_y - height  # Position der unteren Linie

    # 🎨 1. Dachfläche mit Füllung zeichnen
    goto(start_x - half_top, start_y)
    pendown()
    fillcolor(roof_color)
    begin_fill()

    # Obere Linie
    goto(start_x + half_top, start_y)
    # Rechte Kurve
    goto(start_x + half_bottom, bottom_y)
    # Untere Linie
    goto(start_x - half_bottom, bottom_y)
    # Linke Kurve
    goto(start_x - half_top, start_y)

    end_fill()
    penup()

    # 🖌️ 2. Nur die weißen Bézier-Kurven in der Mitte zeichnen
    steps = 40  # Mehr Schritte für eine flüssigere Kurve
    total_curves = num_inner_curves + 2  # 2 äußere Kurven mit einrechnen

    for curve in range(1, total_curves - 1):  # Nur die inneren Kurven zeichnen (keine äußeren)
        t_pos = curve / (total_curves - 1)  # Position zwischen linker und rechter Seite
        x_start = (1 - t_pos) * (start_x - half_top) + t_pos * (start_x + half_top)
        x_end = (1 - t_pos) * (start_x - half_bottom) + t_pos * (start_x + half_bottom)

        # Setze die Linienfarbe auf Weiß und Pinselgröße auf 3 Pixel
        pensize(3)
        pencolor(curve_color)

        # Zeichne eine Bézier-Kurve
        goto(x_start, start_y)
        pendown()
        for i in range(steps + 1):
            t = i / steps
            x = (1 - t) * x_start + t * x_end
            y = ((1 - t) ** 2 * start_y +
                 2 * (1 - t) * t * (start_y - height * curve_factor) +
                 t ** 2 * bottom_y)  # Krümmung abhängig von curve_factor
            goto(x, y)
        penup()


def mySchloss(x, y):
    ## Schloss
    ## zweiter Pfahl
    size = 0.7
    Pfahl( x+80 , y, size)
    ## erster Turm
    Turm( x+20, y, 1, "mediumvioletred", "mediumvioletred")
    setheading(0)
    #erstes Tor
    Tor(width=50, height=120, aspect_ratio=1.5, orientation="up",
              start_x=x+78, start_y=y, line_thickness=2, line_spacing=15)
    ## dritter Pfahl
    size = 0.4
    Pfahl(x+140, -150, size)
    ##zweiter Turm
    Turm(x+120, y, 0.7, "mediumvioletred", "mediumvioletred")
    ## zweites Tor
    Tor(width=50, height=120, aspect_ratio=1.5, orientation="up",
              start_x=x+160, start_y=y, line_thickness=2, line_spacing=15)
    setheading(0)
    ## vierter Pfahl
    size = 0.5
    Pfahl(x+200, y, size)
    ## linker Pfahl
    size=0.5
    Pfahl(x, y, size)

mySchloss(0, -150)



