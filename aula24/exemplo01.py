# pip install polars
import pandas as pd 
import polars as pl # biblioteca de manipulação de dados em larga escala
from datetime import datetime # trabalhar com o tempo

ENDERECO_DADOS = './../dados/'

try:
    
    inicio = datetime.now()

    print('Carregando...')

    # Pandas :  0:00:18.68284 
    # df_bolsa_familia = pd.read_csv(ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1')

    # Polars:   0:00:05.949639
    df_bolsa_familia = pl.read_csv(ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1')

    print(df_bolsa_familia)

    final = datetime.now()
    print(f'Tempo de execução de {final - inicio}')
except Exception as e:
    print(f'Erro ao obter ps dadps {e}')