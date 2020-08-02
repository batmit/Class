while True:
    irineu = 1
    print('*' * 30)
    n1 = float(input('Digite um valor: '))
    print('*' * 30) 
    if n1 < 0:
        break
    while irineu <= 10:
        print(f'{n1} vezes {irineu} = {n1 * irineu}')
        irineu += 1
print('Fim!!!', end=' ')
