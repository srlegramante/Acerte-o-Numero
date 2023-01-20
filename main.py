import random

valor_aleatorio = random.randint(1,10)
acertou = False

while acertou == False:
    chute = int(input('Chute um numero: '))
    if chute > valor_aleatorio:
        print('O chute foi maior do que o valor gerado...')
    elif chute < valor_aleatorio:
        print('O chute foi menor do que o valor gerado...')
    elif chute == valor_aleatorio:
        acertou = True
        print('Você acertou! ')
    else:
        print('Digite um valor valido.')