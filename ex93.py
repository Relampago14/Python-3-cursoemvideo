# Ficou quase idêntico kkkkkk

dados = {}
gols = []

dados['jogador'] = str(input('Digite o nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))

for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols ele marcou na {c+1}ª partida: ')))

dados['gols'] = gols[:]
dados['total'] = sum(gols)

print('-=' * 25)

print(dados)

print('-=' * 25)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 25)

print(f'O jogador {dados["jogador"]} jogou {partidas} partidas')

for pos, g in enumerate(gols):
    print(f'Na partida {pos+1}, fez {g} gols')

print(f'Foi um total de {dados["total"]} gols')
