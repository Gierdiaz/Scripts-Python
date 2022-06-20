soma = 0
cont = 0
for count in range(1, 7):
    num = int(input("Digite o {}º valor: ".format(count)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print("Você informou {} números PARES e a soma é {}".format(cont, soma))
