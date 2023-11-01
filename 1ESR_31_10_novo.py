def raiz_binaria(num,precisao):
    inicio = 0
    fim = num
    chute = (inicio + fim)/2
    while abs(chute**2 - num) > precisao:
        if chute**2 > num:
            fim = chute
        else:
            inicio = chute
        chute = (inicio+fim)/2
    return chute

def raiz_binaria_recursiva(num,precisao,inicio,fim):
    chute = (inicio + fim)/2
    if abs(chute**2 - num) > precisao:
        if chute**2 > num:
            fim = chute
        else:
            inicio = chute
        return raiz_binaria_recursiva(num,precisao,inicio,fim)
    return chute
def checa_numero():
    num = input("Diga um numero : ")
    while not num.isnumeric():
        num = input("Diga um numero : ")
    return num
def checa_numero_recursivo():
    num = input("Diga um numero : ")
    if not num.isnumeric():
        return checa_numero()
    return num
def printa_dicionario(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dicionario(dic[key])
        else:
            print(dic[key])
    return
def acha_indice(num,inicio,fim,lista):
    indice_chute = (inicio+fim)//2
    if lista[indice_chute] != num:
        if lista[indice_chute] > num:
            fim = indice_chute
        else:
            inicio = indice_chute
        return acha_indice(num,inicio,fim,lista)
    return indice_chute
def quicksort(lista):
    if len(lista)<=1:
        return lista
    else:
        pivo = lista[0]
        menores = [elem for elem in lista if elem < pivo]
        maiores = [elem for elem in lista if elem > pivo]
        menores_ordenados = quicksort(menores)
        maiores_ordenados = quicksort(maiores)
        print(menores,pivo,maiores)
        return menores_ordenados + [pivo] + maiores_ordenados
lista = [4,2,6,1,7,0,3]
print(quicksort(lista))



import json
with open('teste.json','r') as teste:
    teste = json.load(teste)
    print(teste.keys())


