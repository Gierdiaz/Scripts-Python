sexo = str(input("Digite o seu sexo (m = masculino / f = feminino): "))
peso = float(input("Qual é o seu peso atual em(Kg): "))
altura = float(input("Qual é a sua altura atual em(m): "))

imc = peso / (altura**2)

# calcula o valor de peso ideal de acordo com o sexo
if sexo == "m":
    ideal = (altura**2 * 23)
else:
    ideal = (altura**2 * 22)

print(
    "O seu IMC é de {:.1f} e seu peso ideal é {:.1f} Kg"
    .format(imc, ideal)
)

# informa a situação da pessoa
if imc < 18.5:
    print("Você está muito magro")
elif imc <= 24.9:
    print("VOcê  está normal")
elif imc <= 29.9:
    print("Você está com sobrepeso")
elif imc <= 34.9:
    print("Você está obeso grau I")
elif imc <= 39.9:
    print("Você está Obeso grau II")
else:
    print("Você está Obeso grau III ou Mórbido")
