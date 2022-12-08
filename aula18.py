"""teste = []
galera = []

teste.append('João')
teste.append('17')
galera.append(teste[:])
teste[0] = ('Maria')
teste[1] = ('19')
galera.append(teste[:])

print(galera)"""

"""galera = [['João', 17], ['Maria', 19], ['Ana', 42]]

for p in galera:
    print(f'{p[0]} tem {p[1]} anos.')"""

galera = []
dado = []
totmai = 0
totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append((int(input('Idade: '))))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] > 18:
        print(f'{p[0]} é idoso com {p[1]} anos')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade com {p[1]} anos')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores')
