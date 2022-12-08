# Ficou um pouco diferente a linha de pensamento em algumas partes, porém funciona igual :p

dados = dict()
gols = list()
gols_individual = list()
jogadores = list()

while True:

    dados['jogador'] = str(input('Digite o nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))

    for c in range(0, partidas):
        gols_marcados = int(input(f'Quantos gols {dados["jogador"]} fez na {c + 1}ª partida? '))
        gols_individual.append(gols_marcados)
        gols.append(gols_marcados)

    dados['gols'] = gols_individual[:]
    jogadores.append(dados.copy())
    gols_individual.clear()

    while True:

        p = str(input('Quer continuar? S/N ')).upper()[0]

        if p in 'SN':
            break
        print('Erro! Responda apenas S ou N: ')

    if p == 'N':
        break
print(f'Nº  Nome      gols        Total')
print('-' * 31)

for k, v in enumerate(jogadores):
    print(f'{k + 1:<4}', end='')
    for d in v.values():
        print(f'{str(d):<8}', end='')
print(f'{sum(gols):>6}')
print('-' * 31)

while True:

    # Como algumas pessoas não sabem que o python começa pelo '0', eu diminuo em um o valor de n para a lista ser
    # acessada corretamente

    n = int(input('Mostrar dados de qual jogador? (999 interrompe): '))

    if n - 1 in range(0, len(jogadores)):
        print(f'Analisando dados de {jogadores[n - 1]["jogador"]}')
        for pos in range(0, len(jogadores[n - 1]['gols'])):
            print(f'Na partida {pos + 1} ele fez {jogadores[n - 1]["gols"][pos]} gols')
    elif n == 999:
        break
