soma = 0
media = 0
nomevelho = ''
maior = 0
totmulher20 = 0

for pessoa in range(1,4): 
    print("---- {}ª PESSOA ----".format(pessoa))
    nome = str(input("NOME: ")).strip()
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO: ")).strip()
    soma = soma + idade
    if pessoa == 1 and sexo in "MasculinomasculinoMm":
        maior = idade
        nomevelho = nome
    if sexo in "MasculinomasculinoMm" and idade > maior:
        maior = idade
        nomevelho = nome
    if sexo in "FemininofemininoFf" and idade < 20:
        totmulher20 += 1

media = soma/pessoa
print("A média da idade do grupo é {} anos ".format(media))
print("O homem mais velho tem {} anos e se chama {}".format(maior, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))
