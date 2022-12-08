lista = [[], []]

for c in range(0, 7):
    pergunta = (int(input(f'Digite o {c+1}º valor: ')))
    if pergunta % 2 == 0:
        lista[0].append(pergunta)
    else:
        lista[1].append(pergunta)
print(f'Os números pares digitados foram {sorted(lista[0])}')
print(f'Os números ímpares digitados foram {sorted(lista[1])}')
