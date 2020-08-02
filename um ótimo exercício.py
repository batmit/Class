valor = quaint = baa = 0
names = ' '
panela = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    cont = ' '
    n1 = float(input('Digite o preço do produto em reais: '))
    valor = valor + n1
    if n1 >= 1000:
        quaint = quaint + 1
    panela += 1
    if panela == 1:
        names = nome
        baa = n1
    if n1 < baa:
        names = nome
        baa = n1
    while cont not in 'SN':
        cont = str(input('Deseja continuar? ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Você gastou no final {valor}')
print(f'Ao todo {quaint} produtos custaram mais de 1000 reais.')
print(f'O produto mais barato custou: {baa} reais e seu nome era: {names}')
