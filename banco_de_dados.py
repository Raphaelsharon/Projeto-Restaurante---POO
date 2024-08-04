import sqlite3
from sqlite3 import Error

########## Criar Conexão
class Banco_de_Dados():
    def ConexaoBanco():
        caminho = "C:\\Users\\PH\\Documents\\Faculdade\\git\\Projeto-Restaurante---POO\\banco.db"
        conexao = None
        try:
            conexao = sqlite3.connect(caminho)
        except Error as ex:
            print(ex)
        return conexao

    #Criar Tabela
    def CriarTabela(conexao, sql):
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
            print("Tabela criada")
        except Error as ex:
            print(ex)
        return None

    def inserir_informacoes_tabela(conexao, sql):
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
            conexao.commit()
            print("Informação inserida")
        except Error as ex:
            print(ex)
        return None

    #Comando sql para Criar Tabela
    produto_tabela = """CREATE TABLE produtos (
        in_codigo_produto  NUMERIC,
        tex_nome_descricao TEXT (14),
        in_preco           NUMERIC,
        tex_validade       DATE (14) 
    );"""

    enderaco_tabela = """CREATE TABLE enderaco (
        in_codigo_client   NUMERIC,
        tex_rua            TEXT (14),
        tex_numero         TEXT (14),
        tex_complemento    TEXT (14),
        tex_bairro         TEXT (14)
    );"""

    item_pedido_tabela = """CREATE TABLE item_pedido (
        in_codico_pedido   NUMERIC,
        in_quatidade       INTEGER,
        in_preco_item      NUMERIC
    );"""

    pedido_tabela = """CREATE TABLE pedido (
        in_codico_produto       NUMERIC,
        tex_endereco_entrega    INTEGER,
        in_status               INTEGER
    );"""
    
    #Inserir dados as tabelas
    def insert_produto(conexao,str_nome, flt_preco, date_validade):
        insert_produto = "INSERT INTO produtos (tex_nome_descricao, in_preco, tex_validade) VALUES('"+str_nome+"', '"+flt_preco+"', '"+date_validade+"')"
        Banco_de_Dados.inserir_informacoes_tabela(conexao, insert_produto)
        
    def insert_endereco(conexao, str_rua, int_num, str_complemento, str_bairro):
        insert_endereco = "INSERT INTO enderaco (tex_rua, tex_bairro, tex_numero, tex_complemento) VALUES('"+str_rua+"', '"+int_num+"', '"+str_complemento+"', '"+str_bairro+"')"
        Banco_de_Dados.inserir_informacoes_tabela(conexao, insert_endereco)

    def insert_item(conexao, int_quatidade, flt_preco_item):
        insert_item = "INSERT INTO item_pedido (in_quatidade, in_preco_item) VALUES('"+int_quatidade+"', '"+flt_preco_item+"')"
        Banco_de_Dados.inserir_informacoes_tabela(conexao, insert_item)

    def insert_pedido(conexao, int_endereco_entrega, int_status):
        insert_pedido = "INSERT INTO pedido (tex_endereco_entrega, in_status) VALUES('"+int_endereco_entrega+"', '"+int_status+"')"
        Banco_de_Dados.inserir_informacoes_tabela(conexao, insert_pedido)
        
    def insert_funcionarios(conexao, nome, cpf, pocentagem):
        pass
#CriarTabela(variavel_conexao, enderaco_tabela)
#CriarTabela(variavel_conexao, item_pedido_tabela)
#CriarTabela(variavel_conexao, pedido_tabela)
