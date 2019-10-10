def winterIsComing():
    #variaveis 
    habit = list()
    answer = 0
    #inputs
    cidades = int(input('Insira o nº de cidades: '))
    estradas = int(input('Insira o nº estradas que ligam duas cidades: '))

    for c in range(cidades):
        habit.append(int(input(f'Insira o nº de habitantes da cidade {c+1} ')))
    for c1 in range(estradas):
        cidadeA = int(input('Insira a primeira cidade: '))
        cidadeB = int(input('Insira a segunda cidade: '))
    #algo
        total = habit[cidadeA-1] + habit[cidadeB-1]

        if total > answer:
            answer = total

    return answer
print(winterIsComing())