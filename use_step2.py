from environment import *
import time, random, math

if __name__ == "__main__":
    a=time.time()
    env = environment()
    env.reset()

    _2pi = math.pi * 2
    ut = 1/50

    '''
        Movimento desejado
        1º girar em torno do ponto azul no sentido horario
        2º girar em torno do ponto preto no sentido anti-horario

        X<---+--->X   o
        |    |    |   |=> Centro da rotação
        |    |    |=====> Roda direita
        |    |==========> Centro do robô
        |===============> Roda esquerda

        Para realizar uma volta completa em torno do ponto 'o'
        é necessário que a roda esquerda gire com uma velocidade
        maior que a roda direita.

        O deslocamento das rodas seguem a formula abaixo:
        dl = 2*r1*pi
        dr = 2*r2*pi

        sendo:
        dl: deslocamento roda esquerda
        dr: deslocamento roda esquerda
        r1: distancia entre roda esquerda e centro da rotacao
        r2: distancia entre roda direita e centro da rotacao

        Para calcular a velocidade é necessario saber quanto tempo para 
        realizar a volta completa, se considermos 1 s, considerando ut (constante de tempo)
        igual 1/50 s, teremos que as velocidades devem ser:
        vl = dl * ut
        vr = dr * ut

        Para reproduzir a velocidade que desejamos devemos aplicar a força certa, considerando
        que a massa dos robôs é igual a 0.5 a força a ser aplicada seria

        fl = (m * dl)/s²
    '''
    # v = _2pi
    # m = 0.5
    # a = v/ut
    # f = a*m

    d = _2pi
    f = (0.5*d)/ut

    # Ciclo percorrido
    # Example 50x  (1/50)s >>> Percorrido 1s
    # Example 100x (1/50)s >>> Percorrido 2s
    for i in range(10000):
        if(i<50):
            env.step2([[0,0],[f*75,f*25]]) # set force go around blue
        elif(i<100):
            # env.step2([[0,0],[-f*75,-f*25]]) # unset force
            env.step2([[0,0],[f*25,f*75]]) # set force go around black
        else:
            env.step2([[0,0],[f*50,f*50]])
            # env.step2([[0,0],[0,0]])

        # print('vx_1: {}, vy_1:{}, vx_2:{}, vy_2:{}'.format(env.robots[0].vx,env.robots[0].vy,env.robots[1].vx,env.robots[1].vy))
        
        # time.sleep(1/50) ### Default 50 FPS
        # if(not env.render()):
            # break

    print("Time execution was: {}".format((time.time()-a)))