casa=float(input("Valor da Casa ou do Terreno: "))
salario=float(input("Salário do Comprador: "))
anos=float(input("Quantos anos de gostaria de pagar? "))

prestacao=casa/(anos*12)
minimo=salario*50/100

print("Para pagar uma casa de R${:.2f} em {:.1f} anos".format(casa, anos), end="")

print(" a prestação será de R${:.2f}".format(prestacao))

print("Comparando tem que pagar {:.2f} e o mínimo é de {:.2f}".format(prestacao, minimo))
if prestacao <= minimo:
    print("Empréstimo pode ser concedido")

else:
    print("Empréstimo negado.")
