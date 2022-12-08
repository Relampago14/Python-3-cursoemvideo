"""x = 0
print(x)
"""

"""n = int(input('Num: '))
print(n)
"""

"""a = int(input(' '))
b = int(input(' '))
r = a / b
print(r)
"""

"""r = 2 / '2'
print(r)"""

"""lst = [3, 6, 4]
print(lst[3])
"""

"""import uteis
print(uteis)"""

try:
    a = int(input(' '))
    b = int(input(' '))
    r = a / b
except Exception as erro:
    print(f'O problema encontrado foi {erro}')
else:
    print(f'{r}')
finally:
    print('Volte sempre')
