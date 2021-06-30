import hashlib

hashUSer = input("Digite a palavra que será gerado o hash: ")

menu = int(input('''### MENU - ESCOLHA O TIPO de HASH ###
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a ser gerado: '''))

if menu == 1:
    res = hashlib.md5(hashUSer.encode('utf-8'))
    print('A hash MD5 da string: ', hashUSer, 'é: ', res.hexdigest())
elif menu == 2:
    res = hashlib.sha1(hashUSer.encode('utf-8'))
    print('A hash SHA1 da string: ', hashUSer, 'é: ', res.hexdigest())
elif menu == 3:
    res = hashlib.sha256(hashUSer.encode('utf-8'))
    print('A hash SHA256 da string: ', hashUSer, 'é: ', res.hexdigest())
elif menu == 4:
    res = hashlib.sha512(hashUSer.encode('utf-8'))
    print('A hash SHA512 da string: ', hashUSer, 'é: ', res.hexdigest())
else:
    print("Escolha uma opção valida")


