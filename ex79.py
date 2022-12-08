valores = []

valores.append((int(input('Digite um valor: '))))

while True:

    pergunta = str(input('Deseja continuar? S/N '))

    if pergunta in 'Ss':
        add = (int(input('Digite um valor: ')))
        if add in valores:
            print('Esse resultado já foi inserido. Tente novamente')
        else:
            valores.append(add)
    else:
        print(sorted(valores))
        break

