def fatorial(f, show=""):
    """
        -> Essa função mostra o fatorial do número desejado.
    :param f: Número desejado.
    :param show: Variável booleana para mostrar a expressão ou não (opcional)
    :return: retorna o valor do fatorial do número f
    """
    n = 1
    for v in range(f, 0, -1):
        n *= v
        if show:
            if v == 1:
                print(f'{v} = ', end='')
            else:
                print(f'{v} x ', end='')
    return n


print(f'{fatorial(5, True)}')
print()
help(fatorial)
