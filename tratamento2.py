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


#Performance geral - top 10%
df['Nota_Geral'] = df[['NU_NOTA_REDACAO', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC','NU_NOTA_MT']].sum(axis=1, skipna=True)

percentil = df['Nota_Geral'].quantile(0.9)
df['Top_10Percentil_Geral'] = 0  # Inicializa com 0
df.loc[(df['Nota_Geral'] >= percentil), 'Top_10Percentil_Geral'] = 1


#print(df)
#subset_df = df[df['Top_10Percentil_Geral'] == 1]
#imprimir_resumo(subset_df, df.columns, 'Geral_Psicologia_Subset', 'ENEM Top 10%')
#imprimir_resumo(df, df.columns, 'Geral_Psicologia','ENEM Geral')


# Agora 'subset_df' contém apenas as linhas onde 'Top_10Percentil_Geral' é igual a 1

print(df.columns)
df.to_csv('MICRODADOS_ENEM_2022_FILTRADOS.csv', index=False, sep=';')
colunas = df.columns.tolist()


colunas = ['Top_10Percentil_Geral', 'Sexo_Masculino',
            'Preta', 'Parda', 'Amarela', 'Indigena', 
            'Pai_Menos_que_Medio','Pai_Ensino_Medio_Completo', 'Pai_Ensino_Superior_Mais', 
            'Mae_Menos_que_Medio','Mae_Ensino_Medio_Completo', 'Mae_Ensino_Superior_Mais',
            'Pai_Grupo_1', 'Pai_Grupo_2', 'Pai_Grupo_3',
            'Pai_Grupo_4', 'Pai_Grupo_5', 'Mae_Grupo_1',
            'Mae_Grupo_2', 'Mae_Grupo_3', 'Mae_Grupo_4', 'Mae_Grupo_5', 
            'Ate_1212', 'Entre_1212_e_3030', 'Escola_Publica', 'Escola_Privada','Acesso_Internet']

df = df[colunas]
df.to_csv('MICRODADOS_ENEM_2022_PSICOLOGIA.csv', index=False, sep=';')

#imprimir_resumo(df, df.columns, 'Filtrado_Psicologia', 'ENEM Geral')
#subset_df = df[df['Top_10Percentil_Geral'] == 1]
#imprimir_resumo(subset_df, df.columns, 'Filtrado_Psicologia_Subset','ENEM Top 10%')

