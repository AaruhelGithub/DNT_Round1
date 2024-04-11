import turtle
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Turtle")
t = turtle.Turtle()
t.penup()
t.backward(120)
t.left(90)
t.forward(100)
t.right(90)

t.pendown()
t.right(90)
t.forward(190)

t.left(90)
n = 60
angle = 360/60
for i in range(0,31):
  t.forward(10)
  t.left(angle)
t.right(6)

t.left(180)
t.penup()
t.forward(150)
t.right(90)
t.forward(190)


t.right(180)
t.pendown()
t.forward(190)
t.right(155)
t.forward(210)
t.right(205)
t.forward(190)

t.right(90)
t.penup()
t.forward(130)
t.right(90)
t.forward(190)

t.right(180)
t.pendown()
t.forward(190)
t.right(90)
t.forward(40)
t.backward(80)