import csv

def manipula_arquivo():
    caminho = input('Digite o caminho do arquivo: ')
    try: 
        with open(caminho, newline='') as arquivo_csv: 
            leitor_csv = csv.reader(arquivo_csv, delimiter=',')
            cabecalho = next(leitor_csv)
            dados = [linha for linha in leitor_csv]
            
        return cabecalho, dados, caminho
    
    except FileNotFoundError:
        print(f'O arquivo "{caminho}" não foi encontrado!')
    except Exception as e:
        print(f'Erro: {e}')
    
def exibir_conteudo(cabecalho, dados):
    print(f'{", ".join(cabecalho)}')
    for linha in dados:
        print(f'{", ".join(linha)}')
        
def calculo_valor_total(dados):
    total_geral = 0
    for linha in dados:
        preco = float(linha[1])
        quantidade = int(linha[2])
        total_produto = preco * quantidade
        total_geral += total_produto
        print(f'Produto: {linha[0]}, tem total em estoque de: R$ {total_produto:.2f}')
    print(f'Total geral em estoque: R$ {total_geral:.2f}')

def adiciona_dados(dados):
    novo_produto = []
    novo_produto.append(input("Insira o Nome do Produto: "))
    novo_produto.append(input("Insira o Preço: "))
    novo_produto.append(input("Insira a Quantidade em Estoque: "))
    dados.append(novo_produto)
    print('Produto adicionado com sucesso!')

def salva_arquivo(caminho, cabecalho, dados):
    with open(caminho, 'w', newline='') as modificado_csv:
        escritor_csv = csv.writer(modificado_csv)
        escritor_csv.writerow(cabecalho)
        escritor_csv.writerows(dados)
        print('Arquivo modificado com sucesso!')
            

cabecalho, dados, caminho = manipula_arquivo()
exibir_conteudo(cabecalho, dados)
calculo_valor_total(dados)

while True:
    if input('Deseja adicionar um novo produto? (s/n) ').lower() == 's':
        adiciona_dados(dados)
        calculo_valor_total(dados)
        salva_arquivo(caminho, cabecalho, dados)
    else: break
   

        


        
        
        
