import random
def dracarys():
    #declações
    rank = list()
    nomes = dict()
    dracarys = 0
    #inputs
    sug = int(input('Insira o nº de sugestões: '))
    for c in range(sug):
        influs = int(input('Insira a influencia: '))
        suges = str(input('Insira o sugestão de nome: '))
    #condições
        if 0 < influs and influs < 100 and len(suges) < 20 and suges[-1] == 'l' and suges[-2] == 'a':
            if influs in nomes:
                tempInflu = (random.randint(-5, 5) + influs)
                nomes[tempInflu] = suges
                rank.append(tempInflu)
            else:
                nomes[influs] = suges
                rank.append(influs)
    rank.sort(reverse = True)
    if len(rank) == 0:
        print('Dracarys!')
    else:
        for c in rank:
            print(nomes[c])
dracarys()