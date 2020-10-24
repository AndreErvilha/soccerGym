from my_environment import *
import time, random

def rnd_force():
    #x1 = random.randint(-5000,5000)
    #y1 = random.randint(-5000,5000)
    x1 = 0
    y1 = 0
    x2 = random.randint(-5000,5000)
    y2 = random.randint(-5000,5000)
    return [[x1,y1],[x2,y2]]

if __name__ == "__main__":
    a=time.time()
    env = MyEnvionment()

    env.reset()
    bestReward = 0
    for i in range(10000):
        commands = rnd_force()
        ### Default 50 FPS
        # time.sleep(1/50)
        observation, reward, done, info = env.step(commands)
        bestReward = reward if (reward>bestReward) else bestReward
        env.render()

    print("Time execution was: {}, best reward was: {}".format((time.time()-a),bestReward))