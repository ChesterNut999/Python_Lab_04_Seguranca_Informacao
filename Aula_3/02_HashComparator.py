import hashlib, os

# Diretórios dos arquivos
import struct

arquivo1 = '/home/Maurilio/PycharmProjects/Python_Lab_04_Test_Py_Seguranca_Informacao/resources/Aula_3/a.txt'
arquivo2 = '/home/Maurilio/PycharmProjects/Python_Lab_04_Test_Py_Seguranca_Informacao/resources/Aula_3/b.txt'

# Define o tipo de codificação com leitura binária
hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

# Compara o conteúdo e os hashes dos arquivos
if hash1.digest() != hash2.digest():
    print('-' * 60)
    print(f'O conteúdo do arquivo {os.path.basename(str.upper(arquivo1))} é difente de {os.path.basename(str.upper(arquivo2))}')
    print('-' * 60)
    print(f'O hash do arquivo {os.path.basename(str.upper(arquivo1))} é:', hash1.hexdigest())
    print(f'O hash do arquivo {os.path.basename(str.upper(arquivo2))} é:', hash2.hexdigest())
else:
    print('-' * 60)
    print(f'O conteúdo do arquivo {os.path.basename(str.upper(arquivo1))} é igual a {str.upper(os.path.basename(arquivo2))}')
    print('-' * 60)
    print(f'O hash do arquivo {os.path.basename(str.upper(arquivo1))} é:', hash1.hexdigest())
    print(f'O hash do arquivo {os.path.basename(str.upper(arquivo2))} é:', hash2.hexdigest())
