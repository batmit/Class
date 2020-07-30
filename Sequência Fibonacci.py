fib = int(input('Digite a quantidade de termos que deseja que seja mostrado na sequencia fibonnaci: '))
n = 0
v1 = 0
v2 = 1
print('0 - 1', end ='-')
while n < fib:
    v3 = v1 + v2
    print(f' {v3} ', end = '-') 
    v1 = v2
    v2 = v3
    n = n + 1
print('  Fim')
