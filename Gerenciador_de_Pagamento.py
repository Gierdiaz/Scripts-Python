print("{:=^40}".format("Loja Brasil"))

preco = float(input("Digite o valor a ser pago pelo produto: R$"))

print("""      FORMAS DE PAGAMENTO:
      [1] À vista no dinheiro/cheque
      [2] À vista no cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão

      """)
#Formas de pagamento      
opcao = int(input("Qual é a opção desejada? "))

if opcao == 1:
   total = preco - (preco * 10/100)

elif opcao == 2:
    total = preco - (preco * 5/100)
    
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f}".format(parcela))

elif opcao == 4:
    total = preco + (preco * 20/100)
    totaldeparcelas = int(input("Quantas parcelas: "))
    parcela = total / totaldeparcelas
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(totaldeparcelas, parcela))                       

#Esse print vai acontecer sempre
print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preco, total))
