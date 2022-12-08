from random import randint

jogos = int(input('Digite quantos jogos serão sorteados: '))

print(f'Sorteando {jogos} jogos')

for v in range(jogos):
    num = []
    while len(num) != 6:
        n = randint(0, 60)
        if n not in num:
            num.append(n)
    print(f'Jogo {v+1}: {sorted(num)}')
