"""dados = {'nome': 'Pedro', 'idade': 25}
dados['sexo'] = 'M'
del dados['idade']

print(dados)"""

filme = {'título': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}

"""print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')"""

locadora = [filme]

print(locadora[0]['ano'])

"""pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 88

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())"""

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'Rj'}
estado2 = {'uf': 'São Paulo', 'sigla': 'Sp'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
