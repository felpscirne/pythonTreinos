from random import randint

resultado=0

jogar = (input("Bem vindo ao sistema de rolagem de dados, digite 0 para sair ou qualquer tecla para continuar \n"))

while jogar != '0':
    
    lado = int(input("Escolha a quantidade de lados do dado: 4, 6, 8, 10, 12, 20 ou 100 \n"))
    
    if lado != 4 and lado != 6 and lado != 8 and lado != 10 and lado != 12 and lado != 20 and lado != 100:
        print("Número inválido, tente novamente\n")
        continue
   
    quantidade = int(input("Quantos dados você quer jogar com essa quantidade de lados? \n"))
    
    soma=0
    for i in range(0, quantidade):
        resultado = randint(1, lado)
        print("O resultado do dado N",i+1," foi: ", resultado, sep="")
        soma+=resultado
    
    print("A soma dos dados foi:",soma)

    jogar = (input("Deseja jogar novamente? Digite 0 para sair ou qualquer tecla para continuar: \n"))

print("Obrigado por jogar, volte sempre!")            
