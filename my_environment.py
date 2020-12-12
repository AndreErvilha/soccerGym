from robot import *
import math

from environment import *
class MyEnvironment(environment):
    def done(self):
        return super().done()
    
    def info(self):
        return super().info()

    def observation(self):
        obs = super().observation()
        ball_pos = obs["ball"]["pos"]
        player_pos = obs["player"]["pos"]
        distance = math.hypot(ball_pos[0]-player_pos[0],ball_pos[1]-player_pos[1])
        angle = math.atan2(ball_pos[1]-player_pos[1],ball_pos[0]-player_pos[0])
        return [
            (ball_pos[0]-player_pos[0])/distance,
            (ball_pos[1]-player_pos[1])/distance,
            (angle-self.robots[1].angle)%(2*math.pi)
        ]
    
    # You can override methods and implement your own environment
    def render(self):
        return super().render() 

    def reset(self):
        return super().reset()


    # def rewarde(self):
    #     obs = super().observation()
    #     ball_pos = obs["ball"]["pos"]
    #     player_pos = obs["player"]["pos"]
    #     angle = math.atan2(ball_pos[1]-player_pos[1],ball_pos[0]-player_pos[0])
    #     angle2 = (angle-self.robots[1].angle)%(math.pi)
    #     angle2 = abs(math.cos(angle2))
    #     reward = 300*(1-angle2)
    #     return super().rewarde()#+reward;

    # def step(self, commands):
    #     cont = 0
    #     for robot in self.robots:
    #         if cont == 0:
    #             # robot.setForce(0,0)
    #             pass
    #         else:
    #             # robot.setForce(commands[0],commands[1])
    #             # print(robot.angle)
    #             robot.setAngle(commands[2])
    #         cont += 1
        
    #     return super().step(commands)

    # def move2whells(self,vr,vl):

    #     # commands = [vr,vl,teta]
    #     # print()
    #     # print(commands)

    #     self.robots[1].angle
    #     # diameter robot 50, then radius is 25

    #     vr_x = (vr*25+vl*25)/2
    #     angle = (vr*25-vl*25)/50
        
    #     self.robots[1].angle += (angle+teta)%(math.pi*2)

    #     # print('vx: {}, angle: {}'.format(vr_x,angle))

    #     vx = vr_x * math.cos(self.robots[1].angle)
    #     vy = vr_x * math.sin(self.robots[1].angle)

    #     commands = [vx,vy,(angle+teta)%(math.pi*2)]
    #     # print(commands)
    #     # print('x: {} y: {}'.format(self.robots[0].x,self.robots[1].y))
        
    #     # self.robots[1].pos(vx*10+150,vy*10+150)
    #     # self.robots[1].setAngle((angle+teta)%(math.pi*2))

    #     return self.step(commands)

if __name__ == "__main__":
    env = MyEnvionment()

    state = env.reset()
    commands = [-100,-100]
    obs, rwd, done, info = env.step(commands)
    print("Obs: {}, rwd: {}, done: {}, info: {}".format(obs, rwd, done, info))