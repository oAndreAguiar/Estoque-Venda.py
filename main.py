import pandas as pd

def pesquisar_produto_csv(file_path, termo_pesquisa):
    df = pd.read_csv(file_path)
    resultado = df[df['nome'].str.contains(termo_pesquisa, case=False)]
    return resultado

def exportar_dict_para_csv(dicionario, nome_arquivo):
        df = pd.DataFrame.from_dict(dicionario)    
        df.to_csv(nome_arquivo, index=False)


print('Seja Bem-vindo ao seu gerenciador!\nEscolha uma opção')
print('1. Estoque\n2. Venda')

comando_entrada = int(input('Digite o comando: '))



if comando_entrada == 1:
    print('ESTOQUE')
    print('1.Cadastrar produto\n2.Pesquisar\n3.Exportar\n4.Voltar')
    comando_estoque = int(input('Escolha uma opção:'))
elif comando_entrada == 2:
    print('VENDA')
    print('1. Criar venda\n2.Editar produto\n3.Precificar\n4.Voltar')
    comando_venda = int(input('Escolha uma opção:'))

if comando_estoque == 1:
    estoque = {}
    estoque_nome = []
    estoque_quantidade = []
    estoque_valor = []
    estoque_descricao = []
    while True:
        nome_produto = input('Digite o nome: ')
        estoque_nome.append(nome_produto)
        estoque['nome'] = estoque_nome

        quantidade_produto = int(input('Digite a quantidade: '))
        estoque_quantidade.append(quantidade_produto)
        estoque['quantidade'] = estoque_quantidade

        valor_produto = float(input('Digite o valor: '))
        estoque_valor.append(valor_produto)
        estoque['valor'] = estoque_valor

        descricao_produto = str(input('Digite a descrição: '))
        estoque_descricao.append(descricao_produto)
        estoque['descricao'] = estoque_descricao

        comando_cadastro = int(input('digite 1 para cadastrar mais um item ou 0 para sair'))

        if comando_cadastro == 0:
            estoque = pd.DataFrame.from_dict(estoque)
            exportar_dict_para_csv(estoque,'estoque.csv')
            print(estoque)
            break 
        elif comando_cadastro == 1:
            pass
elif comando_estoque == 2:
    df_estoque = pd.read_csv('estoque.csv')

    termo_pesquisa = input('Digite o termo de pesquisa: ')
    resultado_pesquisa = pesquisar_produto_csv('estoque.csv', termo_pesquisa)

    if not resultado_pesquisa.empty:
            print(resultado_pesquisa)
    else:
        print('Nenhum resultado encontrado.')
elif comando_estoque == 3:
    exportar_dict_para_csv(meu_dict, 'output.csv')

elif comando_estoque == 4:
    pass