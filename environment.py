from robot import *
import math, pygame

# define some colors
BLACK = (20, 20, 20, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (81, 150, 116, 255)
GRAY = (200, 200, 200, 255)
YELLOW = (255, 200, 0, 255)
BLUE = (0, 55, 200, 255)

class environment:
    def __init__(self,ut=1/50):
        robot1 = robot(diam=30,m=0.1,fatr=0,ut=ut)
        robot2 = robot(fatr=0,ut=ut)

        self.robots = [robot1,robot2]
        self.width = 1000
        self.height = 600
        self.display = None
        self.angle = 0
        self.elasticity = 0.6
        self.key = ''
        
    def render(self):
        if(self.display == None):
            pygame.init()
            self.display = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption("Soccer")

        self.angle += 1
        # Draw external field
        pygame.draw.rect(self.display,GRAY,pygame.Rect(0,0,self.width,self.height))

        # Draw internal field
        pygame.draw.rect(self.display,GREEN,pygame.Rect(75,75,self.width-150,self.height-150))
        # pygame.draw.circle(self.display, BLUE, (250,300),(5))
        # pygame.draw.circle(self.display, GRAY, (350,300),(5))
        # pygame.draw.rect(self.display,GRAY,pygame.Rect(275,250,50,50))
        # pygame.draw.rect(self.display,GRAY,pygame.Rect(325,300,50,50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                self.key = event.key
                # print(self.key)    

        # Draw player
        def draw_player(player, angle, color):
            pygame.draw.circle(self.display, color,(int(player.x),int(player.y)),int(player.raio))
            raio = player.raio-(player.raio/5)-5
            # self.angle += 3
            radians = player.angle  # radians = player.angle/360*math.pi
            sen = math.sin(radians)
            cos = math.cos(radians)
            pygame.draw.circle(self.display,BLACK,(int(player.x+(raio*cos)),int(player.y+(raio*sen))),int(player.raio/5))

        teams = 0
        for robot in self.robots:
            if teams == 0:
                draw_player(robot,self.angle,YELLOW)
            else:
                draw_player(robot,self.angle,BLUE)
            teams +=1

        # Desenha tela
        pygame.display.update()
        return True

    def reset(self):
        cont = 2
        for robot in self.robots:
            robot.x = self.width/cont
            robot.y = self.height/cont
            robot.angle = 0
            cont+=1

        # self.robots[0].pos(self.width/4,self.height/2)
        # self.robots[1].pos(self.width*3/4,self.height/2)

        self.robots[0].pos(100,100)
        self.robots[1].pos(300,300)

        return self.observation()

    def step2(self, commands):
        cont = 0
        for robot in self.robots:
            if cont == 0:
                # robot.setForce(0,0)
                robot.setWellsForce(commands[0][1],commands[0][1])
                pass
            else:
                robot.setWellsForce(commands[1][0],commands[1][1])
                # print(commands)
                # robot.setWellsVel(commands[0],commands[1])

            robot.step2()
            self.__collide_with_wall(robot)
            cont+=1

        done = self.__verify_collisions()
        obs = self.observation()
        reward = self.rewarde()
        #done = self.done()
        info = self.info()
        return obs, reward, done, info

    def step(self, commands):
        cont = 0
        for robot in self.robots:
            if cont == 0:
                robot.setForce(commands[0][0],commands[0][1])
                pass
            else:
                robot.setForce(commands[1][0],commands[1][1])

            robot.step()
            self.__collide_with_wall(robot)
            cont+=1

        done = self.__verify_collisions()
        obs = self.observation()
        reward = self.rewarde()
        #done = self.done()
        info = self.info()
        return obs, reward, done, info

    def step2(self, commands):
        cont = 0
        for robot in self.robots:
            if cont == 0:
                robot.setWellsForce(commands[0][0],commands[0][1])
                pass
            else:
                robot.setWellsForce(commands[1][0],commands[1][1])
                # print(commands)
                # robot.setWellsVel(commands[0],commands[1])

            robot.step2()
            self.__collide_with_wall(robot)
            cont+=1

        done = self.__verify_collisions()
        obs = self.observation()
        reward = self.rewarde()
        #done = self.done()
        info = self.info()
        return obs, reward, done, info

    def observation(self):
        return {
            "ball":{
                "pos": [self.robots[0].x,self.robots[0].y],
                "vel": [self.robots[0].vx,self.robots[0].vy],
            },
            "player":{
                "pos": [self.robots[1].x,self.robots[1].y],
                "vel": [self.robots[1].vx,self.robots[1].vy],
            }
        }

    def rewarde(self):
        num = 1000*(self.robots[0].raio+self.robots[1].raio)
        distance = math.hypot(self.robots[0].x-self.robots[1].x,self.robots[0].y-self.robots[1].y)
        return num/distance

    def done(self):
        return ((self.robots[0].raio+self.robots[1].raio)+3) > math.hypot(self.robots[0].x-self.robots[1].x,
                                                                       self.robots[0].y-self.robots[1].y)

    def info(self):
        return {}

    def __collide(self, robo1, robo2):
        # imprime dados antes processamento da colisao
        # print('Antes')
        # print('x:{}, y:{}, vx:{}, vy:{}'.format(robo1.x,robo1.y,robo1.vx,robo1.vy))
        # print('x:{}, y:{}, vx:{}, vy:{}'.format(robo2.x,robo2.y,robo2.vx,robo2.vy))
        '''
        1. Decompor velocidade dos robos na componente beta
        2. Subtrair velocidade da componente beta da velocidade do robô
        3. Subtrair velocidade da componente beta da velocidade do robô

        Legenda:
            - alpha1: Angulo do sentido de movimento do robô 1
            - alpha2: Angulo do sentido de movimento do robô 2
            - beta: Angulo de interação (colisão)
        '''
        # Calcula angulo beta
        beta = math.atan2(robo2.y-robo1.y,
                          robo2.x-robo1.x)

        # Calcula modulo velocidade alpha e angulo
        vel_alpha1 = math.hypot(robo1.vx,robo1.vy)
        alpha1 = math.atan2(robo1.vy,robo1.vx)

        vel_alpha2 = math.hypot(robo2.vx,robo2.vy)
        alpha2 = math.atan2(robo2.vy,robo2.vx)

        delta1 = alpha1 - beta
        delta2 = alpha2 - beta

        ### print("\n\n########################################################")
        ### print("vel_alpha1= {}, alpha1={}\nvel_alpha2= {}, alpha2={}\n".format(vel_alpha1, alpha1, vel_alpha2, alpha2))

        # Calcula modulo velocidade alpha e angulo
        '''
        ############################################################################
        ### Parte da energia cinetica do objeto é tranferida para o outro objeto
        ### para isso é necessario calcular a componente que será transferida
        ############################################################################
        '''
        vel_beta_robo1 = vel_alpha1 * math.cos(delta1) # velocidade em modulo
        vel_beta_robo2 = vel_alpha2 * math.cos(delta2) # velocidade em modulo
        
        ### print("vel_beta_robo1={}, vel_beta_robo2={}".format(vel_beta_robo1,vel_beta_robo2))

        # Subtrai componente beta da alpha
        robo1.vx -= vel_beta_robo1 * math.cos(beta)
        robo1.vy -= vel_beta_robo1 * math.sin(beta)

        robo2.vx -= vel_beta_robo2 * math.cos(beta)
        robo2.vy -= vel_beta_robo2 * math.sin(beta)
        
        ''' #########################################################################
        ### O calculo de transferencia da energia depende da 'massa' dos dois corpos
        ###
        ###       / m1  -  m2 \       /    2m2    \ 
        ### v1 = |-------------| u1 +|-------------| u2
        ###       \ m1  +  m2 /       \ m1  +  m2 /
        ###
        ###
        ###       / m2  -  m1 \       /    2m1    \ 
        ### v2 = |-------------| u2 +|-------------| u1
        ###       \ m1  +  m2 /       \ m1  +  m2 /
        ###
        ### onde: 
        ###     v1,v2 = velocidade final no eixo de colisao
        ###     m1,m2 = massas dos corpos 1 e 2 consecutivamente
        ###     u1,u2 = velocidade inicial no eixo de colisao
        ######################################################################### '''
        somaMassa = robo1.m + robo2.m
        u1 = vel_beta_robo1 # velocidade em modulo
        u2 = vel_beta_robo2 # velocidade em modulo
        m1 = robo1.m
        m2 = robo2.m

        v1 = (((m1-m2)/(m1+m2))*u1)+((2*m2/(m1+m2))*u2)
        v2 = (((m2-m1)/(m1+m2))*u2)+((2*m1/(m1+m2))*u1)

        ### print("u1={}, u2={}, m1={}, m2={}, v1={}, v2={}".format(u1,u2,m1,m2,v1,v2))

        robo2.vx += v2 * math.cos(beta)
        robo2.vy += v2 * math.sin(beta)

        robo1.vx += v1 * math.cos(beta)
        robo1.vy += v1 * math.sin(beta)

        # Ajustes para funcionamento da movimentação 2 rodas
        var_x = robo2.angle-robo1.angle # Angulo entre os dois robos (#ref 2>1)

        mod_vel = math.hypot(robo1.vx*math.cos(delta1-robo1.angle),robo1.vy*math.sin(delta1-robo1.angle)) # modulo da velocidade transferida
        robo1.vl = robo1.vr = mod_vel*math.cos(var_x) # velocidade transferida no eixo x referencial

        var_x = robo1.angle-robo2.angle # Angulo entre os dois robos (#ref 1>2)

        mod_vel = math.hypot(robo2.vx*math.cos(delta2-robo2.angle),robo2.vy*math.sin(delta2-robo2.angle)) # modulo da velocidade transferida
        robo2.vl = robo2.vr = mod_vel*math.cos(var_x) # velocidade transferida no eixo x referencial

        ''' ##########################################################################
        ### Em caso de colisão o robo recebe a ultima posição antes da colisão
        ### isso evita que os objetos fiquem sobrepostos
        ########################################################################## '''

        robo1.x = robo1.last_x
        robo2.x = robo2.last_x
        robo1.y = robo1.last_y
        robo2.y = robo2.last_y

        # imprime dados após processamento da colisao
        # print('Depois')
        # print('x:{}, y:{}, vx:{}, vy:{}'.format(robo1.x,robo1.y,robo1.vx,robo1.vy))
        # print('x:{}, y:{}, vx:{}, vy:{}'.format(robo2.x,robo2.y,robo2.vx,robo2.vy))
        # print()
        
    def __verify_collisions(self):
        robot1 = self.robots[0]
        robot2 = self.robots[1]

        '''
        Verificar colisão:
            - Calcula distancia entre os robôs (1)
            - Verifica se distancia é menor que a soma dos raios (2)
        '''
        dx = robot1.x-robot2.x
        dy = robot1.y-robot2.y
        distance = math.sqrt(dx**2+dy**2) # (1)

        if distance <= (robot1.raio+robot2.raio): # (2)
            self.__collide(robot1,robot2)
            return True
        return False

    def __collide_with_wall(self, player):
            colided = False
            # Verify collisions between robot and walls
            # horizontally
            if player.left() < 0:
                player.x = 0+player.raio
                player.vx *= -self.elasticity
                colided = True
            elif player.right() > self.width:
                player.x = self.width-player.raio
                player.vx *= -self.elasticity
                colided = True
            #vertically
            if player.top() < 0:
                player.y = 0+player.raio
                player.vy *= -self.elasticity
                colided = True
            elif player.bottom() > self.height:
                player.y = self.height-player.raio
                player.vy *= -self.elasticity
                colided = True

            if colided:
                mod_vel = math.hypot(player.vx,player.vy)
                angle = math.atan2(player.vy,player.vx)
                delta = player.angle-angle
                vel = mod_vel*math.cos(delta)
                # print('vx{},vy{},angle{},delta{},vel{}'.format(player.vx,player.vy,angle,delta,vel))
                player.vr = vel
                player.vl = vel