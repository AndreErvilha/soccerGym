from my_environment import *
from dqn import DQNAgent
import numpy as np
import time as delay

state_size = 3
action_size = 9

actions = [ [[0,0],[-100,-100]],    [[0,0],[-100,0]],   [[0,0],[-100,100]],
            [[0,0],[0,-100]],       [[0,0],[0,0]],      [[0,0],[0,100]],
            [[0,0],[100,-100]],     [[0,0],[100,0]],    [[0,0],[100,100]]]

env = MyEnvironment()
agent = DQNAgent(state_size, action_size)
agent.load("./save/example_dqn.h5")#load
batch_size = 32
for e in range(3000):
    state = np.reshape(env.reset(), [1, state_size])
    last_reward = 0
    for time in range(1000):
        env.render() #render
        action = agent.act_2(state)
        commands = actions[action]
        next_state, reward, done, _ = env.step2(commands)
        next_state = np.reshape(next_state, [1, state_size])
        agent.remember(state, action, reward, next_state, done)
        state = next_state

        if len(agent.memory) > batch_size:
            agent.replay(batch_size)
    if e % 1 == 0:
        agent.save("./save/example_dqn.h5")


        