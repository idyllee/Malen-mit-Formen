import turtle

# Spielfigur-Klasse
class Player:
    def __init__(self, x, y, color, shape="turtle"):
        self.x = x
        self.y = y
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.shape(shape)
        self.t.color(color)
        self.t.goto(self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.t.goto(self.x, self.y)

# Spieler erstellen
player1 = Player(-200, -200, "blue")   # Mit Pfeiltasten
player2 = Player(200, -200, "red")     # Mit WASD
tutu = Player(0, 9, "skyblue")
ziel =  Player(0, 300, "black")

# Bewegungsfunktionen
def p1_up(): player1.move(0, 20)
def p1_down(): player1.move(0, -20)
def p1_left(): player1.move(-20, 0)
def p1_right(): player1.move(20, 0)


def p2_up(): player2.move(0, 20)
def p2_down(): player2.move(0, -20)
def p2_left(): player2.move(-20, 0)
def p2_right(): player2.move(20, 0)


def tutu_up(): tutu.move(0, 20)
def tutu_down(): tutu.move(0, -20)
def tutu_left(): tutu.move(-20, 0)
def tutu_right(): tutu.move(20, 0)


# Bildschirm und Tastenzuweisungen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.listen()

# Spieler 1 – Pfeiltasten
screen.onkey(p1_up, "Up")
screen.onkey(p1_down, "Down")
screen.onkey(p1_left, "Left")
screen.onkey(p1_right, "Right")

# Spieler 2 – WASD
screen.onkey(p2_up, "w")
screen.onkey(p2_down, "s")
screen.onkey(p2_left, "a")
screen.onkey(p2_right, "d")

screen.onkey(tutu_up, "i")
screen.onkey(tutu_down, "j")
screen.onkey(tutu_left, "k")
screen.onkey(tutu_right, "l")

screen.mainloop()
