# Ficou um pouco diferente mas eu fiz funcionar igual :)

l1 = [[], [], []]
l2 = [[], [], []]
l3 = [[], [], []]
pares = []

for c in range(0, 9):
    valor = int(input('Digite um valor: '))
    if c <= 2:
        l1[c].append(valor)
    elif 2 < c <= 5:
        l2[c-3].append(valor)
    elif 5 < c <= 8:
        l3[c-6].append(valor)
    if valor % 2 == 0:
        pares.append(valor)

print(f'[{l1[0][0]:^5}] [{l1[1][0]:^5}] [{l1[2][0]:^5}]')
print(f'[{l2[0][0]:^5}] [{l2[1][0]:^5}] [{l2[2][0]:^5}]')
print(f'[{l3[0][0]:^5}] [{l3[1][0]:^5}] [{l3[2][0]:^5}]')
print(f'A soma dos números pares é {sum(pares)}')
print(f'A soma dos valores da terceira {l1[2][0] + l2[2][0] + l3[2][0]}')
print(f'O maior valor da segunda linha é {max(l2)[0]}')
