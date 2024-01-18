import pandas as pd
from functions import *


dataset = 'MICRODADOS_ENEM_2022.csv'
colunas = ['NU_INSCRICAO','TP_SEXO','TP_COR_RACA',
            'TP_LOCALIZACAO_ESC', 'TP_STATUS_REDACAO',
            'Q001', 'Q002','Q006','Q025',
            'NU_NOTA_REDACAO', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC','NU_NOTA_MT',
            'TP_PRESENCA_LC', 'TP_ESCOLA',
            'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC','TP_PRESENCA_MT']

df = pd.read_csv(dataset, sep=';', encoding='ISO-8859-1',usecols=colunas)

# Lista das colunas que você quer processar
columns_to_process = ['Q001', 'Q002', 'Q006']

# Loop sobre as colunas
for column in columns_to_process:
    # Definindo a ordem desejada para as categorias
    order = sorted(df[column].unique())
    print(order)