from class_endereco import Endereco
from class_item_pedido import ItemPedido
from class_pedido import Pedido
from class_produto import Produto


def menu_principal():  # MENU PRINCIPAL
    print('''
        MENU Principal:

        [1] - Cadastrar novo endereço
        [p] - Cadastrar novo produto
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))


def cadastrar_endereco():
    str_cep = str(input('Informe o cep:'))
    str_rua = str(input('Informe a rua:'))
    int_num = int(input('Informe o número:'))
    str_complemento = str(input('Informe o complemento:'))
    str_bairro = str(input('Informe o bairro:'))
    str_cidade = str(input('Informe a cidade:'))
    endereco = Endereco(str_cep, str_rua, int_num,
                        str_complemento, str_bairro, str_cidade)
    return endereco


# Aplicação de exemplo disciplina POO - UFRB
# Sistema de controle de pedidos
# Professor Guilherme Braga Araújo

def cadatrar_produto():
        int_codigo_produto = int(input("Informe o código do produto: "))
        str_descricao = str(input("Informe a descrição do produto: "))
        float_valor = float(input("Informe o valor do produto: "))
        str_validade = str(input("Informe a validade do produto: "))
        produto = Produto(int_codigo_produto, str_descricao, float_valor, str_validade)
        return produto
    
opcao_escolhida = menu_principal() # menu_principal

while True:
    
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
            
    elif (opcao_escolhida == "p"):
        produto = cadatrar_produto()
        if (produto):
            print("Novo produto castrado com sucesso!")
            print(f"Código: {produto._codigo_produto}")
            print(f"Descrição: {produto._descricao}")
            print(f"Valor: {produto._valor}")
            print(f"Validade: {produto._validade}")
            
    opcao_escolhida = menu_principal()