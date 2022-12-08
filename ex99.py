# Ficou muito diferente, mas eu acho que o comando do exercício foi satisfeito

from random import randint

num = list()


def numeros(m):
    print('-=' * 20)
    print('Os valores recebidos foram: ', end='')
    for n in m:
        print(f'{n}', end=' ')
    print()
    if len(m) > 0:
        print(f'O maior valor da lista é {max(m)}')
    else:
        print(f'Não há número nenhum na lista')


# Ao invés de predefinir valores, deixei que a máquina sorteasse os valores para mim

for v in range(0, 5):
    for c in range(0, randint(0, 9)):
        num.append(randint(0, 9))
    numeros(num[:])
    num.clear()
