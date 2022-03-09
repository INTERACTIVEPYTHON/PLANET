from turtle import Shape, Turtle, mainloop, Vec2D as Vec

G = 8

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.t = 0
        self.dt = 0.01
    def init(self):
        for p in self.planets:
            p.init()
    def start(self):
        for i in range(10000):
            self.t += self.dt
            for p in self.planets:
                p.step()

class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        Turtle.__init__(self, shape=shape)
        self.penup()
        self.m = m
        self.setpos(x)
        self.v = v
        gravSys.planets.append(self)
        self.gravSys = gravSys
        self.resizemode("user")
        self.pendown()
    def init(self):
        dt = self.gravSys.dt
        self.a = self.acc()
        self.v = self.v + 0.5*dt*self.a
    def acc(self):
        a = Vec(0,0)
        for planet in self.gravSys.planets:
            if planet != self:
                v = planet.pos()-self.pos()
                a += (G*planet.m/abs(v)**3)*v
        return a
    def step(self):
        dt = self.gravSys.dt
        self.setpos(self.pos() + dt*self.v)
        if self.gravSys.planets.index(self) != 0:
            self.setheading(self.towards(self.gravSys.planets[0]))
        self.a = self.acc()
        self.v = self.v + dt*self.a

## create compound yellow/blue turtleshape for planets

def main():
    s = Turtle()
    s.reset()
    s.getscreen().tracer(0,0)
    s.ht()
    s.pu()
    s.fd(6)
    s.lt(90)
    s.begin_poly()
    s.circle(6, 180)
    s.end_poly()
    m1 = s.get_poly()
    s.begin_poly()
    s.circle(6,180)
    s.end_poly()
    m2 = s.get_poly()

    planetshape = Shape("compound")
    planetshape.addcomponent(m1,"orange")
    planetshape.addcomponent(m2,"blue")
    s.getscreen().register_shape("planet", planetshape)
    s.getscreen().tracer(1,0)

    ## setup gravitational system
    gs = GravSys()
    sun = Star(1000000, Vec(0,0), Vec(0,-2.5), gs, "circle")
    sun.color("yellow")
    sun.shapesize(1.8)
    sun.pu()
    earth = Star(12500, Vec(210,0), Vec(0,195), gs, "planet")
    earth.pencolor("green")
    earth.shapesize(0.8)
    moon = Star(1, Vec(220,0), Vec(0,295), gs, "planet")
    moon.pencolor("blue")
    moon.shapesize(0.5)
    gs.init()
    gs.start()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()'''



from turtle import *

def stop():
    global running
    running = False

def main():
    global running
    clearscreen()
    bgcolor("gray10")
    tracer(False)
    shape("triangle")
    f =   0.793402
    phi = 9.064678
    s = 5
    c = 1
    # create compound shape
    sh = Shape("compound")
    for i in range(10):
        shapesize(s)
        p =get_shapepoly()
        s *= f
        c *= f
        tilt(-phi)
        sh.addcomponent(p, (c, 0.25, 1-c), "black")
    register_shape("multitri", sh)
    # create dancers
    shapesize(1)
    shape("multitri")
    pu()
    setpos(0, -200)
    dancers = []
    for i in range(180):
        fd(7)
        tilt(-4)
        lt(2)
        update()
        if i % 12 == 0:
            dancers.append(clone())
    home()
    # dance
    running = True
    onkeypress(stop)
    listen()
    cs = 1
    while running:
        ta = -4
        for dancer in dancers:
            dancer.fd(7)
            dancer.lt(2)
            dancer.tilt(ta)
            ta = -4 if ta > 0 else 2
        if cs < 180:
            right(4)
            shapesize(cs)
            cs *= 1.005
        update()
    return "DONE!"

if __name__=='__main__':
    print(main())
    mainloop()

