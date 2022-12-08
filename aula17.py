"""lanche = ['a', 'b', 'c']
lanche.append('d')
lanche.insert(0, 'z')
lanche.remove('z')
lanche.pop()
if 'd' in lanche:
    lanche.remove('e')
else:
    print(lanche)"""

"""valores = [2, 1, 2, 3, 2, 6, 2, 4, 2]
for v in valores:
    if 2 in valores:
        valores.remove(2)
print(valores)"""


# valores.sort(reverse=True)
# print(len(valores))

"""valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for pos, v in enumerate(valores):
    print(f'Na posição {pos+1} encontrei o valor {v}!')
print('Terminei')
"""

a = [1, 2, 3]
b = a[:]
b[1]= 'facil'

print(a)
print(b)