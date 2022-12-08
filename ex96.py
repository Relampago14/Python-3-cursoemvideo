def metragem(l, c):
    area = l * c
    print(f'A área de um terreno de {l}m * {c}m é igual a {area}m²')


metragem(float(input('Digite o comprimento do terreno: ')), float(input('Digite a largura do terreno: ')))
