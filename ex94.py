# Ta aí minha resposta espero que ajude

dados = dict()
lista = list()
idade = list()
mulheres = list()
velhos = list()

while True:

    dados['nome'] = str(input('Digite o nome da pessoa: '))

    while True:
        sexo = str(input('Digite o sexo da pessoa: '))

        if sexo in 'Mm' 'Ff':
            dados['sexo'] = sexo
            if sexo in 'Ff':
                mulheres.append(dados['nome'])
            break
        print('Por favor, digite apenas F ou M')

    dados['idade'] = int(input('Digite a idade da pessoa: '))
    idade.append(dados['idade'])

    lista.append(dados.copy())

    p = str(input('Quer continuar? S/N '))

    if p in 'Nn':
        media = sum(idade) / len(idade)

        print(f'A) Ao todo tem {len(lista)} pessoas')

        print(f'B) A média de idade é {media:.2f} anos')

        print(f'C) As mulheres cadastradas foram: ', end=' ')
        # Fiz mecanismo que põe ponto final apenas no último nome e vírgula nos demais.

        for pos, m in enumerate(mulheres):
            if pos + 1 == len(mulheres):
                print(f'{m}.')
            else:
                print(f'{m},', end=' ')

        print(f'D) As pessoas que estão acima da média são: ')
        for v in lista:
            if v['idade'] > media:
                velhos.append(v)
        # Fiz um if que verifica se a chave corresponde a idade, se for ele pula a linha e segue com o laço

        for i in velhos:
            for k, v in i.items():
                if k == 'idade':
                    print(f'{k} = {v}.')
                else:
                    print(f'{k} = {v};', end=' ')
        break

    while p not in 'Ss' 'Nn':

        print('Por favor digite apenas S ou N')
        p = str(input('Quer continuar? S/N '))
