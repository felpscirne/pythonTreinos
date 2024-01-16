import random

print('Bem vindo ao jogo de pedra, papel e tesoura!')
def jogar():
    escolha = input('Escolha entre papel, pedra ou tesoura.\n').lower()
    computador = random.choice(['papel', 'pedra', 'tesoura'])

    if escolha not in ['papel', 'pedra', 'tesoura']:
        return('Escolha inválida.')
    
    print(f'O computador escolheu {computador}.')

    if escolha==computador:
        return('Empate!')
    
    if ganhou(escolha, computador):
        return('Você ganhou!')

    return('Você perdeu!')

def ganhou(jogador, computador):
    if (jogador == 'papel' and computador == 'pedra') or (jogador == 'pedra' and computador == 'tesoura') or (jogador == 'tesoura' and computador == 'papel'):
        return True

continuar = 's'
while continuar == 's':
    print(jogar())
    continuar = input('Deseja jogar novamente? (s/n)\n').lower()
    if continuar == 'n':
        print('Obrigado por jogar, volte sempre!')
        break
    elif continuar != 's':
        print('Opção inválida, encerrando o jogo.')
        break