from robot import *
import math
import random

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
            (player_pos[0]-ball_pos[0])/distance,
            (player_pos[1]-ball_pos[1])/distance,
            (angle-self.robots[1].angle)%(2*math.pi)
        ]
    
    # You can override methods and implement your own environment
    def render(self):
        return super().render() 

    def reset(self):
        invalid = True
        while(invalid):
            x = random.randint(50,self.width-50)
            y = random.randint(50,self.height-50)
            self.robots[0].pos(x,y)
            self.collide_with_wall(self.robots[1])
            invalid = self.verify_collisions()

        return self.observation()


    # def rewarde(self):
    #     return super().rewarde();

if __name__ == "__main__":
    env = MyEnvionment()

    state = env.reset()
    commands = [-100,-100]
    obs, rwd, done, info = env.step(commands)
    print("Obs: {}, rwd: {}, done: {}, info: {}".format(obs, rwd, done, info))