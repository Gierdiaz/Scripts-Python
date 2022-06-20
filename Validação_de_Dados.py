sexo = "F" and "M"

sexo = str(input("Digite o sexo: ")).strip().upper()[0] #pega só a primeira letra

while sexo not in "F" and "M":
    if sexo != "F" and sexo != "M":
        sexo = input("Sexo não registrado. Digite novamente: ").strip().upper()[0]
print("Sexo {} registrado".format(sexo))
