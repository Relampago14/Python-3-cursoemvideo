# Ao invés de criar uma variável para somar os pares, criei uma lista.

from random import randint

valores = list()
pares = list()

print('Sorteando os valores: ', end='')


def sorteia(s):
    print(f'{s}', end=' ')
    valores.append(s)


def somapar(sp):
    print()
    for v in sp:
        if v % 2 == 0:
            pares.append(v)
    print(f'A soma dos valores pares de {sp} é {sum(pares)}')


for c in range(0, 5):
    sorteia(randint(0, 9))

somapar(valores)
