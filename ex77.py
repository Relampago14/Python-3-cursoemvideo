palavras = ('pudim', 'arroz', 'cachorro', 'perereca')
for v in palavras:
    print(f'\nNa palavra {v} temos ', end='')
    for letra in v:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
