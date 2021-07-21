import time
from threading import Thread

def corrida(velocidade, piloto, trajeto=0):

    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} | km: {} \n'.format(piloto, trajeto))

# def carro2(velocidade):
#     trajeto = 0
#
#     while trajeto <= 100:
#         print('Carro2: ', trajeto)
#         trajeto += velocidade

t_carro1 = Thread(target=corrida, args=[10, 'Rafael'])
t_carro2 = Thread(target=corrida, args=[10, 'Maurilio'])

t_carro1.start()
t_carro2.start()

# carro1(10)
# print('-' * 60)
# carro2(20)