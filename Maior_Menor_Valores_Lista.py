v = []
for cont in range(0,5):
    v.append(int(input("Informe 5 valores: ")))
print(f"Os números digitados na lista são: {v}\n", end=" ")


print(f"\nO maior valor digitado  da lista foi: {max(v)} na posição {v.index(max(v))}")


print(f"O menor valor digitado da lista foi: {min(v)} na posição {v.index(max(v))}")


