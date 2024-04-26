from class_endereco import Endereco
from class_item_pedido import ItemPedido
from class_pedido import Pedido
from class_produto import Produto

from datetime import datetime

def menu_principal():  # MENU PRINCIPAL
    print('''
        MENU Principal:

        [1] - Cadastrar novo endereço
        [2] - Cadastrar novo produto
        [3] - Remover produto
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))


def cadastrar_endereco():
    str_cep = str(input('Informe o cep: '))
    str_rua = str(input('Informe a rua: '))
    int_num = int(input('Informe o número: '))
    str_complemento = str(input('Informe o complemento: '))
    str_bairro = str(input('Informe o bairro: '))
    str_cidade = str(input('Informe a cidade: '))
    endereco = Endereco(str_cep, str_rua, int_num,
                        str_complemento, str_bairro, str_cidade)
    return endereco

def cadastrar_produto():
    int_codigo = int(input('Informe o código identificador do produto: '))
    str_nome = str(input('Qual o nome/descrição do produto? '))
    flt_valor = float(input('Informe o valor (ex. 0.00): '))
    date_validade = (input('Informe a validade do produto (formato dd/mm/aaaa): '))
    date_validade = datetime.strptime(date_validade, '%d/%m/%Y')
    return Produto(int_codigo, str_nome, flt_valor, date_validade)    

def remover_produto():
    int_codigo_remocao = int(input('Informe o código do produto para remoção: '))
    produto_remover = estoque_produtos[int_codigo_remocao]
    print("Produto (" + produto_remover._descricao + ") removido!") 
    del estoque_produtos[int_codigo_remocao]  

def buscar_produto_por_codigo():
    int_codigo_remocao = int(input('Informe o código do produto para busca: '))
    # Verifica se existe produto cadastrado
    for chave in estoque_produtos.keys():
        if chave == int_codigo_remocao:
            return estoque_produtos[int_codigo_remocao]
    return False
    


# Aplicação de exemplo disciplina POO - UFRB
# Sistema de controle de pedidos
# Professor Guilherme Braga Araújo

estoque_produtos = {}

while True:
    # menu_principal
    opcao_escolhida = menu_principal()
    # verificando escolha
    if (opcao_escolhida == "s"):
        break
    elif (opcao_escolhida == "1"):
        endereco = cadastrar_endereco()
        if (endereco):
            print("Configuramos um objeto endereço, veja: ")
            print(endereco._cep)
            print(endereco._rua)
            print(endereco._complemento)
            print(endereco._bairro)
            print(endereco._cidade)

    elif (opcao_escolhida == "2"):
        produto = cadastrar_produto()
        if (produto):
            # adiciona produto ao nosso estoque
            estoque_produtos[produto._codigo_produto] = produto
    
    elif (opcao_escolhida == "3"):
        remover_produto()
    
    #print(estoque_produtos)
    produto_pesquisa = buscar_produto_por_codigo()
    if (produto_pesquisa):
        print("Produto encontrado:")
        print(">Código=" + str(produto_pesquisa._codigo_produto))
        print(">Descricao=" + produto_pesquisa._descricao)
        print(">Valor=" + str(produto_pesquisa._valor))
        print(">Validade=" + str(produto_pesquisa._validade))
    else:
        print("Produto nâo cadastrado/encontrado.")
