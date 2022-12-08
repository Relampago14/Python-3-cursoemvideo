valores = []

for c in range(0, 5):
    add = int(input('Digite o seu valor: '))
    if c == 0 or add > valores[-1]:
        valores.append(add)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if add <= valores[pos]:
                valores.insert(pos, add)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados foram {valores}')
