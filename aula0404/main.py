'''
Gabriel Aparecido Cassalho Xavier
rm99794
'''
print("Bem Vindo á Vinheria Agnello")
idade = int(input("Em que ano você nasceu?"))
endereco = input("Qual o seu endereço?")
anoAtual = 2023
idade = anoAtual - idade

if idade > 18:
    prcVinhoUm = 120
    prcVinhoDois = 100
    prcVinhoTres = 80
    vlrFreteGratis = 100
    vlrFrete = 20


    print("Temos as opções dos seguintes vinhos:")
    print(f"1- Rose da casa no valor de R${prcVinhoUm},00.")
    print(f"2- Suave de mesa da casa no valor de R${prcVinhoDois},00.")
    print(f"3- Vinho tinto da casa no valor de R${prcVinhoTres},00.")

    vinhoUm = int(input("Quantos vinhos da opção 1(Rose da casa), você deseja?")) * prcVinhoUm
    vinhoDois = int(input("Quantos vinhos da opção 2(Suave de mesa da casa), você deseja?")) * prcVinhoDois
    vinhoTres = int(input("Quantos vinhos da opção 3(Vinho tinto da casa), você deseja?")) * prcVinhoTres

    if vinhoUm > 0 or vinhoDois > 0 or vinhoTres > 0:
        valorTotal = vinhoUm + vinhoDois + vinhoTres

        if valorTotal >= vlrFreteGratis:
            print("Sua compra deu mais de R$100,00. O frete sai totalmente grátis.")
        else:
            valorTotal += vlrFrete

        print("Obrigado por comprar com a gente.")
        print(f"O valor total da sua compra foi de R${valorTotal}.")
        print(f"E será entregue no endereço: {endereco}")
    else:
        print("Você não escolheu nenhum vinho. Volte sempre!")

else:
    print("Não é permitido a venda para menores de idade.\nMas não esqueça da gente quando for mais velho!")
