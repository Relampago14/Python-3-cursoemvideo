from datetime import date


def voto(v):
    idade = date.today().year - v
    if idade < 16:
        estado = 'NÃO VOTA'
        return estado
    elif 16 <= idade < 18 or idade > 65:
        estado = 'VOTO é OPCIONAL'
        return estado
    else:
        estado = 'VOTO é OBRIGATÓRIO'
        return estado


situacao = voto(int(input('Digite o ano em que você nasceu: ')))
print(f'Estado: {situacao}')
