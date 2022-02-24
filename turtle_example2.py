import turtle #first import the module

#after create graphical window
#gw=turtle.Screen()
#add a background colour
#gw.bgcolor("yellow")
#creating turtle object
w=turtle.Turtle()
n=3
#for i in range(n):
#    w.forward(100)
#    w.circle(50,extent=None,steps=None)
#    w.forward(100)

for i in range(4):
    w.forward(100)
    w.right(90)
for i in range(4):
    w.left(30)
    w.forward(150)
    w.right(30)
