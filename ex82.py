lista = []
par = []
impar = []

lista.append(int(input('Digite um numero: ')))

while True:
    p = input('Deseja continuar? S/N ')

    if p in 'Ss':
        lista.append(int(input('Digite um numero: ')))
    else:
        for n in lista:
            if n % 2 == 0:
                par.append(n)
            else:
                impar.append(n)
        print(f'A lista é {lista}')
        print(f'A lista par é {par}')
        print(f'A lista impar é {impar}')
        break
