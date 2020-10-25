from environment import *
import time, random, math

if __name__ == "__main__":
    a=time.time()
    env = environment()
    env.reset()
    # env.elasticity = 1
    
    p0 = env.robots[0]
    p1 = env.robots[1]

    p0.pos(50,50)
    p0.diameter = 50
    p0.raio = 25
    p0.m = 1
    p0.angle = math.pi*6/4
    p0.saveState()

    p1.pos(800,500)
    p1.diameter = 50
    p1.raio = 25
    p1.m = 1
    p1.angle = 0
    p1.saveState()

    # Ciclo percorrido
    # Example 50x  (1/50)s >>> Percorrido 1s
    # Example 100x (1/50)s >>> Percorrido 2s

    # env.step([[0,0],[5000,0]])
    env.step([[0,0],[5000,-5000]])
    print('angulo antes da colisão: {}'.format(math.atan2(p1.vy,p1.vx)))
    for i in range(200):
        # env.step([[0,0],[0,0]])
        env.step([[0,0],[0,0]])

        time.sleep(1/50) ### Default 50 FPS
        if(not env.render()):
            break
    
    print('angulo depois da colisão: {}'.format(math.atan2(p1.vy,p1.vx)))

    print("Time execution was: {}".format((time.time()-a)))