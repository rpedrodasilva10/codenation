import csv
# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
#


def q_1():
    players = []
    with open('/home/dark/codenation/python-1/data.csv', 'r') as arquivo:
        conteudo = csv.DictReader(arquivo, delimiter=',')
        for row in conteudo:
            nacionalidade = row['nationality']
            if nacionalidade not in players:
                players.append(row['nationality'])
    return players.__len__()
    pass

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    clubs = []
    with open('/home/dark/codenation/python-1/data.csv', 'r') as arquivo:
        conteudo = csv.DictReader(arquivo, delimiter=',')
        for row in conteudo:
            club = row['club']
            if club not in clubs:
                clubs.append(row['club'])
    return clubs.__len__()
    pass

# **Q3.** Liste o primeiro nome dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    names = []
    with open('/home/dark/codenation/python-1/data.csv', 'r') as arquivo:
        conteudo = csv.DictReader(arquivo, delimiter=',')
        for row in conteudo:
            # name = row['full_name'],['name']
            if names.__len__() < 20:
                names.append(row['full_name'])
    return names
    pass

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    bestpaid = []
    answer = []
    with open('/home/dark/codenation/python-1/data.csv', 'r') as arquivo:
        conteudo = csv.DictReader(arquivo, delimiter=',')
        for row in conteudo:
            info = row['full_name'], float(row['eur_wage'])
            bestpaid.append(info)
    bestpaid = sorted(bestpaid, key=lambda bestpaid: bestpaid[1], reverse=True)
    cont = 0
    for x in bestpaid:
        if cont < 10:
            cont = cont + 1
            answer.append(x[0])
    return answer
# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    older = []
    anwser = []
    with open('/home/dark/codenation/python-1/data.csv', 'r') as arquivo:
        conteudo = csv.DictReader(arquivo, delimiter=',')
        for row in conteudo:
            info = row['full_name'], row['age']
            older.append(info)
    older = sorted(older, key=lambda older: older[1], reverse=True)
    cont = 0
    for x in older:
        if cont < 10:
            cont = cont + 1
            anwser.append(x[0])
    return anwser
    pass

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    ages = {}
    with open('/home/dark/codenation/python-1/data.csv', 'r') as arquivo:
        conteudo = csv.DictReader(arquivo, delimiter=',')
        for row in conteudo:
            value = int(row['age'])
            if value in ages.keys():
                ages[int(value)] = int(ages[value]) + 1
            else:
                ages[int(value)] = 1
    return ages
    pass
