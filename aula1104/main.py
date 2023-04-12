quantidade_items = 300
def menu():
    print("======================================================")
    print("=                                                    =")
    print("=             Seja bem vindo ao Semaphore            =")
    print("=                    Menu principal                  =")
    print("= 1)Deseja ver o estoque?                            =")
    print("= 2)Deseja realizar uma compra?                      =")
    print("= 3)Deseja realizar seu cadastro?                    =")
    print("= 0)Deseja sair do sistema?                          =")
    print("=                                                    =")
    print("======================================================")
    opcao = input("Escolha a opção desejada: ")
    valido = False
    while not valido:
        if opcao.isnumeric():
            opcao = int(opcao)
            if opcao >= 0 and opcao <= 3:
                valido = True
                continue

        print("Escolha uma opção válida!!")
        opcao = input("Escolha a opção desejada: ")
    return opcao

def estoque():
    print("Bem vindo ao estoque!")
    print(f"No estoque temos {quantidade_items}")
    opcao_estoque = int(input("Digite um valor"))
    while opcao_estoque != 0:
        print("Ainda no estoque")
        opcao_estoque = int(input("Digite um valor novamente"))

opcao_escolhida = menu()
while opcao_escolhida != 0:
    match opcao_escolhida:
        case 1:
            estoque()
        case 2:
            compra()
        case 3:
            cadastro()
    opcao_escolhida = menu()

print("Obrigado. Até a próxima!")
'''
plt.plot(tempo, a, "r", label = "Pop A")
plt.plot(tempo, b, "b", label = "Pop B")
plt.ylabel("Número de habitantes")
plt.xlabel("tempo")
plt.legend()
plt.grid()
plt.show()
#pip install matplotlib
'''