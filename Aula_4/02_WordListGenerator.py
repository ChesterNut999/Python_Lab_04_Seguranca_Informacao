import itertools

string = input('Digite a palavra a ser permutada: ')
resultado = itertools.permutations(string, len(string))

print('-' * 60)
for i in resultado:
    print(''.join(i))