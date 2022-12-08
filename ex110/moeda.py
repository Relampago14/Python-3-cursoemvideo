# Não mudou quase nada kkkkkk


def metade(preço=0, show=False):
    preço /= 2
    return preço if show is False else moeda(preço)


def dobro(preço=0, show=False):
    preço *= 2
    return preço if show is False else moeda(preço)


def aumento(preço=0, a=0, show=False):
    por_cento = (a/100) * preço
    preço = por_cento + preço
    return preço if show is False else moeda(preço)


def dimunuir(preço=0, r=0, show=False):
    por_cento = (r/100) * preço
    preço = preço - por_cento
    return preço if show is False else moeda(preço)


def moeda(preço=0):
    return f'{preço:.2f}'.replace('.', ',')


def resumo(preço, a=0, r=0):
    print('-' * 30)
    print('RESUMO DO PREÇO'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \tR$ {moeda(preço)}')
    print(f'Dobro do preço:  \tR$ {dobro(preço, True)}')
    print(f'Metade do preço: \tR$ {metade(preço, True)}')
    print(f'{a}% de aumento:  \tR$ {aumento(preço, a, True)}')
    print(f'{r}% de redução:  \tR$ {dimunuir(preço, r, True)}')
