from class_endereco import Endereco
from class_item_pedido import ItemPedido
from class_pedido import Pedido
from class_produto import Produto


def menu_principal():  # MENU PRINCIPAL
    print('''
        MENU Principal:

        [1] - Cadastrar novo endereço
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
