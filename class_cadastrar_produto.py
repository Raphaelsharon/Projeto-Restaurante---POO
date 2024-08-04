#r.b.santos
from class_produto import Produto
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
root = tk.Tk()


class Cadastrar_Produto(Produto):

    def cadastrar_produto_lista(codigo, nome, preco, validade):
        int_codigo = int(codigo)
        str_nome = str(nome)
        flt_preco = float(preco)
        date_validade = str(validade)
        #date_validade = datetime.strptime(date_validade, '%d/%m/%Y')
        return Produto(int_codigo, str_nome, flt_preco, date_validade)
    
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