from my_environment import *
import time, random, math

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
    angle = math.pi * 2 / 360
    # observation, reward, done, info = env.move2whells(angle*60,angle*30,0)
    for i in range(1000):
        commands = rnd_force()
        
        time.sleep(1/50) ### Default 50 FPS

        # observation, reward, done, info = env.step(commands)
        observation, reward, done, info = env.step2([angle*50/3, angle*50/3])
        # observation, reward, done, info = env.step2([0,0])
        # bestReward = reward if (reward>bestReward) else bestReward
        if(not env.render()):
            break

    print("Time execution was: {}, best reward was: {}".format((time.time()-a),bestReward))