maior = 0
manor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p} pessoa: '))
    if p == 1:                                      # o primeiro é considerado o maior e o menor ao mesmo tempo
        maior = peso
        menor = peso
    else:                                                # se o segundo for maior passa para o segundo e repete tudo novamente
        if peso > maior:                                 # se o segundo for maior que o maior ele passa a ser o menor e repete
            maior = peso
            maior = peso
        if menor < peso:                                 # se o segundo passa a ser o menor que o menor ele passa a ser o menor
            meior = peso                                      
print(f'O maior foi {maior} e o menor foi {menor}')
