from ex109 import moeda

p = float(input('Digite o preço: R$ '))
print(f'O valor é R$ {moeda.moeda(p)} e a metade é R$ {moeda.metade(p, True)}')
print(f'A dobro do valor é R$ {moeda.dobro(p, True)}')
print(f'Aumentando em 10% fica igual à R$ {moeda.aumento(p, False)}')
print(f'Diminuindo em 13% fica igual à R$ {moeda.dimunuir(p)}')
