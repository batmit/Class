from random import randint
comp = randint(0, 10)
vic = 0
while True:
    print('-=-' * 30)
    n = str(input('Digite par ou ímpar: ')).strip().upper()[0]
    while n not in 'PipI':
        n = str(input('Digite par ou ímpar: ')).strip().upper()[0]
    n2 = int(input('Digite um número de 0 a 10: '))
    soma = comp + n2
    print(f'Você jogou {n2} e o computador jogou {comp}')
    print('-=-'*30)
    if n == 'P':
        if soma % 2 == 0:
            print('Você ganhou')
            vic += 1
        else:
            print('Você perdeu')
            break
    else:
        if soma % 2 == 0:
            print('Você perdeu')
            break
        else:
            print('Você ganhou')
            vic += 1
    print('Vamos jogar de novo...')
print('Fim!!!')
if vic != 1:
    print(f'Você ganhou {vic} vezes')
else:
    print(f'Você ganhou {vic} vez')
