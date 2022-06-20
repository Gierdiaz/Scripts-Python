print("====== DESAFIO 15 ======")

print("O valor do veículo custa 60R$ por dia e é cobrado uma taxa de 0,15₵ por kilometro")
dia = int(input("Por quantos dias o veículo foi alugado? "))
km = int(input("Quantos kilometros percorridos? "))

total = (km*0.15) + (dia*60)
print("O valor a pagar pela aluguel do veículo será de {}R$".format(total))
