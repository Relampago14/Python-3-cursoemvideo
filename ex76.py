produtos = 'pão', 2, 'sexo', 0, 'arroz', 9
print('-'*30)
print(f'{"Listagem de preços":^30}')
print('-'*30)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<23}', end='')
    else:
        print(f'R${produtos[pos]:>5.2f}')
