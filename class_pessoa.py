class Pessoa:
    def __init__(self, nome, cpf, porcentagem_lucro):
        self._nome = nome
        self._cpf = cpf
        self._pocentagem_lucro = porcentagem_lucro
        
        
class Cliente(Pessoa):
   def __init__(self, nome, cpf, endereço):
    super().__init__ (nome, cpf)
    self._endereço = endereço

class Atendente(Pessoa):#entregador
    def __init__(self, nome, cpf):
     super().__init__ (nome, cpf)

class Garcom(Pessoa):
    def __init__(self, nome, cpf):
      super().__init__(nome,cpf)
      
class Entregador(Pessoa):
    def __init__(self, nome, cpf, porcentagem_lucro):
        self._nome = nome
        self._cpf = cpf
        self._pocentagem_lucro = porcentagem_lucro
    
