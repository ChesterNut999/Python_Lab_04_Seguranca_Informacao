import random, string

tamanho = int(input('Digite o tamanho de senha: '))
chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+,.:_/?'
rnd = random.SystemRandom() #os.urandom (gera números aleatórios a partir de fontes do SO

print(''.join(rnd.choice(chars) for i in range(tamanho)))