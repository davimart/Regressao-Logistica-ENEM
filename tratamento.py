import pandas as pd
from functions import *


dataset = 'MICRODADOS_ENEM_2022.csv'
colunas = ['NU_INSCRICAO','TP_SEXO','TP_COR_RACA',
            'TP_LOCALIZACAO_ESC', 'TP_STATUS_REDACAO',
            'Q001', 'Q002','Q006','Q025', 'Q003', 'Q004',
            'NU_NOTA_REDACAO', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC','NU_NOTA_MT',
            'TP_PRESENCA_LC', 'TP_ESCOLA',
            'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC','TP_PRESENCA_MT']

df = pd.read_csv(dataset, sep=';', encoding='ISO-8859-1',usecols=colunas)

#remover faltantes
#df = df[df['TP_PRESENCA_CN'] == 1]
#df = df[df['TP_PRESENCA_CH'] == 1]
#df = df[df['TP_PRESENCA_LC'] == 1]
#df = df[df['TP_PRESENCA_MT'] == 1]


#imprimir_resumo(df, colunas, 'bruto')
#for coluna in colunas:
#    summary(df,coluna)

# ------------ DUMMIES --------------

# 'TP_SEXO' - > Sexo_Masculino (0 - feminino, 1 - masculino)
df = dummy_sexo(df)

# 'TP_COR_RACA' - > Preta,etc,Indígena (0 em tudo é Branca)
df = dummy_raca(df)

# ESCOLARIDADE DOS PAIS - Menos que médio, médio, mais que médio e sem 'Não sei'

df = dummy_escolaridade_parente(df)

#RENDA FAMILIAR - menos 1200, entre 1200 e 3000, mais do que 3000
df = dummy_renda_familiar(df)


#'Q025' Na sua residência tem acesso à Internet?
df = dummy_acesso_internet(df)


#TIPO de escola 00 - Privada 10- Não respondeu 01-Pública
df = dummy_tipo_escola(df)

df = dummy_profissao_parente(df)


#Varíavel dependente/target
#Bottom 10% + valores nulos - 1 e resto - 0

# Escolha a coluna 'NU_NOTA_REDACAO'
coluna_notas_redacao = 'NU_NOTA_REDACAO'

# Passo 1: Calcule o 10º percentil
percentil_10 = df[coluna_notas_redacao].quantile(0.1)
#print('PERCENTIL 10% DE NOTAS DA REDACAÇÃO: ', percentil_10)

# Passo 2: Crie a nova coluna com base nas condições
# Nota nula + 10 percentil
df['Performance_Redacao'] = 0  # Inicializa com 0
df.loc[(df[coluna_notas_redacao].isnull()) | (df[coluna_notas_redacao] <= percentil_10), 'Performance_Redacao'] = 1

#10percentil
percentil = df[coluna_notas_redacao].quantile(0.1)
df['10Percentil_Redacao'] = 0  # Inicializa com 0
df.loc[(df[coluna_notas_redacao] <= percentil), '10Percentil_Redacao'] = 1

#25percentil
percentil = df[coluna_notas_redacao].quantile(0.25)
df['25Percentil_Redacao'] = 0  # Inicializa com 0
df.loc[(df[coluna_notas_redacao] <= percentil), '25Percentil_Redacao'] = 1

#nota nula
df['Redacao_Nula'] = 0  # Inicializa com 0
df.loc[(df[coluna_notas_redacao].isnull()), 'Redacao_Nula'] = 1

#falta ou eliminado
df['Redacao_Falta'] = 0  # Inicializa com 0
df.loc[(df['TP_PRESENCA_LC'] == 0) | (df['TP_PRESENCA_LC'] == 2), 'Redacao_Falta'] = 1

#redacao com problema
df['Problema_Redacao'] = 0  # Inicializa com 0
df.loc[(df['TP_STATUS_REDACAO'] != 1) & (~df['TP_STATUS_REDACAO'].isnull()), 'Problema_Redacao'] = 1


#Performance geral - bottom 10%
df['Nota_Geral'] = df[['NU_NOTA_REDACAO', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC','NU_NOTA_MT']].sum(axis=1, skipna=True)

percentil = df['Nota_Geral'].quantile(0.1)
df['10Percentil_Geral'] = 0  # Inicializa com 0
df.loc[(df['Nota_Geral'] <= percentil), '10Percentil_Geral'] = 1

#linguagens - bottom 10%
percentil = df['NU_NOTA_LC'].quantile(0.9)
df['Percentil_Linguagens'] = 0  # Inicializa com 0
df.loc[(df['NU_NOTA_LC'] <= percentil), 'Percentil_Linguagens'] = 1


percentil = df['NU_NOTA_REDACAO'].quantile(0.9)
df['Percentil_Redacao'] = 0  # Inicializa com 0
df.loc[(df['NU_NOTA_REDACAO'] <= percentil), 'Percentil_Redacao'] = 1

# Exibir o DataFrame resultante
#print(df[['NU_NOTA_REDACAO', 'Performance_Redacao']])

percentil = df['Nota_Geral'].quantile(0.25)
df['Vinte_CincoPercentil_Geral'] = 0  # Inicializa com 0
df.loc[(df['Nota_Geral'] <= percentil), 'Vinte_CincoPercentil_Geral'] = 1

#print(df)
colunas = ['NU_INSCRICAO','TP_SEXO','TP_COR_RACA',
            'TP_LOCALIZACAO_ESC', 'TP_STATUS_REDACAO',
            'Q001', 'Q002','Q006','Acesso_Internet',
            'NU_NOTA_REDACAO', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC','NU_NOTA_MT',
            'TP_PRESENCA_LC', 'TP_ESCOLA',
            'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC','TP_PRESENCA_MT']

imprimir_resumo(df, colunas, 'Geral')

df.to_csv('MICRODADOS_ENEM_2022_FILTRADOS.csv', index=False, sep=';')
colunas = df.columns.tolist()


aux = df
colunas = ['10Percentil_Geral', 'Acesso_Internet', 'Sexo_Masculino',
            'Preta', 'Parda', 'Amarela', 'Indigena', 
            'Pai_Ensino_Medio_Completo', 'Pai_Ensino_Superior_Mais', 
            'Mae_Ensino_Medio_Completo', 'Mae_Ensino_Superior_Mais', 
            'Ate_1212', 'Entre_1212_e_3030', 'Escola_SemResposta', 'Escola_Publica']

df = df[colunas]
df.to_csv('MICRODADOS_ENEM_2022_FILTRADOS_final.csv', index=False, sep=';')

imprimir_resumo(aux, colunas, 'Filtrado')

