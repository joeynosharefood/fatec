def figurinhas ():
    album = list()
    figSSTotal = list()
    
    dimAlbum = int(input('Insira o total de figurinhas no album: '))
    figCarimbadas = int(input('Insira o total de figurinhas carimbadas: '))
    figCompradas = int(input('Insira o total de figurinhas compradas: '))
    
    for c in range(figCarimbadas):
        figSSTotal.append(int(input('Insira as figurinhas carimbadas: ')))
    for x in range(figCompradas):
        fig = int(input('Insira as figurinhasc compradas: '))
        if fig in figSSTotal:
            figSSTotal.remove(fig)
            figCarimbadas -= 1

    return figCarimbadas

print(figurinhas())