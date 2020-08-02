n1 = str(input('Digite uma frase: ')).strip().upper()
palavras = n1.split()                             # tudo junto
junto = ''.join(palavras)                         # tudo junto e grande
inverso = ''                                      # ele não tem um valor definido
for frase in range(len(junto) -1, -1, -1):        # len é a última: ele pega a última e vai ao contrário
    inverso = inverso + junto[frase]              # como frase somente aceita número o inverso pega os números e os convertem em letras usando o exemplo da própria palavras
print(f'O inverso de {junto} é {inverso}')        # já foi convertido e está fora da repetição
if junto == inverso:                              
    print('Esse é um palíndromo')
else:
    print('Esse não é um palíndromo')
