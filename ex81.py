numeros = []

numeros.append(int(input('Digite um valor: ')))

while True:

    p = input('Você deseja continuar? S/N ')

    if p in 'Ss':
        add = numeros.append(int(input('Digite um valor: ')))
    else:
        print(f'Você digitou {len(numeros)} números')
        print(f'Os valores em ordem decrescente são {sorted(numeros, reverse=True)}')
        if 5 in numeros:
            print(f'O valor 5 está na lista')
        else:
            print(f'O valor 5 não está na lista')
        break
