'''
So saia do loop se o que o usuário digitar for númerico
'''

def validaNumerosEConverte(vlr):
    while not vlr.isnumeric():
        print("Valor digitado não é numerico.")
        vlr = input("Digite valores numericos:")
    return int(vlr)

vlrs = input("Digite valores numericos:")

vlrs = validaNumerosEConverte(vlrs)

print(vlrs)

