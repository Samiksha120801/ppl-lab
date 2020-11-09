import turtle

s = turtle.getscreen()
t = turtle.Turtle()

class shape:
    def __init__(self, sides=0, length=0):
        self.sides = sides
        self.length = length

class polygon(shape):   #polygon -> shapes
    def info(self):
        print("In geometry, a polygon can be defined as a flat or plane, two-dimensional  with straight sides.")

class square(polygon):    #square -> polygon -> shapes
    def show(self):
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)

class pentagon(polygon):    #pentagon -> polygon -> shapes
    def show(self):
        for i in range(5):
            t.forward(self.length)
            t.right(72)

class hexagon(polygon):     #hexagon -> polygon ->shapes
    def show(self):
        for i in range(6):
            t.forward(self.length)
            t.right(60)


class octagon(polygon):     #octagon -> polygon ->shaoes
    def show(self):
        for i in range(6):
            t.forward(self.length)
            t.right(45)


class triangle(polygon):    #triangle -> polygon ->shapes
    def show(self):
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)

pent1 = hexagon(6, 150)
pent1.info()
pent1.show()