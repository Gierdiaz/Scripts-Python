n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo vlaor: "))

opcao = 0

while opcao != 5:

    print("""
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    """)
    opcao = int(input("Qual é a sua opção?: "))
    if opcao == 1:
        soma = n1 + 2
        print("A soma entre {} + {} = {}".format(n1, n2, soma))
        
    elif opcao == 2:
        produto = n1 * n2
        print("O produto entre {} x {} = {}".format(n1, n2, produto))
        
    elif opcao == 3:
        if  n1 > n2:
            maior = n1
        elif n2 >= n1:
            maior = n2
        print("Entre {} e {} o maior valor é {}".format(n1, n2, maior))

    elif opcao == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo vlaor: "))

    elif opcao == 5:
        print("Finalizando...")
          
        
    else:
        print("Opção inválida. Tente novamente.")
    print("=-="*10)

print("Fim do programa. Volte Sempre!")
