user = 'gabriel'
password = '1234'
validacao = False
i = 0
while validacao == False and i < 3:
    i += 1
    userDigitado = input('Digite o nome de usuário: ')
    passDigitado = input('Digite o password: ')
    if userDigitado == user and password == passDigitado:
        validacao = True

if validacao == False:
    print('Número de tentativas ultrapassado')
else:
    print('Acesso Permitido')
