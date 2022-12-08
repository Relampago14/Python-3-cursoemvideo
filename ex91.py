from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
rank = []

for c in range(0, 4):
    jogadores[f'Jogador {c+1}'] = (randint(1, 6))

for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)

rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for pos, v in enumerate(rank):
    print(f'{pos+1}º lugar: {v[0]} com {v[1]} pontos')