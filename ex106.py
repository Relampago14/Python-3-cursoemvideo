c = ('\033[1;31m', '\033[0;0m')


def ajuda(h):
    help(h)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'{msg.center(tam)}')
    print('~' * tam)
    print(c[1], end='')


while True:
    titulo('SISTEMA DE AJUDA HELP')
    p = str(input('Digite: ')).strip()
    if p.upper() == 'FIM':
        break
    else:
        ajuda(p)
