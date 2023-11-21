import pandas as pd

print('Seja Bem vindo ao seu gerenciador!\n Escolha uma opção')
print('1.Estoque \n 2.Venda')

comando__entrada = int(input('Digite o comando:'))

if comando__entrada == 1:
    print('ESTOQUE')
    print('1.Cadastrar produto\n2.Pesquisar\n3.Exportar\n4.Voltar')
    comando__estoque = input('Escolha uma opção:')
elif comando__entrada == 2:
    print('VENDA')
    print('1. Criar venda\n2.Editar produto\n3.Precificar\n4.Voltar')
    comando__venda = input('Escolha uma opção:')

if comando__estoque == 1:
    estoque = {}
    estoque_nome = []
    estoque_quantidade = []
    estoque_valor = []
    estoque_descricao = []
    while True:
        estoque_nome.append = str(input('Digite o nome'))
        estoque['nome'] = estoque_nome

        estoque_quantidade.append = int(input('Digite a quantidade'))
        estoque['quantidade'] = estoque_quantidade

        estoque_valor.append = float(input('Digite o valor'))
        estoque['valor'] = estoque_valor

        estoque_descricao.append = str(input('Digite a descrição'))
        estoque['descricao'] = estoque_descricao

        comando_cadastro = int(input('digite 1 para cadastrar mais um item ou 0 para sair'))

        if comando_cadastro == 0:
            estoque = pd.DataFrame.from_dict(estoque)
            print(estoque)
            break #ADICIONAR FUNÇÃO DE EXPORTAR EM .CSV
        elif comando_cadastro == 1:
            pass
elif comando__estoque == 2:
    