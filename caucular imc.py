peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print(f'Seu IMC foi de :{imc}', end = '')
if imc < 18.5:
    print('Está abaixo do peso')
elif imc <= 25:
    print('Está no peso ideal')
elif imc <= 30:
    print('Você está com sobrepeso')
elif imc <= 40:
    print('Você é obeso')
elif imc > 40:
    print('Você está com obesidade morbida!')
