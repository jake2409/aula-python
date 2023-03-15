'''
print("Olá. Seja bem vindo!!")

print("--------Menu Principal----------")
print("1-Cadastrar novo produto")
print("2-Ver estoque")
print("3-Lista de promoções")
print("4-Sair")

escolha = float(input("Digite um número para escolher uma opção :"))

if escolha == 1:
    print("Você escolheu o cadastro!")
elif escolha == 2:
    print("Você escolheu o estoque!")
elif escolha == 3:
    print("Você escolheu a lista de promoções!")
elif escolha == 4:
    print("Obrigado por usar o nosso sistema.")
else:
    print("Opção escolhida não existe.")

letra_digitada = input("Digite uma letra :")

if letra_digitada == "a" or letra_digitada == "e" or letra_digitada == "i" or letra_digitada == "o":
    print("Você escolheu uma vogal!")
else:
    print("Você escolheu uma consoante!")
0,3 reprovado
4,5 exame
6, 10 aprovado


nota_a = int(input("Digite o valor da nota A de 0 a 10: "))
nota_b = int(input("Digite o valor da nota B de 0 a 10: "))

if (nota_a < 0 or nota_a > 10) or (nota_b < 0 or nota_b > 10):
    print("Uma das notas informadas é invalida")
else:
    media = (nota_a + nota_b)/2

    if media < 4:
        print("Reprovado")
    elif media < 6:
        print("Exame")
    else:
        print("Aprovado")

print("Você deseja conhecer a minha calculadora?")
resposta = input("Digite 's' para sim ou 'n' para finalizar.")

if resposta == "s":
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    print("Por favor, escolha a operação de acordo com o menu")
    operacao = input("Digite + para realizar uma soma\nDigite - para realizar subtração")
    if operacao == "+":
        print(f"O total da operação é: {valor1 + valor2}")
    elif operacao == "-":
        print(f"O total da operação é: {valor1 - valor2}")
    else:
        print("Operação informada não corresponde com as opções")
else:
    print("Tchau")

'''

valor1 = float(input("Digite o primeiro número: "))
valor2 = float(input("Digite o segundo número: "))
valor3 = float(input("Digite o terceiro número: "))

if valor1 > valor2 or valor1 > valor3:
    print(f"O primeiro valor {valor1} é o maior entre os três valores")
elif valor2 > valor3:
    print(f"O segundo valor {valor2} é o maior entre os três valores")
else:
    print(f"O terceiro valor {valor3} é o maior entre os três valores")