from my_environment import *
from dqn import DQNAgent
import numpy as np
import time as delay

EPISODES = 3000
env = MyEnvironment(ut=3/50)

state_size = 3
action_size = 9

actions = [
    [[0,0],[-100,-100]],
    [[0,0],[-100,0]],
    [[0,0],[-100,100]],
    [[0,0],[0,-100]],
    [[0,0],[0,0]],
    [[0,0],[0,100]],
    [[0,0],[100,-100]],
    [[0,0],[100,0]],
    [[0,0],[100,100]]
]

# actions = [
#     [[0,0],[0,0]],
#     [[0,0],[0,100]],
#     [[0,0],[100,0]],
#     [[0,0],[100,100]]
# ]

agent = DQNAgent(state_size, action_size)
#load
agent.load("./save/example_dqn.h5")
done = False
batch_size = 32

for e in range(EPISODES):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    # print(e)
    last_reward = 0
    for time in range(1000):
        # delay.sleep(1/50)
        #render
        env.render()
        # action = agent.act(state)
        action = agent.act_2(state)
        commands = actions[action]
        
        # if env.key != '':
        #     # print(env.key-297)
        #     commands = actions[env.key-257]
        # else:
        #     commands = actions[0]
        
        # print(commands)
        # print(state)

        next_state, reward, done, _ = env.step2(commands)
        # reward = reward if not done else -10
        if(time==0):
            last_reward = reward-1

        if(reward<=last_reward and done==False):
            # print('bad reward')
            last_reward = reward
            reward = -1000
        else:
            # print('god reward')
            last_reward = reward
        
        next_state = np.reshape(next_state, [1, state_size])
        agent.remember(state, action, reward, next_state, done)
        state = next_state
        if done:
            print("done     => episode: {}/{}, score: {:.2f}, e: {:.2}"
                  .format(e, EPISODES, reward, agent.epsilon))
            agent.replay(len(agent.memory))
            break
        if len(agent.memory) > batch_size:
            # print('replay')
            agent.replay(batch_size)
        if(time == 999):
            # print(reward)
            # print(state)
            print("not done => episode: {}/{}, score: {:.2f}, e: {:.2}"
                  .format(e, EPISODES, reward, agent.epsilon))
    # if e % 1 == 0:
    #     agent.save("./save/example_dqn.h5")