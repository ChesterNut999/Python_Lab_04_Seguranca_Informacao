import ipaddress

ip = '192.168.0.1/32'
# endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(ip, strict=False)

# print('-' * 60)
# print(f'Ip: {endereco}')
# print(f'Rede: {rede}')

for ip in rede:
    print(ip)