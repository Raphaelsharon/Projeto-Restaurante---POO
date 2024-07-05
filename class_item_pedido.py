class ItemPedido:
    def __init__(self, produto, quantidade):
        self.__codigo_produto = produto._codigo_produto
        self.__quantidade = quantidade
        self.__preco_item = produto._preco * quantidade

    @property
    def _codigo_produto(self):
        return self.__codigo_produto

    @_codigo_produto.setter
    def _codigo_produto(self, value):
        self.__codigo_produto = value

    @property
    def _quantidade(self):
        return self.__quantidade

    @_quantidade.setter
    def _quantidade(self, value):
        self.__quantidade = value

    @property
    def _preco_item(self):
        return self.__preco_item

    @_preco_item.setter
    def _preco_item(self, value):
        self.__preco_item = value



