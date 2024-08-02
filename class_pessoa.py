from datetime import datetime
import pandas as pd


class Produto:
    def __init__(self, codigo, nome, preco, validade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.validade = validade

def converter_para_csv():
    arquivo_selecionado = filedialog.askopenfilename()
    if arquivo_selecionado:
        extensao_arquivo = arquivo_selecionado.split('.')[-1]
        if extensao_arquivo.lower() == 'xlsx':
            df = pd.read_excel(arquivo_selecionado)
            nome_arquivo_csv = arquivo_selecionado.split('.')[0] + '.csv'
            df.to_csv(nome_arquivo_csv, index=False)
            print(f'Arquivo CSV convertido: {nome_arquivo_csv}')
            return df
        else:
            print('O arquivo selecionado não é um arquivo XLSX.')
    return None

# Chama a função para iniciar o processo de conversão
df = converter_para_csv()

if df is not None:
    produtos_lista = {}
    for index, row in df.iterrows():
        codigo = row['codigo']
        nome = row['nome']
        preco = row['preco']
        validade = row['validade']
        produtos_lista[codigo] = [nome, preco, validade]
    
    print("Código\tNome\tPreço\tValidade")
    for codigo, dados in produtos_lista.items():
        print(f"{codigo}\t{dados[0]}\t{dados[1]}\t{dados[2]}")