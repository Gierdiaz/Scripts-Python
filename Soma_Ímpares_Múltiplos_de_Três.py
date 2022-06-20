soma = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 == 0: #se a divisão por c for 3 dando resto 0
       soma = soma + c
       cont = cont + 1
print("O somatório de {} valores entre os números ímpares que são múltiplos de três são {}".format(cont,soma))
