
num = (int(input("Informe o primeiro número: ")),
       int(input("Informe o segundo número: ")),
       int(input("Informe o terceiro número: ")),
       int(input("Informe o quarto número: ")))
print(f"Você digitou {num}")



#{num.count(9)}
print(f"O valor 9 apareceu {num.count(9)} vezes")

#{num.index(3)+1}
print(f"O valor 3 apareceu na {num.index(3)+1}ª posição")
print("Os valores pares digitados foram ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")

