import pandas as pd
from functions import *

dataset = 'MICRODADOS_ENEM_2022_PSICOLOGIA.csv'
df = pd.read_csv(dataset, sep=';', encoding='ISO-8859-1')

df.rename(columns={'Top_10Percentil_Geral': 'Top_Geral'}, inplace=True)

df.to_csv(dataset, index=False, sep=';')

