from class_endereco import Endereco
from class_item_pedido import ItemPedido
from class_pedido import Pedido 
from class_produto import Produto
from class_pessoa import *
from datetime import datetime
from banco_de_dados import Banco_de_Dados

def menu_geral():
    print('''
          MENU GERAL:
          [1] - Gerente
          [2] - Funcionarios
          [s] - Sair
          ''')
    return str(input("Escolha uma opção: "))

def menu_gerante():
    print('''
          MENU GERENTE:
          [1] - Cadastrar novo garçom
          [2] - Cadastrar novo atendente
          [3] - Cadastrar novo entregador
          [s] - Sair
          ''')
    return str(input("Escolha uma opção: "))


def menu_principal():  # MENU PRINCIPAL
    print('''
        MENU Principal:
        [1] - Controle de vendas
        [2] - Cadastrar novo produto
        [3] - Remover um produto
        [4] - Pesquisar um produto
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

def menu_pedido():  # MENU Vendas
    print('''
        MENU Vendas:
        [1] - Abrir novo pedido
        [2] - Adicionar item ao pedido
        [3] - Remover item do pedido
        [4] - Listar itens do pedido em detalhes
        [5] - Finalizar pedido e imprimir
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

#----------------------------------------r.b.santos---------------------------------------------------
def pedido_adicionar():
    # código pedido gerado automaticamente
    # alterado -> administrar pedido para entrega e pedido para consumo no local
    local = input('''
                    [1] - Pedido para consumir no local
                    [2] - Pedido para entrega

                    Escolha uma opção: ''')

    if local == '1':
        codigo_pedido = int(len(pedidos) + 1)  # a numeração do pedido começa de 1 até n
        print(f'O código do pedido é {codigo_pedido}')  # alterado -> mostrar o código do pedido
        endereco_pedido = None
        garcom = cadastrar_garcom() #para salvar as informações do garçom q atendeu
        pedido.garcom = garcom

    elif local == '2':
        # código pedido gerado automaticamente
        endereco_pedido = cadastrar_endereco()
        # a numeração do pedido começa de 1 até n
        codido_pedido = int(len(pedidos)) + 1
        # alterado -> mostrar o código do pedido
        atendente = cadastrar_atendente() #para salvar as informações da atendente q atendeu
        pedido.atendente = atendente

    return Pedido(codigo_pedido, endereco_pedido)
#-----------------------------------------------------------------------------------------------------#

def pedido_adicionar_item():
    int_pedido_selecionado = int(input('Informe o código do pedido para adicionar um novo item: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_produto = int(input('Informe o código do produto para adicionar ao pedido: '))
        produto = buscar_produto_por_codigo(int_codigo_produto)
        if produto:
            int_quantidade_item = int(input('Informe a quantidade do item:'))
            novo_item_pedido = ItemPedido(produto, int_quantidade_item)
            pedido.adicionar_item_ao_pedido(novo_item_pedido)
        else:
            print("Não foi possível adicionar este produto, pois o código do produto não existe!")
          #return Pedido(codido_pedido, endereco_pedido)
    else:
        print("Pedido inexistente")
        return False

def pedido_remover_item():
    int_pedido_selecionado = int(input('Informe o código do pedido para remover um item selecionado: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_item = int(input('Informe o número do item para remover deste pedido ' + str(pedido._codigo_pedido) + ': '))
        # verifica se número intem informado existe: não faz sentido remover item 5 se ele não existe
        #if pedido.quantidade_itens_pedido() <= int_codigo_item:
        pedido.remover_item_pedido(int_codigo_item)
    else:
        print("Pedido inexistente")
        return False

def pedido_listar_items():
    int_pedido_selecionado = int(input('Informe o código do pedido para mais detalhes: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        pedido.toString()
    else:
        print("Pedido inexistente")
        return False

def cadastrar_endereco():
    str_rua = str(input('Informe a rua: '))
    int_num = int(input('Informe o número: '))
    str_complemento = str(input('Informe o complemento do endereço: '))
    str_bairro = str(input('Informe o bairro: '))
    endereco = Endereco(str_rua, int_num, str_complemento, str_bairro) #erro Endereco não está definido
    return endereco
#----------------------------------------r.b.santos---------------------------------------------------#
def cadastrar_produto():
    #Criar a conexão
    variavel_conexao = Banco_de_Dados.ConexaoBanco()
    #Criar tabela
    tabela_protudo = Banco_de_Dados.CriarTabela(variavel_conexao, Banco_de_Dados.produto_tabela)
    int_codigo = input('Informe o código identificador do produto: ')
    str_nome = input('Qual o nome/descrição do produto: ')
    flt_preco = input('Informe o valor (ex. 0.00): ')
    try:
        date_validade = (input('Informe a validade do produto (formato dd/mm/aaaa): '))
        #date_validade = datetime.strptime(date_validade, '%d/%m/%Y')
        Banco_de_Dados.insert_produto(variavel_conexao, str_nome, flt_preco, date_validade)
        #finalisa a conexao    
        variavel_conexao.close()
        return Produto(int_codigo, str_nome, flt_preco, date_validade)

    except ValueError:
        print("Data inválida")
        return False

#-----------------------------------------------------------------------------------------------------#
    
def remover_produto():
    int_codigo_remocao = int(input('Informe o código do produto para remoção: '))
    produto_remover = estoque_produtos[int_codigo_remocao]
    print("Produto (" + produto_remover._descricao + ") removido!")
    del estoque_produtos[int_codigo_remocao]

def buscar_produto_por_codigo(int_codigo_produto):
    # Verifica se existe produto cadastrado
    for chave in estoque_produtos.keys():
        if chave == int_codigo_produto:
            return estoque_produtos[int_codigo_produto]
    return False

def buscar_pedido_por_codigo(int_codigo_pedido):
    # Verifica se existe produto cadastrado
    for chave in pedidos.keys():
        if chave == int_codigo_pedido:
            return pedidos[int_codigo_pedido]
    return False

def pedido_finalizar(): # add r.b.santos
    int_pedido_selecionado = int(input('Informe o código do pedido para finalizar: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        pedido.finalizar()
        return True
    else:
        print("Pedido inexistente")
        return False

######### cadastrar funcionarios by isaias

def cadastrar_garcom():
  nome = input("Digite o nome do garçom: ")
  cpf = input("Digite o CPF do garçom: ")
  return Garcom(nome, cpf)

def cadastrar_atendente():
  nome = input("Digite o nome da atendente: ")
  cpf = input("Digite o CPF da atendente: ")
  return Atendente(nome, cpf)

def calcular_dez_porcento(valor_total): # 10% do funcionario
  return valor_total * 0.1

######### ------------------------------------

def cadastrar_entregador():
  nome = str(input("Digite o nome do entregador: "))
  cpf = str(input("Digite o CPF do entregador: "))
  lucro_por_entrega = float(input("Informe o lucro por entrega do entregador: "))
  return Pessoa(nome, cpf, lucro_por_entrega)

# Aplicação de exemplo disciplina POO - UFRB
# Sistema de controle de pedidos
# Professor Guilherme Braga Araújo

estoque_produtos = {}
pedidos = {}
while True:
    #menu_gerente
    opcao_escolhida = menu_geral()
    if opcao_escolhida == "1":
        opcao_escolhida = menu_gerante()
        if opcao_escolhida == "1":
            garcom = cadastrar_garcom()
        elif opcao_escolhida == "2":
            atendente = cadastrar_atendente()
        elif opcao_escolhida == "3":
            entregador = cadastrar_entregador()
        else:
            break
    #menu_funcionario 
    elif opcao_escolhida == "2":
            
        while True:
            # menu_principal
            opcao_escolhida = menu_principal()
            # verificando escolha
            # opc sair
            if (opcao_escolhida == "s"):
                break
            # opc 1
            elif (opcao_escolhida == "1"):
                while True:
                    opcao_escolhida = menu_pedido()
                    # opc menu vendas - novo pedido
                    if (opcao_escolhida == "1"):
                        pedido = pedido_adicionar()
                        if (pedido):
                            # adiciona pedido ao sistema
                            pedidos[pedido._codigo_pedido] = pedido
                    # opc menu vendas - adicionar item
                    elif (opcao_escolhida == "2"):
                        pedido_adicionar_item()
                    elif (opcao_escolhida == "3"):
                        pedido_remover_item()
                    elif (opcao_escolhida == "4"):
                        pedido_listar_items()
                    elif (opcao_escolhida == "5"):
                        pedido_finalizar()
                    else:
                        # Volta para o menu principal
                        break

            # opc 2
            elif (opcao_escolhida == "2"):
                produto = cadastrar_produto()
                if (produto):
                    # adiciona produto ao nosso estoque
                    estoque_produtos[produto._codigo_produto] = produto
            # opc 3
            elif (opcao_escolhida == "3"):
                remover_produto()
            # opc 4
            elif (opcao_escolhida == "4"):
                int_codigo_produto = int(input('Informe o código do produto para busca: '))
                produto_pesquisa = buscar_produto_por_codigo(int_codigo_produto)
                if (produto_pesquisa):
                    print("Produto encontrado:")
                    print(">Código=" + str(produto_pesquisa._codigo_produto))
                    print(">Descricao=" + produto_pesquisa._descricao)
                    print(">Valor=" + str(produto_pesquisa._preco))
                    print(">Validade=" + str(produto_pesquisa._validade))
                else:
                    print("Produto nâo cadastrado/encontrado.")
            else:
                print("A opção escolhida é inválida.")