import math

class robot:
    def __init__(self, x = 0, y = 0, diam = 50, m = 0.5, ut = 1/50, fatr = 1):
        # GENERICAL CONFIGURATIONS
        self.ut = ut
        self.fatr = fatr # REDUCING IN 0,1% ACELLERATION
        self.m = m
        self.diameter = diam
        self.raio = diam/2
        
        # ACTUAL STATE OF THE PLAYER
        self.x = x
        self.y = y 
        self.angle = 1.5*math.pi
        self.vmax = 50

        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.vl = 0
        self.vAngle = 0

        self.ax = 0
        self.ay = 0
        self.ar = 0
        self.al = 0
        self.aAngle = 0

        # LAST STATE OF THE PLAYER
        self.last_x = 0
        self.last_y = 0
        self.last_vx = 0
        self.last_vy = 0
        self.last_ax = 0
        self.last_ay = 0
        self.last_angle = 0

    # def limit_vel(self):
    #     if(self.vx > self.vmax):
    #         self.vx = self.vmax
    #     if(self.vy > self.vmax):
    #         self.vy = self.vmax
    #     if(self.vr > self.vmax):
    #         self.vr = self.vmax
    #     if(self.vl > self.vmax):
    #         self.vl = self.vmax

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

    def setWellsVel(self,vr,vl):
        self.saveState()
        self.vl = vl
        self.vr = vr

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

        # self.limit_vel()

        #self.vx *= (1-self.elasticity)
        #self.vy *= (1-self.elasticity)
        
        self.x += (self.vx*ut)
        self.y += (self.vy*ut)

        # AFTER INTERACT RESET ACELERATION
        self.ax = 0
        self.ay = 0

        #print("x:{},y:{},vx:{},vy:{},ax:{},ay:{}".format(self.x,self.y,self.vx,self.vy,self.ax,self.ay))
        self.vx *= (1-self.fatr)
        self.vy *= (1-self.fatr)
    
    def step2(self, ut=None):
        if(ut==None):
            ut = self.ut

        # APPLY FORCE AND CALCULATE ACELLERATION, VELOCITY AND POSITION
        self.vr += self.ar*ut
        self.vl += self.al*ut

        r = self.raio
        d = self.diameter

        vr_x = (self.vr+self.vl)/2 # velocidade em x no referencial do robo
        w = ((self.vr-self.vl)/50) # velocidade angular
        
        self.angle += (w*ut) # Angulo
        self.angle = self.angle%(math.pi*2) # 0,26

        self.vx = vr_x * math.cos(self.angle)
        self.vy = vr_x * math.sin(self.angle)

        # self.limit_vel()

        self.x += self.vx*ut
        self.y += self.vy*ut

        # self.x += self.vx * ut
        # self.y += self.vy * ut

        # print('vr:{}, vl:{}, vr_x:{}, angle:{}, vx:{}, vy:{}, x:{}, y:{}'.format(self.vr,self.vl,vr_x,self.angle,self.vx,self.vy,self.x,self.y))
        self.vx *= (1-self.fatr)
        self.vy *= (1-self.fatr)
        self.vr *= (1-self.fatr)
        self.vl *= (1-self.fatr)

        # self.limit_vel()

    def pos(self, x, y):
        self.x = x
        self.y = y