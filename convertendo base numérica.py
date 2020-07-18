n = int(input('Digite um número inteiro: '))
dec = int(input('''Você que converter para:
BINARIO [ 1 ]
OCTAL [ 2 ]
HEXADECIMAL [ 3 ]
: '''))
if dec == 1:
    print(f'{n} convertido para binário fica {bin(n)}')
elif dec == 2:
    print(f'{n} convertido para octal fica {oct(n)}')
elif dec == 3:
    print(f'{n} convertido para hexadecimal fica {hex(n)}')
else:
    print('Opção inválida')
