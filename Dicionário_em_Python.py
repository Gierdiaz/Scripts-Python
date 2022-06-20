print("====== DESAFIO 90 ======")

aluno = dict()

aluno['nome'] = str(input('nome: '))

aluno['média'] = float(input(f'média do {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'

elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'

else:
    aluno['situação'] = 'Reprovado'

for  k, v in aluno.items():
    print(f'- {k} = {v}')
