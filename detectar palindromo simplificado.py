frase = str(input('Digite uma frase: '))
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('E um palíndromo')
else:
    print('Não é um palíndromo')
