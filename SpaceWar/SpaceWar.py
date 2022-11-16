import turtle, random
import winsound

pencere = turtle.Screen()
pencere.title('Space War')
pencere.bgcolor('black')
pencere.bgpic("uzay.gif")
pencere.setup(height=600, width=600)

turtle.register_shape("oyuncu.gif")
turtle.register_shape("dusman.gif")
turtle.register_shape("ates.gif")

oyuncu = turtle.Turtle()
oyuncu.color("blue")
oyuncu.speed(0)
oyuncu.shape("oyuncu.gif")
oyuncu.setheading(90)
oyuncu.penup()
oyuncu.goto(0, -250)
oyuncuhizi = 30

ates = turtle.Turtle()
ates.color("yellow")
ates.speed(0)
ates.shape("ates.gif")
ates.setheading(90)
ates.penup()
ates.goto(0, -250)
ateshizi = 20
ates.hideturtle()
ates.turtlesize(1, 1)
ateskontrol = False

yaz = turtle.Turtle()
yaz.color("white")
yaz.speed(0)
yaz.penup()
yaz.goto(0, 200)
yaz.hideturtle()


def atesgit():
    y = ates.ycor()
    y = y + ateshizi
    ates.sety(y)


def sola_git():
    x = oyuncu.xcor()
    x = x - oyuncuhizi
    if x < -300:
        x = -300
    oyuncu.setx(x)

def saga_git():
    x = oyuncu.xcor()
    x = x + oyuncuhizi
    if x > 300:
        x = 300
    oyuncu.setx(x)

def yukari_git():
    y = oyuncu.ycor()
    y = y + oyuncuhizi
    if y > 270:
        y = 270
    oyuncu.sety(y)

def asagi_git():
    y = oyuncu.ycor()
    y = y - oyuncuhizi
    if y < -270:
        y = -270
    oyuncu.sety(y)

def ateset():
    global ateskontrol
    winsound.PlaySound("lazer.wav", winsound.SND_ASYNC)
    x = oyuncu.xcor()
    y = oyuncu.ycor() + 20
    ates.goto(x, y)
    ates.showturtle()
    ateskontrol = True


hedefler = []
for i in range(7):
    hedefler.append(turtle.Turtle())
for hedef in hedefler:
    hedef.color("red")
    hedef.speed(0)
    hedef.turtlesize(1, 1)
    hedef.shape("dusman.gif")
    hedef.penup()
    hedef.setheading(90)
    x = random.randint(-280, 280)
    y = random.randint(180, 260)
    hedef.goto(x, y)




pencere.listen()
pencere.onkey(sola_git, "Left")
pencere.onkey(saga_git, "Right")
pencere.onkey(yukari_git, "Up")
pencere.onkey(asagi_git, "Down")
pencere.onkey(ateset, "space")


while True:
    if ateskontrol:
        atesgit()


    for hedef in hedefler:
        y = hedef.ycor()
        y = y-2
        hedef.sety(y)


        if hedef.distance(ates) < 20:

            ates.hideturtle()
            hedef.hideturtle()
            hedefler.pop(hedefler.index(hedef))
            winsound.PlaySound("patlama.wav", winsound.SND_ASYNC)

        if hedef.ycor() < -270 or hedef.distance(oyuncu) < 20:
            yaz.write("You LOSE", align="center", font=("Courier", 30, "bold"))

    if len(hedefler) == 0:
        yaz.write("You WİN", align="center", font=("Courier", 30, "bold"))


