from my_environment2 import *
from dqn import DQNAgent
import numpy as np
import time as delay

EPISODES = 1000
MOVES = 1000
TRAINING = False
# TRAINING = True

state_size = 3
action_size = 9

maxForce = 300

actions = [
    [[0,0],[-maxForce,-maxForce]],
    [[0,0],[2*-maxForce,0]],
    [[0,0],[-maxForce,maxForce]],
    [[0,0],[0,2*-maxForce]],
    [[0,0],[0,0]],
    [[0,0],[0,2*maxForce]],
    [[0,0],[maxForce,-maxForce]],
    [[0,0],[2*maxForce,0]],
    [[0,0],[maxForce,maxForce]]
]

agent = DQNAgent(state_size, action_size)

#load
agent.load("./save/execution1.h5")
env = MyEnvironment(ut=3/50)
batch_size = 100
print("done;episode;episodes;score;epsilon")

for e in range(EPISODES):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    # print(e)
    last_reward = 0
    for time in range(MOVES):
        if(not TRAINING):
            # delay.sleep(1/50)
            env.render()
        else:
            env.render()
            pass

        if(TRAINING):
            action = agent.act(state)
        else:
            action = agent.act_2(state)
        
        commands = actions[action]


        next_state, reward, done, _ = env.step2(commands)
        
        next_state = np.reshape(next_state, [1, state_size])
        state = next_state
        
        
        if(done):
            reward = 2000
        
        if(reward<=last_reward and done==False):
            last_reward = reward
            reward = -1000
        else:
            last_reward = reward
            
        if(TRAINING):
            agent.remember(state, action, reward, next_state, done)
        
        if done:
            print("1;{};{};{:.2f};{:.2}"
            .format(e, EPISODES, reward, agent.epsilon))
            if(TRAINING):
                agent.replay(len(agent.memory))
            break
        if len(agent.memory) > batch_size and TRAINING:
            agent.replay(batch_size)
        if(time == MOVES-1):
            print("0;{};{};{:.2f};{:.2}"
                .format(e, EPISODES, last_reward, agent.epsilon))

    if(TRAINING):
        agent.save("./save/execution1.h5")