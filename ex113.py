red = "\033[1;31m"
reset = "\033[0;0m"


def leiaint(leia):
    while True:
        try:
            num = str(input(leia)).strip()
            return int(num)
        except (ValueError, TypeError):
            print(f'{red} Erro! Digite um número inteiro corretamente. {reset}')
        except KeyboardInterrupt:
            print()
            print(f'{red} O usuário não digitou os números {reset}')
            return 0


def leiareal(leia):
    while True:
        try:
            num = str(input(leia)).strip()
            return float(num)
        except (ValueError, TypeError):
            print(f'{red} Erro! Digite um número real corretamente. {reset}')
        except KeyboardInterrupt:
            print()
            print(f'{red} O usuário não digitou os números {reset}')
            return 0


inteiro = leiaint('Digite um número inteiro: ')
real = leiareal('Digite um número real: ')
print(f'Você digitou o número inteiro {inteiro} e o número real {real}')
