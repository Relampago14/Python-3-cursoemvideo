# Meu código, paciência sou iniciante ainda kkkkk

listas = []
dado = []
pesados = [0, 0]
leves = [0, 0]
total = 1

dado.append(str(input('Nome da pessoa: ')))
dado.append(float(input('Peso dessa pessoa: ')))
listas.append(dado[:])
dado.clear()

while True:

    p = str(input('Deseja continuar? S/N '))

    if p in 'Ss':
        dado.append(str(input('Nome da pessoa: ')))
        dado.append(float(input('Peso dessa pessoa: ')))
        listas.append(dado[:])
        dado.clear()
        total += 1
        for n in listas:
            if n[1] >= pesados[0]:
                if n[1] == pesados[0]:
                    if n[0] not in pesados:
                        pesados.append(n[0])
                else:
                    pesados.clear()
                    pesados.append(n[1])
                    pesados.append(n[0])

            elif n[1] >= leves[0]:
                if n[1] == leves[0]:
                    if n[0] not in leves:
                        leves.append(n[0])
                else:
                    leves.clear()
                    leves.append(n[1])
                    leves.append(n[0])
    else:
        print(f'O total de pessoas é {total}')
        print(f'O maior peso foi {pesados[0]:.1f} de {pesados[1:]}')
        print(f'O menor peso foi {leves[0]:.1f} de {leves[1:]}')
        break
