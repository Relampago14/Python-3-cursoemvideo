# Dado
# Mudou um pouco, porém funciona da mesma forma

def leiadinheiro(din):
    while True:
        valor = str(input(din))

        if valor.replace(',', '').replace('.', '').isdigit():
            valor = valor.replace(',', '.')
            return float(valor)

        print(f'\033[1;31m"{valor.strip()}" não é um número!\033[0;0m')
