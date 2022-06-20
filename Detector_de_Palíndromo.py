frase = str(input("Digite uma frase: ")). strip().upper()
#strip serve para eliminar espaços antes e depois.
#upper serve para deixar as letras maiúsculas.

palavras = frase.split()
#separou em um vetor, lista.
junto = "".join(palavras)
#juntou tudo em uma string só.
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
#len diz a quantidade de elementos de um.
#aqui foi feito a inversão no for.
    inverso = inverso + junto[letra]
if inverso == junto:
    print("Temos um palíndromo")
else:
    print("A frase digitada não é um palíndromo")
print("O inverso de {} é {}".format(junto, inverso))
