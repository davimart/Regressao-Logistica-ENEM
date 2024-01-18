import pandas as pd
from functions import *


dataset = 'MICRODADOS_ENEM_2022_FILTRADOS.csv'
colunas = ['NU_INSCRICAO','TP_SEXO','TP_COR_RACA',
            'TP_LOCALIZACAO_ESC', 'TP_STATUS_REDACAO',
            'Q001', 'Q002','Q006','Q025','NU_NOTA_REDACAO', 
            'TP_PRESENCA_LC' ,'TP_DEPENDENCIA_ADM_ESC', 'CO_MUNICIPIO_ESC', 'TP_ESCOLA']

df = pd.read_csv(dataset, sep=';', encoding='ISO-8859-1')#,usecols=colunas)
#imprimir_resumo(df, colunas)
#for coluna in colunas:
#    summary(df,coluna)
print(df.describe())
#summary(df,'TP_DEPENDENCIA_ADM_ESC')
#summary(df,'TP_ESCOLA')

#'10Percentil_Geral'
colunas = ['Percentil_Linguagens','NU_NOTA_REDACAO', 'Acesso_Internet', 'Sexo_Masculino',
            'Preta', 'Parda', 'Amarela', 'Indigena', 
            'Pai_Ensino_Medio_Completo', 'Pai_Ensino_Superior_Mais', 
            'Mae_Ensino_Medio_Completo', 'Mae_Ensino_Superior_Mais', 
            'Ate_1212', 'Entre_1212_e_3030', 'Escola_SemResposta', 'Escola_Publica']

df = df[colunas]
df.to_csv('MICRODADOS_ENEM_2022_FILTRADOS_3.csv', index=False, sep=';')




