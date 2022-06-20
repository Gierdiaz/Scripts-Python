n1=float(input("Informe sua primeira nota: "))
n2=float(input("Informe sua segunda nota: "))
m=(n1+n2)
print("Sua média final foi: {:.1f}".format(m))
if m <= 14:
    print("Sua nota está abaixo da média. Você está em recuperação.")
else:
    print("Parabéns! Você conseguiu bater a média e está aprovado.")
