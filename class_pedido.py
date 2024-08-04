from pickle import STRING
# definição da classe
class Pedido:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor
    def __init__(self, codido_pedido, endereco_entrega):
        self.__codigo_pedido = codido_pedido
        self.__endereco_entrega = endereco_entrega
        self.__status = 0  # 0 = aberto, 1 = finalizado/pago
        # criando uma estrutura map em python para armazenar itens do pedido
        self.__itens_pedidos = []
        self.garcom = None
        self.atendente = None

    @property
    def _status(self):
        return self.__status

    @_status.setter
    def _status(self, value):
        self.__status = value

    @property
    def _codigo_pedido(self):
        return self.__codigo_pedido

    @_codigo_pedido.setter
    def _codigo_pedido(self, value):
        self.__codigo_pedido = value

    @property
    def _endereco_entrega(self):
        return self.__endereco_entrega

    @_endereco_entrega.setter
    def _endereco_entrega(self, value):
        self.__endereco_entrega = value

    @property
    def _itens_pedidos(self):
        return self.__itens_pedidos

    @_itens_pedidos.setter
    def _itens_pedidos(self, value):
        self.__itens_pedidos = value

    def adicionar_item_ao_pedido(self, itempedido):
        self.__itens_pedidos.append(itempedido)

    def remover_item_pedido(self, codigo_item):
        self.__itens_pedidos.pop(codigo_item)

    def quantidade_itens_pedido(self):
        return int(len(self.__itens_pedidos))
        # return self.__itens_pedidos.__sizeof__

    def toString(self, porcentagem_funcionar):
        str_line = "** INÍCIO DAS INFORMAÇÕES DO PEDIDO **"
        print(str_line, end='\n')
        str_line = "CÓDIGO DO PEDIDO:" + str(self._codigo_pedido)
        print(str_line, end='\t')
        str_line = "STATUS DO PEDIDO:" + \
            str(self._status)  # (0-aberto | 1-finalizado)
        print(str_line, end='\n')
        print(str_line, end='\t')

#################### para imprimir o endereço apenas se ele existir by isaias
        if self._endereco_entrega: #verifica se existe
          str_line = "RUA:" + str(self._endereco_entrega._rua)
          print(str_line, end='\t')
          str_line = "BAIRRO:" + str(self._endereco_entrega._bairro) + "/" + \
          print(str_line, end='\n')

        else:
            print("Pedido para consumo no local")

########### Imprimir as informções do garçom/ atendente by isaias

        if self.garcom: # verifica se o graçom existe
          str_line = "** INFORMAÇÕES DO GARÇOM **"
          print(str_line, end='\n')
          str_line = "NOME DO GARÇOM:" + str(self.garcom._nome)
          print(str_line, end='\t')
          str_line = "10% DO GARÇOM (R$):" + str(self.dez_porcento)
          print(str_line, end='\n')

        elif self.atendente:  # verifica se o atendente existe
          str_line = "** INFORMAÇÕES DA ATENDENTE **"
          print(str_line, end='\n')
          str_line = "NOME DA ATENDENTE:" + str(self.atendente._nome)
          print(str_line, end='\t')
          str_line = "10% DA ATENDENTE (R$):" + str(self.dez_porcento)
          print(str_line, end='\n')

        calc_preco_total = 0.0
        for i, item in enumerate(self._itens_pedidos):
            calc_preco_total += item._preco_item

        # Calcula os 10%
        dez_porcento = calcular_dez_porcento(calc_preco_total)

        str_line = "QUANTIDADE DE ITENS DO PEDIDO:" + \
            str(self.quantidade_itens_pedido())
        print(str_line, end='\n')
        dbl_preco_total = 0.0
        for i, item in enumerate(self._itens_pedidos):
            str_line = "\t #ITEM:" + str(i)
            print(str_line, end='\t')
            str_line = "PRODUTO:" + str(item._produto._descricao)
            print(str_line, end='\t')
            str_line = "QTD (#):" + str(item._quantidade)
            print(str_line, end='\t')
            str_line = "SUBTOTAL (R$):" + str(item._preco_item)
            dbl_preco_total += item._preco_item
            print(str_line, end='\n')
        str_line = "PREÇO TOTAL DO PEDIDO:" + str(dbl_preco_total)
        print(str_line, end='\n')
        str_line = "** FIM DAS INFORMAÇÕES DO PEDIDO **"
        print(str_line, end='\n')

    def finalizar(self): # add r.b.santos
        self._status = 1
        print(self.toString())
        print("**PEDIDO FINALIZADO**")
