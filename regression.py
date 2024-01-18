import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import statsmodels.api as sm


# Supondo que 'df' é o DataFrame organizado e pronto para a regressão logística
# df = ...

dataset = 'MICRODADOS_ENEM_2022_FILTRADOS.csv'
colunas = ['NU_NOTA_REDACAO','Acesso_Internet', 'Sexo_Masculino',
            'Preta', 'Parda', 'Amarela', 'Indigena', 
            'Pai_Ensino_Medio_Completo', 'Pai_Ensino_Superior_Mais', 
            'Mae_Ensino_Medio_Completo', 'Mae_Ensino_Superior_Mais', 
            'Ate_1212', 'Entre_1212_e_3030', 'Escola_SemResposta', 'Escola_Publica',
            'Performance_Redacao', '10Percentil_Redacao', 'Redacao_Nula', 'Redacao_Falta', 
            'Problema_Redacao', '25Percentil_Redacao', '10Percentil_Geral','Percentil_Linguagens']


df = pd.read_csv(dataset, sep=';', encoding='ISO-8859-1', usecols=colunas)

# Adicionando uma constante para o termo independente
df['constante'] = 1

# Escolha a coluna de destino (variável dependente) e as colunas de recursos (variáveis independentes)
colunas_alvo = ['Performance_Redacao', '10Percentil_Redacao', 
                'Redacao_Nula', 'Redacao_Falta', 'Problema_Redacao', '25Percentil_Redacao',
                '10Percentil_Geral','Percentil_Linguagens']
#colunas_recursos = df.columns.difference([colunas_alvo])
#colunas_recursos = colunas - colunas_alvo

colunas_recursos = pd.Index(colunas).difference(colunas_alvo).tolist()

# Nome do arquivo para salvar o resumo do modelo
nome_arquivo = 'resumo_modelo.txt'

# Abrir o arquivo para escrita
with open(nome_arquivo, 'w') as arquivo:

    for coluna_alvo in colunas_alvo:
        if coluna_alvo == 'Percentil_Linguagens':
            try:
                # Criar um modelo de regressão logística usando StatsModels
                modelo_statsmodels = sm.Logit(df[coluna_alvo], df[colunas_recursos])

                # Ajustar o modelo aos dados
                resultado_statsmodels = modelo_statsmodels.fit()

                # Exibir um resumo do modelo
                #print(resultado_statsmodels.summary())
                
                # Redirecionar a saída do resumo para o arquivo
                print(f'\nResumo da Regressão para {coluna_alvo}:\n', file=arquivo)
                print(resultado_statsmodels.summary(), file=arquivo)
            
            except:
                print("Erro na coluna: ", coluna_alvo)

print(f'Resumo da Regressão para todas as colunas alvo salvo em {nome_arquivo}')

