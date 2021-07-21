import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('-' * 60)
print('Server Socket criado com sucesso!!! Aguardando conexão cliente...')

host = 'localhost'
porta = 5432

s.bind((host, porta))
msg = '\nServidor: Olá cliente!'

while 1:
    dados, endereco = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (msg.encode()), endereco)
        print('Conexão estabelecida! Encerrando teste...')
