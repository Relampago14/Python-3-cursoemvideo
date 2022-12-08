# Adicionei uma if que confere se a contribuição não vai ultrapassar o limite da idade de aposentadoria

from datetime import date

dados = dict()

dados['nome'] = str(input('Digite o nome da pessoa: '))
nascimento = int(input(f'Digite o ano em que {dados["nome"]} nasceu: '))
dados['idade'] = date.today().year - nascimento
dados['número da carteira de trabalho'] = int(input(f'Digite o número da carteira de trabalho: '))

if dados['número da carteira de trabalho'] != 0:
    dados['contratado'] = int(input(f'Digite o ano em que {dados["nome"]} foi contratado: '))
    dados['salário'] = int(input(f'Digite o salário de {dados["nome"]}: '))
    contribuicao = dados['idade'] + 35

    if contribuicao < 65:
        dados['aposentadoria'] = contribuicao
    else:
        dados['aposentadoria'] = 65

print('-=' * 30)

for k, v in dados.items():
    print(f'O {k} recebe {v}')
