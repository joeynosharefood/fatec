def sopaLetras ():
    words = list()
    verifyArray = list()
    wordArray = list()
    word = str(input('Insira a palavra: '))
    while True:
        verify = True if len(word) < 100 else False
        if verify == False:
            print('Insira uma palavra valida!')
            word = str(input('Insira a palavra: '))
        elif verify == True:
            break
    for c in range(len(word)):
        wordArray.append(word[c])
    for c1 in range(10):
        words.append(str(input(f'Insira a palavra de nª {c1+1}: ')))
    for c2 in words:
        test = len(c2)
        for c3 in range(len(c2)):
            test = test - 1 if c2[c3] in wordArray else test 
        verifyArray.append('OK' if test == 0 else '-1')
    for c4 in verifyArray:
        print(c4)
sopaLetras()