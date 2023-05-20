'''
fazer um sistema com login;
criar uma conta
esquecer senha
criar um menu main
criar as opções de traçar rota; escolher semaforo
'''
login = []
senha = []
opcaoMenuIncial = ['1','2','3','0']

def validaOpcao(opcoes,msg):
    opcao = input(msg)
    while opcao not in opcoes:
        print("Digite uma opção válida!")
        opcao = input(msg)
    return opcao

def menuInicial():
    msg = "1) Fazer login \n2) Ainda não tem cadastro? \n3) Esqueci a senha \n0) Sair\n"
    opcao = validaOpcao(opcaoMenuIncial, msg)
    match opcao:
        case '1':
            menuLogin()
        case '2':
            criarConta()
        case '3':
            esqueciSenha()
    return opcao

def menuLogin():
    loginUsuario = input("Informe seu login: \n")
    print(login)
    print(senha)
    while loginUsuario not in login:
        print("Login informado é invalido.")
        loginUsuario = input("Informe seu login: \n")
    senhaUsuario = input("Informe sua senha: \n")
    while senhaUsuario not in senha:
        print("Login informado é invalido.")
        loginUsuario = input("Informe seu login: \n")


def criarConta():
    print("Bem vindo ao cadastro!")
    login.append(input("Informe um código de login: \n"))
    senha.append(input("Informe a sua senha: \n"))


def esqueciSenha():
    print("Bora recuperar sua conta?")
    loginUsuario = input("Informe o login que deseja recuperar a conta: \n")
    while loginUsuario not in login:
        print("Login informado não existe na base de dados!")
        loginUsuario = input("Informe um login valido para recuperar sua conta: \n")

    for i in range(len(login)):
        if login[i] == loginUsuario:
            print(f"A senha para o login informado é {senha[i]}")
            break


    
print("Olá! Seja bem vindo ao sistema de controle de tráfego.")
opcaoSelec = menuInicial()
while opcaoSelec != '0':
    menuInicial()
