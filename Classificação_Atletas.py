from datetime import date
atual = date.today().year
nasc = int(input("Digite o ano do seu nascimento: "))
idade = atual - nasc
print("O atleta que nasceu no ano de {} tem {} anos.".format(nasc, idade))
if idade <= 9:
   print("Classificação: Mirim")
elif idade <= 14:
   print("Classificação: Infantil")
elif idade <= 19:
   print("Classificação: Junior")
elif idade <= 20:
   print("Classificação: Sênior")
elif idade >= 20:
  print("Classificação: Master")
