again = ''
while again != 'N':
    números = ('Zero', "Um", 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quize', 'Desseseis', 'Desessete', 'Desoito', 'Dezenove', 'Vinte')

    n1 = int(input("Digite um número de 0 a 20: "))

    if n1 > 20:
        n1 = int(input("Tente novamente, digite um número de 0 a 20: "))

    print(números[n1])

    again = str(input("Tentar novamente?: ")).strip().upper()[0]