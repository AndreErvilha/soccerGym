from my_environment import *
from dqn import DQNAgent
import numpy as np
import time as delay

if __name__ == "__main__":
    env = MyEnvionment()
    
    state_size = 4 # versor_posicao_axix_x, versor_posicao_axix_y, versor_velocidade_axix_x, versor_velocidade_axix_y
    action_size = 8    # 0 - 35 
                        # 0 >> 0º
                        # 35 >> 350º

    # Create an agent OBJECT
    agent = DQNAgent(state_size, action_size)

    # state = env.reset()
    # state = np.reshape(state, [1, state_size])

    # action = agent.act(state)
    # action_angle = (action*360/action_size)/180*math.pi
    # action_commands = [math.cos(action_angle)*250,math.sin(action_angle)*250]

    # print(env.step(action_commands))

    # agent.load("./save/foot_VS6_Trains.h5")
    # agent.load("./save/TCC_Trains_1.h5")
    # agent.load("./save/TCC_Trains_2.h5")
    # agent.load("./save/TCC_Trains_3.h5")
    # agent.load("./save/TCC_Trains_4.h5")
    done = False
    batch_size = 1

    reached = 0
    EPISODES = 20
    for e in range(EPISODES):
        state = env.reset()
        state = np.reshape(state, [1, state_size])
        last_reward = 0
        for time in range(500):
                       
            # Uncomment this to render
            env.render()
            
            action = agent.act(state)
            action_angle = (action*360/action_size)/180*math.pi
            
            action_commands = [math.cos(action_angle)*5000,math.sin(action_angle)*5000]
            state, reward, done, info = env.step(action_commands)
            # print("state: {}, reward: {}, done: {}, ".format(state,reward,done))
            reward = reward if reward > last_reward else -1000
            last_reward = reward
            #reward = reward if not done else reward * 2

            state = np.reshape(state, [1, state_size])
            agent.remember(state, action, reward, state, done)
            delay.sleep(1/50)
            if done:
                env.reset()
                print("episode: {}/{}, score: {}, e: {:.2}"
                      .format(e, EPISODES, round(reward,2), agent.epsilon))
                env.reward = 0
                env.last_reward = 0
                reached += 1
                break
            # Uncomment this to train
            if len(agent.memory) > batch_size:
                agent.replay(batch_size)
            if time == 499:
                print("episode: {}/{}, score: {}, e: {:.2} # NOT DONE"
                      .format(e, EPISODES, round(reward,2), agent.epsilon))
        # Uncomment this to save
        if e % 5 == 0:
            # agent.save("./save/foot_VS6_Trains.h5")
            # agent.save("./save/TCC_Trains_1.h5")
              agent.save("./save/TCC_Trains_4.h5")
    print("\nReached {} of {}".format(reached,EPISODES))
