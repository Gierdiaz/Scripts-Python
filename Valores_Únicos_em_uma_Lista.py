num = list()
while True:
    k = int(input("Digite um valor: "))
    if k not in num:
            num.append(k)
            print("Valor adicionado")
    else:
        print("Valor duplcado não é adicionado")

    answer = str(input("Deseja continuar a adicionar nº? [S/N] ")).strip().upper()[0]
    while answer not in "NS":
        answer = str(input("Digite [S/N]: ")).strip().upper()[0]
        if answer in "N":
            break
num.sort()
print(f"Sua lista é {num}")
