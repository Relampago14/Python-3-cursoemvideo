# Funções

def metade(preço=0):
    preço /= 2
    preço = f'{preço:.2f}'.replace('.', ',')
    return preço


def dobro(preço=0):
    preço *= 2
    preço = f'{preço:.2f}'.replace('.', ',')
    return preço


def aumento(preço=0):
    dez_por_cento = 0.1 * preço
    preço = dez_por_cento + preço
    preço = f'{preço:.2f}'.replace('.', ',')
    return preço


def dimunuir(preço=0):
    treze_por_cento = 0.13 * preço
    preço = preço - treze_por_cento
    preço = f'{preço:.2f}'.replace('.', ',')
    return preço


def moeda(preço=0):
    return f'{preço}'.replace('.', ',')
