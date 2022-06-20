print("""
[1] Adição
[2] Subtração
[3] Multiplicação
[4] Divisão

Escolha a opção da tabuada:""")
a = int(input())
if a == 1:
    print("Adição")
    b = int(input("Escolha um número para o cálculo: "))
    for count in range(0 , 11, 1):
        print(b, "+", count, "=", (b+count))
elif a == 2:
    print("Subtração")
    b = int(input("Escolha o número para o cálculo: "))
    for count in range(0, 11, 1):
        print(b, "-", count, "=", (b-count))
elif a == 3:
    print("Multiplicação")
    b = int(input("Escolha um número para o cálculo: "))
    for count in range(0, 11, 1):
        print(b, "x", count, "=", (b*count))
elif a == 4:
    print("Divisão")
    b = int(input("Escolha o número para o cálculo: "))
    for count in range(0, 11, 1):
        print(b, "/", count, "=","{:.2f}".format(count/b))
