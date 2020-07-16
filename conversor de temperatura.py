n = float(input('\033[mDigite o valor em celcios: \033[m'))
fa = ((n * 9) / 5) + 32
print(f'O valor em Fahrnheit é : {fa:.2f}')
if n <= 20:
    print('\033[1;34;46mQue frio...\033[m')
else:
    print('\033[1;31;47mQue calor\033[m')
