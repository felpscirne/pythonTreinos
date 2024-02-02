def manipula_arquivo():
    caminho = input('Digite o caminho do arquivo: ')
    try: 
        with open(caminho, 'r') as arquivo: conteudo = arquivo.read()
        
        palavras_distintas = set(conteudo.lower().split())
        num_palavras_distintas = len(palavras_distintas)
        print(f'O número de palavras distintas é: {num_palavras_distintas}')

        palavra_antiga = input('Digite uma palavra para substituir no arquivo: ')
        palavra_nova = input('Digite a palavra para por no lugar: ')
        conteudo_novo = conteudo.replace(palavra_antiga, palavra_nova)

        caminho_novo = input('Digite o caminho do novo arquivo ou deixe vazio para sobrescrever: ')
        if caminho_novo == '':
            caminho_novo = caminho
        with open(caminho_novo, 'w') as arquivo_novo:
            arquivo_novo.write(conteudo_novo)

        print('Arquivo modificado com sucesso!')

    except FileNotFoundError:
        print(f'O arquivo "{caminho}" não foi encontrado!')
    except Exception as e:
        print(f'Erro: {e}')
    
manipula_arquivo()