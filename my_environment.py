from environment import *
class MyEnvionment(environment):
    
    # You can override methods and implement your own environment
    def render(self):
        return super().render() 

    def reset(self):
        return super().reset()

    def observation(self):
        obs = super().observation()
        ball_pos = obs["ball"]["pos"]
        player_pos = obs["player"]["pos"]
        distance = math.hypot(ball_pos[0]-player_pos[0],ball_pos[1]-player_pos[1])
        ball_vel = obs["ball"]["vel"]
        player_vel = obs["player"]["vel"]
        return [
            (ball_pos[0]-player_pos[0])/distance,
            (ball_pos[1]-player_pos[1])/distance,
            ball_vel[0]-player_vel[0],
            ball_vel[1]-player_vel[1]
        ]

    def reward(self):
        # angulo vetor (robo->bola)
        teta = math.atan(self.robots[0].y-self.robots[1].y,self.robots[0].x-self.robots[1].x)
        alpha = math.atan(self.robots[0].ay-self.robots[1].ay,self.robots[0].ax-self.robots[1].ax)
        delta = abs(teta-alpha)
        delta = delta/math.pi*1000
        return 1000-delta;

    def done(self):
        return super().done()

    def info(self):
        return super().info()

if __name__ == "__main__":
    env = MyEnvionment()

    state = env.reset()
    commands = [-100,-100]
    obs, rwd, done, info = env.step(commands)
    print("Obs: {}, rwd: {}, done: {}, info: {}".format(obs, rwd, done, info))