import hashlib

print('-' * 60)

# string = hashlib.md5(str.encode(input('Gere o Hash para uma palavra: ')))
# print('Hash MD5 gerado para',string,':' + string.hexdigest())

string = input('Gere um Hash a partir da palavra digitada. Aguardando sua entrada...\n')
print('-' * 60)

menu = int(input('###### MENU DE HASH ######\n'
             '1) MD5\n'
             '2) SHA1\n'
             '3) SHA256\n'
             '4) SHA512\n'
             '5) GERAR HASH COM TODAS AS CODIFICAÇÕES\n'
             '6) ** SAIR DO MENU\n' + ('-' * 60) +
             '\nDigite o número da opção desejada: '))

if menu == 1:
    resultado = hashlib.md5(str.encode('utf-8'))
    print('Você digitou:',string,'| Hash MD5:' + resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(str.encode('utf-8'))
    print('Você digitou:',string,'| Hash SHA1:' + resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(str.encode('utf-8'))
    print('Você digitou:',string,'| Hash SHA256:' + resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(str.encode('utf-8'))
    print('Você digitou:',string,'| Hash SHA512:' + resultado.hexdigest())
elif menu == 5:
    resultadoMD5 = hashlib.sha512(str.encode('utf-8'))
    resultadoSHA1 = hashlib.sha512(str.encode('utf-8'))
    resultadoSHA256 = hashlib.sha512(str.encode('utf-8'))
    resultadoSHA512 = hashlib.sha512(str.encode('utf-8'))

    print('Você digitou:',string,'\n' + ('-' * 60) + '\n'
                                ' - Hash MD5: ' + resultadoMD5.hexdigest(),'\n'
                                ' - Hash SHA1: ' + resultadoSHA1.hexdigest(),'\n'
                                ' - Hash SHA256: ' + resultadoSHA256.hexdigest(),'\n'
                                ' - Hash SHA512: ' + resultadoSHA512.hexdigest())
elif menu == 6:
    print('Obrigado por usar o gerador de Hash!')
    exit()
