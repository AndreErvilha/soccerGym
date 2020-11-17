from environment import *
import time, random, math

if __name__ == "__main__":
    a=time.time()
    env = environment()
    env.reset()

    for i in range(10000):
        env.step2([[0,0],[20,0]])
        # env.render()

    print("Time execution was: {}".format((time.time()-a)))
