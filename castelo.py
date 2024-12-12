import turtle

def desenhar_castelo():
    turtle.shape("classic")
zoom=2
turtle.setup(800,600)

#retangulo 
turtle.begin_fill()
turtle.color("purple")

turtle.up()
turtle.goto(120 * zoom,90 * zoom)
turtle.down()

retangulo_1= [
    (120,60),
    (60,60),
    (60,90),
    (120,90)
]

for (x,y) in retangulo_1:
    turtle.goto(x * zoom,y * zoom)

turtle.end_fill()

#torre3 
turtle.begin_fill()
turtle.color("magenta")

turtle.up()
turtle.goto(100 *zoom, 110 *zoom)
turtle.down()

torre_3= [
    (100,90),
    (80,90),
    (80,110),
    (100,110)
]

for (x,y) in torre_3:
     turtle.goto(x * zoom,y * zoom)

turtle.end_fill()

#trian3
turtle.begin_fill()
turtle.color("pink")

turtle.up()
turtle.goto(90 *zoom, 120*zoom)
turtle.down()

trian_3= [
    (100,110),
    (80,110),
    (90,120)
]

for (x,y) in trian_3:
     turtle.goto(x * zoom,y * zoom)

turtle.end_fill()

#quadrados
turtle.up()
turtle.goto(60 * zoom,93* zoom)
turtle.down()

turtle.speed(2)
turtle.begin_fill()
turtle.color("purple")

def desenha_quadrado(tamanho):
    for _ in range(4):
       turtle.forward(tamanho)
       turtle.right(90)

num_quadrados = 8
tamanho = 6
espacamento = 2


for _ in range(num_quadrados):
    desenha_quadrado(tamanho)
    turtle.penup()
    turtle.forward((tamanho + espacamento) * zoom)
    turtle.pendown()

turtle.end_fill()


#torre1 
turtle.begin_fill()
turtle.color("margenta")

turtle.up()
turtle.goto(140 *zoom, 100 *zoom)
turtle.down()

torre_1= [
    (140,60),
    (120,60),
    (120,100),
    (140,100)
]

for (x,y) in torre_1:
     turtle.goto(x * zoom,y * zoom)

turtle.end_fill()

#torre2 
turtle.begin_fill()
turtle.color("magenta")

turtle.up()
turtle.goto(60 *zoom,100 *zoom)
turtle.down()

torre_2= [
    (60,60),
    (40,60),
    (40,100),
    (60,100)
]

for (x,y) in torre_2:
     turtle.goto(x * zoom,y * zoom)

turtle.end_fill()

#trian1
turtle.begin_fill()
turtle.color("pink")

turtle.up()
turtle.goto(130 *zoom, 110*zoom)
turtle.down()

trian_1= [
    (140,100),
    (120,100),
    (130,110)
]

for (x,y) in trian_1:
     turtle.goto(x * zoom,y * zoom)

turtle.end_fill()

#trian2
turtle.begin_fill()
turtle.color("pink")

turtle.up()
turtle.goto(50 *zoom, 110*zoom)
turtle.down()

trian_2= [
    (60,100),
    (40,100),
    (50,110)
]

for (x,y) in trian_2:
     turtle.goto(x * zoom,y * zoom)

turtle.end_fill()

#porta_1
turtle.begin_fill()

turtle.up()
turtle.goto(100 *zoom, 80*zoom)
turtle.down()

turtle.pensize(2)
turtle.pencolor("pink")
turtle.fillcolor("magenta")

porta_1= [
    (100,60),
    (90,60),
    (90,80),
    (100,80)
]

for (x,y) in porta_1:
     turtle.goto(x * zoom,y * zoom)

turtle.end_fill()

#porta_2
turtle.begin_fill()

turtle.up()
turtle.goto(90 *zoom, 80*zoom)
turtle.down()

turtle.pensize(2)
turtle.pencolor("pink")
turtle.fillcolor("magenta")

porta_2= [
    (90,60),
    (80,60),
    (80,80),
    (90,80)
]

for (x,y) in porta_2:
     turtle.goto(x * zoom,y * zoom)

turtle.end_fill()



turtle.hideturtle()
turtle.done()