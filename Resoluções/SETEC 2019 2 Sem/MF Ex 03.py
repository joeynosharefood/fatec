def caixa():
    total = 0
    contagem = list()
    meses = int(input('Insira o Total de meses: '))
    interv = int(input('Insira o intervalo de meses: '))
    for c in range(meses):
        contagem.append(int(input(f'Insira as moedas do mês {1+c}: ')))
    contagem.sort(reverse = True)
    for c in range(interv):
        total += contagem[c]
    return total
print(caixa())  