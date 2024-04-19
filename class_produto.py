# definição da classe
class Produto:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor 
    def __init__(self, codigo_produto, descricao, valor, validade):
        self.__codigo_produto = codigo_produto # __ modificador de acesso private
        self.__descricao = descricao
        self.__valor = valor
        self.__validade = validade

    @property
    def _codigo_produto(self):
        return self.__codigo_produto

    @_codigo_produto.setter
    def _codigo_produto(self, value):
        self.__codigo_produto = value

    @property
    def _descricao(self):
        return self.__descricao

    @_descricao.setter
    def _descricao(self, value):
        self.__descricao = value

    @property
    def _valor(self):
        return self.__valor

    @_valor.setter
    def _valor(self, value):
        self.__valor = value

    @property
    def _validade(self):
        return self.__validade

    @_validade.setter
    def _validade(self, value):
        self.__validade = value
