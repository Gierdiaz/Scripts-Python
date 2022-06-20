from time import sleep
from random import randint

item = ("PEDRA","PAPEL","TESOURA")
computador = randint(1,3)

print("Suas opções:")
print("""
[1] PEDRA
[2] PAPEL
[3] TESOURA
""")
jogador = int(input("Qual é a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print("-="*11)
print("O SEU ADVERSÁRIO JOGOU {}".format(item[computador]))
print("O JOGADOR JOGOU {}".format(item[jogador]))
print("-="*11)

#Computador jogou Pedra
if computador == 1: 
    if jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("Jogador venceu")
    elif jogador == 3:
        print("Computador venceu")
    else:
        print("Jogada inválida")
      
#Computador jogou Papel
elif computador == 2:
    if jogador == 1:
        print("Computador venceu") 
    elif jogador == 2:
        print("EMPATE") 
    elif jogador == 3:
        print("Jogador venceu")
    else:
        print("Jogada inválida")
      
#Computador jogou Tesoura
elif computador == 3:
    if jogador == 1:
        print("Jogador venceu") 
    elif jogador == 2:
        print("computador venceu")
    elif jogador == 3:
        print("EMPATE") 
    else:
        print("Jogada inválida")
      
