#organizando por "import" e "from X import"

import os
from random import randint
from time import sleep

# limpa o terminal alter do início de execução do programa
import os


# Aqui nós colocamos o laço de execução uma vez que o objetivo é repetir esse programa
jogando = True
while jogando:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\033[1mOlá, gostaria de jogar um pouco? XD\033[m")

    print("-=-"*20)
    print("\033[1mVocê consegue adivinhar em qual número entre 0 e 2 devo estar pensando agora...\033[m] \U0001F4AD")
    print("-=-"*20)
    sleep(5)

    # faz eu pensar em um número aleatório.
    eu = randint(0,2) 
    jogador = int(input("\033[1;35mE ai, em qual número eu estou pensando? \033[m \U0001F60F "))
    
    print("\033[1;36mHmmm...\033[m \U0001F914")
    sleep(2)
 
    if jogador == eu:
        print("\033[1;36mVocê adivinhou o número, mizeravi kkk. Parabéns!\033[m \U0001F604")
        sleep(5)
    else:
        print("\033[1;36mPoxa, você errou! Eu pensei no número {} e você digitou o número {}.\033[m \U0001F635".format(eu, jogador))
        sleep(5)
    # aqui nós precisamos guardar a resposta do jogador
    resp = str(input("\033[1;35mQuer tentar novamente?\033[m "))
 
    # sim deve ser uma string
    if resp == "sim":
        print("\033[1;36mCerto, Vamos tentar de novo então!\033[m \U0001F4AA")
        sleep(3)
    else:
        print("\033[1;36mOk, nos vemos na próxima!\033[m \U0001F44B")
        sleep(3)
    # nós mudamos o valor de jogando de acordo com a resposta do jogador
    jogando = resp == "sim"