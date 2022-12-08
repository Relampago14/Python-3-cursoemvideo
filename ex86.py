# Um poquinho diferente, fiz tempestade em copo d'água kkkkk

l1 = [[], [], []]
l2 = [[], [], []]
l3 = [[], [], []]

for c in range(0, 9):
    valor = int(input('Digite um valor: '))
    if c <= 2:
        l1[c].append(valor)
    elif 2 < c <= 5:
        l2[c-3].append(valor)
    elif 5 < c <= 8:
        l3[c-6].append(valor)
print(f'[{l1[0][0]:^5}] [{l1[1][0]:^5}] [{l1[2][0]:^5}]')
print(f'[{l2[0][0]:^5}] [{l2[1][0]:^5}] [{l2[2][0]:^5}]')
print(f'[{l3[0][0]:^5}] [{l3[1][0]:^5}] [{l3[2][0]:^5}]')
