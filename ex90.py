aluno = {'nome': str(input('Digite o nome do aluno: ')), 'média': float(input('Digite a média do aluno: '))}

if aluno['média'] >= 6:
    aluno['situação'] = 'aprovado'
elif 6 > aluno['média'] >= 5:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'

for k, v in aluno.items():
    print(f'{k} recebe {v}')

# Foi oq eu fiz porém apliquei poucos conceitos vou deixar o código comentado

"""aluno = {'nome': str(input('Digite o nome do aluno')), 'média': int(input('Digite a média do aluno:'))}

if aluno['média'] >= 6:
    print(f'O aluno {aluno["nome"]} tem média {aluno["média"]:.1f} e está aprovado')
elif 6 > aluno['média'] >= 5:
    print(f'O aluno {aluno["nome"]} tem média {aluno["média"]:.1f} e está de recuperação')
else:
    print(f'O aluno {aluno["nome"]} tem média {aluno["média"]:.1f} e está reprovado')"""

