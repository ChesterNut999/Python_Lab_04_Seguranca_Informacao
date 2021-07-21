import socket, sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print('Conexão Falhou!!!')
        print('Erro: {}'.format(e))
        sys.exit()

    print('-' * 60)
    print('Socket criado com sucesso!!!')
    print('-' * 60)
    hostAlvo = input('Informe um IP/ HOST válido para conexão: ')
    portaAlvo = input('Informe a porta válida para conexão: ')

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print('-' * 60)
        print('Cliente TCP conectado com sucesso!!!\nHost: ' + hostAlvo, '\nPorta: ' + portaAlvo)
        s.shutdown(2)
        print('-' * 60)

    except socket.error as e:
        print('Conexão falhou!!!')
        print('Erro: {}'.format(e))
        sys.exit()

if __name__ == '__main__':
    main()