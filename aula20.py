"""def mostralinha():
    print('-' * 3)


mostralinha()
print('Boa')
mostralinha()
print('Bom')
mostralinha()
print('Bem')
mostralinha()"""

"""def mensagem(msg):
    print('-' * 30)
    print(msg)


mensagem('Sexo')
mensagem('Aoba')

print('-' * 30)"""

"""def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma é igual a {s}')


soma(4, 5)
soma(b=8, a=9)
soma(2, 1)
"""

"""def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e ao todo são {tam} números.')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
"""


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
