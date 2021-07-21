import os, time

print('-' * 20, 'EXERCICIO 2 - PING MÚLTIPLO:')
with open('//resources/Aula_1/hosts') as file:
    dump = file.read().splitlines()

    for ip in dump:
        print('Verificando HOST/ IP: ', ip)
        print('-' * 60)
        os.system('ping -c3 {} '.format(ip))
        print('-' * 60)
        time.sleep(5)