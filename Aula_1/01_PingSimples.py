# importa o módulo/ biblioteca os (integra os programas ou recursos do SO)
import os

print('-' * 20, 'EXERCICIO 1 - PING:')
host = input("Digite o IP ou host a ser verificado: ")
print('-' * 60)

os.system('ping {}'.format(host))
print('-' * 60)

