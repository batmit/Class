d = 0
n = int(input('Digite um número inteiro: '))
for c in range(1, n + 1):
    if n % c == 0:
        d = d + 1
        print('\033[31m',c)
    else:
        print('\033[34m', c)
        print('\033[m')
if d == 2:
    print('\nEle é primo')
else:
    print('\nEle não é primo')
