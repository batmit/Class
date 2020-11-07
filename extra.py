confirm = ''
while confirm != 'S':

    n1 = str (input('Digite seu nome: '))

    n2 = int(input('Digite sua idade: '))

    n3 = str(input("Digite seu sexo: "))

    lista = n1, n2, n3

    print(lista)

    print(f'Seu nome é {lista[0]}')
    print(f"Sua idade é {lista[1]}")
    print(f"Seu sexo é {lista[2]}")
    confirm = str (input('Deseja confirmar[S/N]: ')).strip().upper()[0]