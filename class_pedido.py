# definição da classe
class Pedido:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor
    def __init__(self, codido_pedido, endereco_entrega):
        self.__codigo_pedido = codido_pedido
        self.__endereco_entrega = endereco_entrega
        self.__status = 0 # 0 = aberto, 1 = finalizado/pago
        # criando uma estrutura map em python para armzenar itens do pedido
        self.__itens_pedidos = [] 

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
        
    def remover_item_pedido(self, codigo_produto):
        del self.__itens_pedidos[codigo_produto]
        
    def quantidade_itens_pedido(self):
        return int(len(self.__itens_pedidos))
        #return self.__itens_pedidos.__sizeof__
