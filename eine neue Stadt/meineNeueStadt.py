# meine neue Stadt
from turtle import *
from neueStadtLib import *

bgcolor("mistyrose")
setup(1200, 1000)

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

mySchloss(0, -150)
