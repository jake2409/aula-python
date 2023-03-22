"""
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))
d = float(input("Digite o quarto valor: "))

print("1- Você deseja descobrir o maior número?")
print("2- Você deseja descobrir o menor número?")
resp = int(input("Digite a opção desejada: "))

if resp == 1:
    if a > b and a > c and a > d:
        print(f"O primeiro valor {a} é o maior")
    elif b > c and b > d:
        print(f"O segundo valor {b} é o maior")
    elif c > d:
        print(f"O terceiro valor {c} é o maior")
    else:
        print(f"O quarto valor {d} é o maior")
else:
    menor_de_todos = a
    if b < menor_de_todos:
        menor_de_todos = b
    if c < menor_de_todos:
        menor_de_todos = c
    if d < menor_de_todos:
        menor_de_todos = d
    print(f"{menor_de_todos} é o menor de todos")

preco_amaciante = 0.50
print("Lojinha de amaciante!")

qtd_compra = int(input("Quantos amaciantes deseja comprar?"))
is_cadastrado = input("Você é cadastrado? (s/n)")

if qtd_compra >= 100 or is_cadastrado == 's':
    preco_amaciante = 0.35
if qtd_compra >= 100 and is_cadastrado == 's':
    preco_amaciante = 0.30
result = qtd_compra * preco_amaciante
print(f"O valor total da compra é de: {result}!")
i = 0
while i < 10:
    print(i)
    i+=1
"""

