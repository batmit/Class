import random
no = random.randint(0, 5)
n = float(input('Eu irei pensar em um número de o a 5. Tente adivinhar: '))
if no == n:
    print('Acertou!')
else:
    print('Errrou')
