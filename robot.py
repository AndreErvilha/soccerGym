import math

class robot:
    def __init__(self, x = 0, y = 0, diam = 50, m = 0.5, ut = 1/50):
        # GENERICAL CONFIGURATIONS
        self.ut = ut
        self.fatr = 0.50 # REDUCING IN 0,1% ACELLERATION
        self.m = m
        self.diameter = diam
        self.raio = diam/2
        
        # ACTUAL STATE OF THE PLAYER
        self.x = x
        self.y = y 
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.vl = 0
        self.ax = 0
        self.ay = 0
        self.ar = 0
        self.al = 0
        self.angle = 1.5*math.pi

        # LAST STATE OF THE PLAYER
        self.last_x = 0
        self.last_y = 0
        self.last_vx = 0
        self.last_vy = 0
        self.last_ax = 0
        self.last_ay = 0
        self.last_angle = 0

    def left(self):
        return self.x - (self.diameter/2)

    def right(self):
        return self.x + (self.diameter/2)

    def top(self):
        return self.y - (self.diameter/2)

    def bottom(self):
        return self.y + (self.diameter/2)

    def saveState(self):
        # SAVE STATE
        self.last_x = self.x
        self.last_y = self.y
        self.last_vx = self.vx
        self.last_vy = self.vy
        self.last_ax = self.ax
        self.last_ay = self.ay
        self.last_angle = self.angle

    def setAngle(self, angle):
        self.angle = angle

    def setVel(self, vx, vy):
        self.saveState()
        self.vx = vx
        self.vy = vy
        # self.vx -= self.vx*self.fatr
        # self.vy -= self.vy*self.fatr

    def setWellsVel(self,vl,vr):
        self.saveState()
        self.vr = vr
        self.vl = vl
        # self.vr -= self.vr*self.fatr
        # self.vl -= self.vl*self.fatr

    def setForce(self,fx,fy):
        # >> Força > Aceleração > Velocidade > Deslocamento
        # SAVE STATE
        self.saveState()
        self.ax = fx/self.m
        self.ay = fy/self.m
        # self.vx -= self.vx*self.fatr
        # self.vy -= self.vy*self.fatr

    def setWellsForce(self,fr,fl):
        self.saveState()
        self.ar = fr/self.m
        self.al = fl/self.m
        # self.vx -= self.vx*self.fatr
        # self.vy -= self.vy*self.fatr

    def step(self, ut = None):
        if(ut==None):
            ut = self.ut

        # APPLY FORCE AND CALCULATE ACELLERATION, VELOCITY AND POSITION
        self.vx += self.ax*ut
        self.vy += self.ay*ut

        #self.vx *= (1-self.elasticity)
        #self.vy *= (1-self.elasticity)
        
        self.x += (self.vx*ut)
        self.y += (self.vy*ut)

        # AFTER INTERACT RESET ACELERATION
        self.ax = 0
        self.ay = 0

        #print("x:{},y:{},vx:{},vy:{},ax:{},ay:{}".format(self.x,self.y,self.vx,self.vy,self.ax,self.ay))
    
    def step2(self, ut=None):
        if(ut==None):
            ut = self.ut

        r = self.raio
        d = self.diameter

        vr_x = (self.vr+self.vl)*r/2
        self.angle += (self.vr-self.vl)*r/d

        self.angle = self.angle%(math.pi*2)

        self.x += vr_x * math.cos(self.angle)
        self.y += vr_x * math.sin(self.angle)

        # self.x += self.vx * ut
        # self.y += self.vy * ut

        print('vr: {}, vl:{}, vr_x:{}, angle:{}, vx:{}, vy:{}'.format(self.vr,self.vl,vr_x,self.angle,self.vx,self.vy))

    def pos(self, x, y):
        self.x = x
        self.y = y

"""
p = player(0,0,30)

p.move(100,1000)
for i in range(50):
    p.move(0,-20)
    print("{}, {}, {}".format(i,p.X,p.Y))

for i in range(50,100):
    p.move(0,-20)
    print("{}, {}, {}".format(i,p.X,p.Y))
"""
