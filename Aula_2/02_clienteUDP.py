import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('-' * 60)
print('Cliente Socket criado com sucesso!!! Conectando ao server...')

host = 'localhost'
porta = 5432
msg = 'Olá servidor!'

try:
    s.sendto(msg.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)

finally:
    print('Cliente: Fechando conexão!')
    s.close()