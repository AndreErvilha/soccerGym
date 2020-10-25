from environment import *
import time, random, math

if __name__ == "__main__":
    a=time.time()
    env = environment()
    env.reset()
    
    p0 = env.robots[0]
    p1 = env.robots[1]

    p0.pos(500,300)
    p0.diameter = 50
    p0.raio = 25
    p0.m = 1
    p0.angle = 0
    p0.saveState()

    p1.pos(300,300)
    p1.diameter = 50
    p1.raio = 25
    p1.m = 1
    p1.angle = 0
    p1.saveState()

    # Ciclo percorrido
    # Example 50x  (1/50)s >>> Percorrido 1s
    # Example 100x (1/50)s >>> Percorrido 2s

    env.step([[0,0],[5000,0]])
    # env.step2([[0,0],[5000,5000]])
    for i in range(200):
        env.step([[0,0],[0,0]])
        # env.step2([[0,0],[0,0]])

        time.sleep(1/50) ### Default 50 FPS
        if(not env.render()):
            break

    print("Time execution was: {}".format((time.time()-a)))