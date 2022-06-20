print("====== DESAFIO 92 ======")

from datetime import datetime

dados = dict()

dados['nome'] = str(input('nome: '))

nasc = int(input("Ano do Nascimento: "))

dados['idade'] = datetime.now().year -  nasc

dados['CTPS'] = int(input("Carteira de Trabalho: "))

if dados['CTPS'] != 0:
    dados['contratação'] = int(input("Ano de Contratação: "))
    dados['salário'] = float(input("Salário: R$ "))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print("-"*22)
for k, v in dados.items():
    print(f' - {k}: {v}')
print("-"*22)   
print(dados)


