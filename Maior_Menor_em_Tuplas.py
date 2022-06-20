from time import sleep
from random import randint

print("====== DESAFIO 74 ======")
sleep(2)

print("Sorteio de 5 números de 1 a 10.\nConsegue adivinhar qual combinação será formada?")
sleep(5)

#sorteio com Tuplas.
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

#end="" para os valores permanecerem na mesma linha no print.
print("Os valores sorteados foram: ", end="")
for n in numeros:
   print(f"{n} ", end="")
   sleep(2)

#\n para pular de linha. Sempre muito importante.
print(f"\nO maior valor sorteado foi {max(numeros)}")
sleep(2)

print(f"O menor valor sorteado foi {min(numeros)}")
sleep(2)
