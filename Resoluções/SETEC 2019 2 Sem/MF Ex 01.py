def pergaminho():
    total = 0
    
    multas = int(input('Insira o numero de mutas: '))
    for c in range(multas):
        sol = int(input('Insira o numero de sóis: '))
        pontos = int(input('Insira os pontos: '))
        if sol < 365:
            total += pontos
    if total >= 20:
        return 'G'
    else:
        return 'N'
print(pergaminho())