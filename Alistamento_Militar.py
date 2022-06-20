from time import sleep
from datetime import date
atual = date.today().year
nascimento = int(input("Digite o ano em que você nasceu: "))
sleep(2)
idade = atual - nascimento
print("Quem nasceu em {} tem {} anos em {}".format(nascimento,idade,atual))
sleep(2)
if   idade == 18:
     print("Você deve comparecer para se alistar")
     sleep(2)
elif idade < 18:
     print("Ainda está novo para se alistar")
     sleep(2)
elif idade > 18:
     print("Já passou da idade do alistamento")
     sleep(2)

