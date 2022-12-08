# Acho que meu código ficou mais polido com relação à resolução

from ex108 import moeda

p = float(input('Digite o preço: R$ '))
print(f'O valor é R$ {moeda.moeda(p)} e a metade é R$ {moeda.metade(p)}')
print(f'A dobro do valor é R$ {moeda.dobro(p)}')
print(f'Aumentando em 10% fica igual à R$ {moeda.aumento(p)}')
print(f'Diminuindo em 13% fica igual à R$ {moeda.dimunuir(p)}')
