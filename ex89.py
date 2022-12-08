# Um pouco diferente mas funciona :p

alunos = []
dado = list()

while True:

    dado.append(str(input('Digite o nome do aluno: ')))
    dado.append((float(input('Digite a nota do aluno: '))))
    dado.append((float(input('Digite a nota do aluno: '))))

    alunos.append(dado[:])
    dado.clear()
    p = str(input('Quer continuar? S/N: '))

    if p not in 'Ss':
        break

print('No. Nome        Média')
print('-' * 22)

for v in range(0, len(alunos)):
    print(f'{v+1:<3} {alunos[v][0]:<11} {(alunos[v][1] + alunos[v][2]) / 2:>5.1f}')

while True:

    n = int(input('Mostrar notas de qual aluno? 999 interrompe: '))

    if n-1 in range(0, len(alunos)):
        print(f'{alunos[n-1][0]} {alunos[n-1][1:]}')
    elif n == 999:
        print(f'Finalizado')
        break
