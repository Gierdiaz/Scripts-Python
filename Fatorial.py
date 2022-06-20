#from math import factorial 
n = int(input("Calcule o seu fatorial "))
#f = factorial(n)
f = 1
c = n
#print("O fatorial de {} é {}".format(n, f))
print("Calculando {}! = ".format(n), end= "")
while c > 0:
    print("{}".format(c), end= "")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print("{}".format(f))
