print("="*20)
print("10 TERMOS DE UMA PA")
print("="*20)

term = int(input("Primeiro termo da PA: "))
raz = int(input("Razão da PA: "))
dec = term + (10-1)*raz
for count in range(term, dec + raz, raz):
    print("{}".format(count), end=" ")

