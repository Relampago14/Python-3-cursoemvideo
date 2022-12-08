# Não precisei usar o return e mudei as médias um pouco

dic = dict()


def notas(*n, sit=False):
    """
        -> Função a qual analisa as notas dos alunos e mostra o total de notas, a maior nota, a menor nota, a média e
           a situação da turma (opcional)
    :param n: São as notas dos alunos.
    :param sit: É a situação dos alunos (opcional)
    :return: Não há retorno
    """
    dic['total'] = len(n)
    dic['maior nota'] = max(n)
    dic['menor nota'] = min(n)
    if sit:
        dic['média'] = (sum(n) / (len(n)))
        if dic['média'] < 6:
            dic['situação'] = 'Ruim'
        elif 8 > dic['média'] >= 6:
            dic['situação'] = 'Pode melhorar'
        elif dic['média'] >= 8:
            dic['situação'] = 'Excelente!'
    else:
        dic['média'] = (sum(n) / len(n))


notas(5.5, 9.5, 10, 6.5, sit=True)
print(dic)
