while True:
    print("-" * 30 )
    print('{:.^40}'.format('Banco Daniel'))
    print('-' * 30 )
    valor = int(input('Digite um valor a ser retirado do caixa: '))
    cedula = 100
    total = valor
    totalcedula = 0
    while True:
        if total >= cedula:
            total -= cedula
            totalcedula += 1
        else:
            if totalcedula > 0:
                print(f'{totalcedula} de {cedula}')
            totalcedula = 0
            if cedula == 100:
                cedula = 50
            if cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 1
            elif total == 0:
                break
    print("-=-" * 30)
    n3 = str(input('Deseja fazer outro saque?: ')).strip().upper()[0]
    if n3 == 'N':
        break
