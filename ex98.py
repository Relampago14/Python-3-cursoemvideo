# Fiz através do for e funciona da mesma forma

from time import sleep


def contador(a, b, c):
    print('-=' * 20)
    if c < 0:
        c = -c
    print(f'Contagem de {a} até {b} de {c} em {c}.')
    if c == 0:
        c = 1
    if a > b:
        if c > 0:
            c = -c
    for v in range(a, b, c):
        print(f'{v}', end=' ')
        sleep(0.3)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
