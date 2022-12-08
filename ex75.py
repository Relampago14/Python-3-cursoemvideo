valores = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')),
           int(input('Digite um valor: ')))
print(f'O algarismo 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O algarismo 3 apareceu pela primeira vez na {valores.index(3)+1}ª posição')
else:
    print(f'O algarismo 3 não apareceu')
print(f'Os algarismos pares foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
