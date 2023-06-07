'''Usuarios cadastrados'''
login = ['padrinho','ong','apadrinhado', 'ong2', 'ong3']
'''Senha dos usuários'''
senha = ['123', '321', '213', '312', '231']
'''
Ongs disponiveis e seus eventos
a 3° casa da lista é um array com o index do login que é padrinho da ong
a 4° casa da lista é a correspondencia de login da ong
'''
ongs = [ 
    ['Banco de alimentos', 'Evento dia 10/06/2023', 'Brasilandia', [0], 1], 
    ['Ação da Cidadania', 'Evento dia 11/06/2023', 'Praça da Sé', [0], 3], 
    ['Amigos do Bem', 'Evento dia 13/06/2023', 'Perus', [], 4]
]


tipoUsuario = ['1', '2', '3']
logado = False
opcaoMenuIncial = ['1','2','0']


def validaOpcao(opcoes,msg):
    opcao = input(msg)
    '''Somente saira do loop quando digitar uma opção que contem na lista de opções'''
    while opcao not in opcoes:
        print("Digite uma opção válida!")
        opcao = input(msg)
    return opcao


def menuInicial():
    msg = "1) Fazer login \n2) Esqueci a senha \n0) Sair\n"
    opcao = validaOpcao(opcaoMenuIncial, msg)
    '''Switch case para as opções listadas'''
    match opcao:
        case '1':
            logado = menuLogin()
            menuMain(logado)
        case '2':
            esqueciSenha()
    return opcao

def menuLogin():
    contador = 0
    loginUsuario = input("Informe seu login: \n")

    while loginUsuario not in login:
        print("Login informado é invalido.")
        loginUsuario = input("Informe seu login: \n")

    for i in range(len(login)):
        if login[i] == loginUsuario:
            senhaDoLogin = senha[i]
            contador = i

    senhaUsuario = input("Informe sua senha: \n")
    while senhaUsuario != senhaDoLogin:
        print("Senha informada é invalido.")
        senhaUsuario = input("Informe sua senha: \n")
    '''Retorna o valor do index da lista do perfil logado.'''
    return contador

def esqueciSenha():
    print("Bora recuperar sua conta?")
    loginUsuario = input("Informe o login que deseja recuperar a conta: \n")
    while loginUsuario not in login:
        print("Login informado não existe na base de dados!")
        loginUsuario = input("Informe um login valido para recuperar sua conta: \n")
    '''Loop para rodar na lista de login e verificar qual a senha para o login informado '''
    for i in range(len(login)):
        if login[i] == loginUsuario:
            print(f"A senha para o login informado é {senha[i]}")
            break


def menuPadrinho(usuario):
    msg = "1) Ver ongs Disponíveis \n2) Ver suas ongs apadrinhadas \n0) Sair \n"
    opcoes = ['1','2','0']
    opcao = 1
    while not opcao == '0':
        opcao = validaOpcao(opcoes, msg)
        if opcao == '1':
            for i in ongs:
                print(f"Nome da ONG: {i[0]}")
                print(f"Data do próximo evento: {i[1]}")
                print(f"Região do próximo evento: {i[2]}")
                if usuario in i[3]:
                    print("Você já é padrinho!")
                print("-------------------------------------")
        elif opcao == '2':
            for i in ongs:
                if usuario in i[3]:
                    print(f"Nome da ONG: {i[0]}")
                    print(f"Data do próximo evento: {i[1]}")
                    print(f"Região do próximo evento: {i[2]}")
                    print("-------------------------------------")

def menuOng(usuario):
    msg = "1) Visualizar informações \n2) Editar informações \n3) Ver padrinhos \n0) Sair\n"
    opcoes = ['1', '2', '3', '0']
    opcao = 1
    while not opcao == '0':
        opcao = validaOpcao(opcoes, msg)
        if opcao == '1':
            for i in ongs:
                if usuario == i[4]:
                    print(f"Nome da ONG: {i[0]}")
                    print(f"Data do próximo evento: {i[1]}")
                    print(f"Região do próximo evento: {i[2]}")
                    print("-------------------------------------")
        elif opcao == '2':
            for i in ongs:
                if i[4] == usuario:
                    i[0] = input("Informe o nome da sua ONG: \n")
                    i[0] = "Nome da ONG: " + i[0]

                    i[1] = input("Informe quando vai ocorrer o próximo evento: \n")
                    i[1] = "Data do próximo evento: " + i[1]

                    i[2] = input("Informe a região do próximo evento: ")
                    i[2] = "Região do próximo evento: " + i[2]
        elif opcao == '3':
            for i in ongs:
                if i[4] == usuario:
                    quantidade = len(i[3])
                    print(f"Você possui {quantidade} padrinhos.")
                    for padrinhos in i[3]:
                        print(f"Você possui como padrinho: {login[padrinhos]}")


def menuMain(usuario):
        print("Seja bem vindo!")
        tipo = tipoUsuario[usuario]
        match tipo:
            case '1':
                menuPadrinho(usuario)
            case '2':
                menuOng(usuario)




print("Olá! Seja Bem Vindo!")
opcaoSelec = menuInicial()
''' Não encerra enquanto não digitar 0 '''
while opcaoSelec != '0':
    opcaoSelec = menuInicial()