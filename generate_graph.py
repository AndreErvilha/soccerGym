from my_environment2 import *
from dqn import DQNAgent
import numpy as np
import time as delay

agent = DQNAgent(3, 9)

#load
agent.load("./save/execution_to_generate_the_graphic.h5")

grau = math.pi/180/10

for a in range(360*10):
    a = a-math.pi
    x = math.cos(a*grau)
    y = math.sin(a*grau)
    d = a*grau

    state = [x,y,d]
    state = np.reshape(state, [1, 3])
    action = agent.act_2(state)

    i = math.hypot(x,y)
    print("x:{:.5f},y:{:.5f},a:{:.5f},i:{:.5f},action:{}".format(x,y,d,i,action))