quantidade_items = 300
endereco_cli = ''
num_casa_cli = 0
preco_semaforo = 500

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


def estoque(endereco_cli, num_casa_cli, quantidade_items):
    print("======================================================")
    print("=                                                    =")
    print("=                 Bem vindo ao estoque!              =")
    print(f"No estoque temos {quantidade_items} semáforos disponivéis!")
    print("= 1) Deseja realizar uma compra?                     =")
    print("= 2) Deseja voltar ao menu principal?                =")
    print("=                                                    =")
    print("======================================================")
    opcao_estoque = input("Escolha a opção desejada: ")
    valido = False
    while not valido:
        if opcao_estoque.isnumeric():
            opcao_estoque = int(opcao_estoque)
            if opcao_estoque >= 1 and opcao_estoque <= 2:
                valido = True
                continue
        print("Escolha uma opção válida!!")
        opcao_estoque = input("Escolha a opção desejada: ")
    if opcao_estoque == 1:
        return compra(endereco_cli, num_casa_cli, quantidade_items)





def compra(endereco_cli, num_casa_cli, quantidade_items):
    print("======================================================")
    print("=                                                    =")
    print("=               Bem vindo ao setor de compras!       =")
    print("======================================================")

    qtd_compra = input("Quantos semáforos você deseja?")
    while not qtd_compra.isnumeric() or int(qtd_compra) > quantidade_items:
        print("Valor informado não corresponde a um número ou quantidade indisponível no estoque.")
        print(f"Atualmente temos {quantidade_items} semáforos disponivéis no estoque.")
        qtd_compra = input("Quantos semáforos você deseja comprar?")

    qtd_compra = int(qtd_compra)

    if endereco_cli == "":
        print("Você ainda não realizou um cadastro.")
        endereco = cadastro(endereco_cli)
        endereco_cli = endereco[0]
        num_casa_cli = endereco[1]
    

    total_pagar = qtd_compra * preco_semaforo
    print(f"Você quer comprar {qtd_compra} semáforos.")
    print(f"Que deveram ser entregues no endereço {endereco_cli}, número {num_casa_cli}.")
    print(f"Sua compra deu um total de R${total_pagar},00.")

    print("=============================================================")
    print("=                                                           =")
    print("= Ainda não temos pagamento on-line.                        =")
    print("= Mas o nosso entregador pode levar a maquininha até você.  =")
    print("= 1) Deseja realizar o pagamento no crédito?                =")
    print("= 2) Deseja realizar o pagamento no débito?                 =")
    print("= 3) Deseja realizar o pagamento no dinheiro?               =")
    print("=                                                           =")
    print("=============================================================")
    forma_pgmt = input("Escolha a opção desejada: ")
    valido = False
    while not valido:
        if forma_pgmt.isnumeric():
            forma_pgmt = int(forma_pgmt)
            if forma_pgmt >= 1 and forma_pgmt <= 3:
                valido = True
                continue
        print("Escolha uma opção válida!!")
        forma_pgmt = input("Escolha a opção desejada: ")
    
    
    if forma_pgmt == 3:
        print("Você escolheu a opção dinheiro. Deseja troco?")
        troco = input("Se sim, troco pra quanto? Se não digite N.")
        while not troco.isnumeric() and troco != 'N':
            print("Opção digitada está invalida!")
            print("Você escolheu a opção dinheiro. Deseja troco?")
            troco = input("Se sim, troco pra quanto? Se não digite N.")
        if troco.isnumeric():
            troco = int(troco) - total_pagar
            print(f"Ótimo. Nosso entregador levará R${troco},00 de troco.")
        else:
            print("Compra realizada com sucesso! Seu pedido logo chegará até você.")
    
    quantidade_items -= qtd_compra
    return [endereco_cli, num_casa_cli, quantidade_items]





def cadastro(endereco_cli):
    print("======================================================")
    print("=                                                    =")
    print("=                Bem vindo ao cadastro!              =")
    if endereco_cli != '':
        print("= Você já se cadastrou!                              =")
        print("======================================================")
        return
    print("======================================================")
    endereco_cli = input("Qual o endereço de entrega?")
    while endereco_cli == "":
        print("Campo não pode ser vazio.")
        endereco_cli = input("Qual o endereço de entrega?")

    num_casa_cli = input("Qual o número da casa?")
    while not num_casa_cli.isnumeric():
        print("Valor informado para número da casa inválido. Por favor, digite somente números!")
        num_casa_cli = input("Qual o número da casa?")

    print("Obrigado pelas informações!")
    return [endereco_cli, num_casa_cli]




opcao_escolhida = menu()
while opcao_escolhida != 0:
    match opcao_escolhida:
        case 1:
            endereco = estoque(endereco_cli, num_casa_cli, quantidade_items)
        case 2:
            endereco = compra(endereco_cli, num_casa_cli, quantidade_items)
        case 3:
            endereco = cadastro(endereco_cli)
    if endereco:
        endereco_cli = endereco[0]
        num_casa_cli = endereco[1]
        quantidade_items = endereco[2]
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