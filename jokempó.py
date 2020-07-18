rom random import randint
from time import sleep
n = int(input('Pedra[0]\nPapel[1]\nTesoura[2]\n:'))
xo = sleep(2)
com = randint(0, 2)
print('-=-' * 20)
if n == 0:
  print('Você jogou pedra')
  if com == 0:
    print('O computador jogou pedra')
    print('Empate')
  elif com == 1:
    print('O computador jogou papel')
    print('Você perdeu')
  elif com == 2:
    print('O computador jogou tesoura')
    print('Você ganhou')
elif n == 1:
  print('Você jogou papel')
  if com == 0:
    print('O computador jogou pedra')
    print('Você ganhou')
  elif com == 1:
    print('O computador jogou papel')
    print('Empate')
  elif com == 2:
    print('O computador jogou tesoura')
    print('Você perdeu')
elif n == 2:
  print('Você jogou tesoura')
  if com == 0:
    print('O computador jogou pedra')
    print('Ele venceu')
  elif com == 1:
    print('O computador jogou papel')
    print('Você venceu ')
  elif com == 2:
    print('O computador jogou tesoura')
    print('Empate')
print('-=-' * 20)
