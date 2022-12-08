# Fiz diferente mas acho q a solução do Guanabara ficou melhor


def metade(preço=0, show=False):
    preço /= 2
    return preço if show is False else moeda(preço)


def dobro(preço=0, show=False):
    preço *= 2
    return preço if show is False else moeda(preço)


def aumento(preço=0, show=False):
    dez_por_cento = 0.1 * preço
    preço = dez_por_cento + preço
    return preço if show is False else moeda(preço)


def dimunuir(preço=0, show=False):
    treze_por_cento = 0.13 * preço
    preço = preço - treze_por_cento
    return preço if show is False else moeda(preço)


def moeda(preço=0):
    return f'{preço:.2f}'.replace('.', ',')
