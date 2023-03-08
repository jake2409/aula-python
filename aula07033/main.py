'''
valor_amaciante = float(input("Qual o valor do amaciante ?"))
valor_desconto  = float(input("Qual o valor do desconto ?"))

valor_desconto = valor_desconto/100
valor_descontado = valor_amaciante * valor_desconto

valor_total = valor_amaciante - valor_descontado

print(f"O valor total do amaciante é {valor_total}\nE o valor descontado é {valor_descontado}")

a = 2
b = 3
c = a

a = b
b = c

a = 2
b = 3

a ,b = b, a #somente no python isso funcionaria
print(a,b)

a = 1
b = 2.0
c = "gabriel"
d = true
e = false
f = none

#operadores lógicos >, >=, <, <=, ==, !=, and, or, not, in


salario = float(input("Diga seu salario : "))

if salario>10000:
    print("Bom salario")
elif(salario>5000):
    print("Regular")
else:
    print("Ruim")
'''

salario = float(input("Diga seu salario : "))
resposta = "Isento"

if salario >= 4664.68:
    reposta = "27,5%"
elif salario >= 3751.06:
    resposta = "22,5%"
elif salario >= 2826.66:
    resposta = "15%"
elif salario >= 1903.99:
    resposta = "7,5%"


print(resposta)