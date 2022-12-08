def titulo(t):
    print(('-' * 40))
    print(t.center(40))
    print('-' * 40)


def opções(op):
    while True:
        print()
        titulo('MENU PRINCIPAL')
        print('\033[1;32m1 - Ver pessoas cadastradas')
        print('2 - Cadastrar uma pessoa')
        print('3 - Fechar o sistema\033[0;0m')
        try:
            p = int(input(op))
            if p == 1:
                titulo('PESSOAS CADASTRADAS')
                with open('lista.json', 'r') as file:
                    for linha in file:
                        print(f'{linha}', end='')
            elif p == 2:
                titulo('NOVO CADASTRO')
                nome = str(input('Digite o nome: '))
                while True:
                    idade = str(input('Digite a idade: '))
                    if idade.isnumeric():
                        with open('lista.json', 'a') as file:
                            file.write(f'{nome}')
                            file.write(f' \t \t \t \t \t \t{idade} anos\n')
                            print(f'Novo registro de {nome} adicionado com sucesso!')
                        break
                    else:
                        print('\033[1;31mDigite corretamente a idade.\033[0;0m')
            elif p == 3:
                titulo('VOLTE SEMPRE')
                break
            else:
                print('\033[1;31mOpção inválida, tente novamente.\033[0;0m')
        except ValueError:
            print('\033[1;31mOpção inválida, tente novamente.\033[0;0m')
