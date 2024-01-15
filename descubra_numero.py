from random import randint

def adivinhe_pc(x):
    minimo = 1
    maximo = x
    resposta = ''
    print(f'Pense em um número de 1 a {x}.')
    
    while resposta != 'c':
        if minimo != maximo:
            palpite = randint(minimo, maximo)
        else:
            palpite = minimo
        resposta = input(f'O número {palpite} é muito alto (A), muito baixo (B) ou correto (C)?\n').lower()
        if resposta == 'a':
            maximo = palpite - 1
        elif resposta == 'b':
            minimo = palpite + 1
    
    print(f'Booa! O número era {palpite}.')

adivinhe_pc(1000)

print ('Agora é contigo, adivinhe o aleatorio')

def adivinhe_usuario(x):
    aleatorio = randint(1, x)
    palpite = 0

    while palpite != aleatorio:
        palpite = int(input(f'Qual o seu palpite? (1 a {x})\n'))
        if palpite < aleatorio:
            print ('Muito baixo, tente outra vez.')
        elif palpite > aleatorio:
            print ('Muito alto, tente outra vez.')
    
    print(f'Booooa! O número era {aleatorio}.')

adivinhe_usuario(1000)