# definição da classe
class Pedido:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor
    def __init__(self, endereco_entrega):
        self.__endereco_entrega = endereco_entrega
        # criando uma estrutura map em python para armzenar itens do pedido
        self.__itens_pedidos = {} 

    def adicionar_item_quantidade(self, codigo_produto, quantidade):
        self.__itens_pedidos[codigo_produto] = quantidade

    def remover_item(self, codigo_produto):
        del self.__itens_pedidos[codigo_produto]
        
    def quantidade_itens(self):
        return self.__itens_pedidos.__sizeof__
