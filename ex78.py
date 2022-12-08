valores = []
maior = 0
menor = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c+1}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'Você digitou os valores {valores}')
print(f'O maior número é {maior} na posição ', end='')

for pos, v in enumerate(valores):
    if valores[pos] == maior:
        print(f'{pos+1}', end=' ')
print(f'\nO menor número é {menor} na posição ', end='')

for pos, v in enumerate(valores):
    if valores[pos] == menor:
        print(f'{pos+1}', end=' ')
