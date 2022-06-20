from datetime import date
atual = date.today().year

totalmaior = 0
totalmenor = 0

for pessoas in range(1, 4):
    nascimento = int(input("Digite o ano em que a {}º pessoa nascimento: ".format(pessoas)))
    idade = atual - nascimento
    print("Tem {} anos".format(idade))
    if idade > 20:
        totalmaior += 1
    else:
        totalmenor += 1
print("Tivemos {} pessoas maiores de idade e {} pessoas menores de idade".format(totalmaior, totalmenor))
