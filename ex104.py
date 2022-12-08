# Minha resposta:

def leiaint(leia):
    red = "\033[1;31m"
    reset = "\033[0;0m"
    while True:
        num = str(input(leia)).strip()
        if not num.isnumeric():
            print(f'{red} Erro! Você não digitou um algarismo. {reset}')
        else:
            return num


n = leiaint('Digite um número: ')
print(f'Você digitou {n}')
