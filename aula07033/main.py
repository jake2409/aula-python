valor_amaciante = float(input("Qual o valor do amaciante ?"))
valor_desconto  = float(input("Qual o valor do desconto ?"))

valor_desconto = valor_desconto/100

valor_descontado = valor_amaciante * valor_desconto

valor_total = valor_amaciante - valor_descontado




print(f"O valor total do amaciante é {valor_total}\nE o valor descontado é {valor_descontado}")
