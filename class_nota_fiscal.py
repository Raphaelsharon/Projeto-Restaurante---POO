from datetime import datetime
import pandas as pd

class Produto:
    def __init__(self, codigo, nome, preco, validade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.validade = validade

    def __repr__(self):
        return f"Produto(codigo={self.codigo}, nome='{self.nome}', preco={self.preco}, validade={self.validade})"

def cadastrar_produto(codigo,nome,preco,validade):
    int_codigo = codigo
    str_nome = nome
    flt_preco = preco
    date_validade = validade
    #date_validade = datetime.strptime(date_validade, '%d/%m/%Y')
    return Produto(int_codigo, str_nome, flt_preco, date_validade)

# Ler o arquivo Excel
file_path = r"C:\Users\PH\Downloads\produtos.xlsx"  # Altere este caminho conforme necessário
df = pd.read_excel(file_path)

# Imprimir os nomes das colunas para verificar
#print(df.columns)

# Criar uma lista para armazenar as instâncias de Produto
produtos = []

# Ajustar os nomes das colunas de acordo com a impressão anterior
for index, row in df.iterrows():
    produto = cadastrar_produto(row['codigo'], row['nome'], row['preco'], row['validade'])
    produtos.append(produto)
    
# Imprimir os produtos para verificar
for produto in produtos:
    print(produto)