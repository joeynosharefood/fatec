def armario():
    itens = list()
    answer = list()
    totalItens = int(input('Insira o total de itens: '))
    consultas = int(input('Insira o total de consultas: '))
    for c in range(totalItens):
        itens.append(int(input('Insira o item que Mindinho possui: ')))
    for c in range(consultas):
        consulta = int(input('Insira a Consulta desejada: '))
        if consulta in itens:
            answer.append('S')
        else:
            answer.append('N')
    for c in answer:
        print(c)
armario()