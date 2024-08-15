import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100]

print('Filtro basico \n', df_filtro_basico[['nome', 'idade']])

# Indentificar outliers com Z-score
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[z_scores >= 3]
print("Outliers pela Z-score: \n", outliers_z)

# Filtrar outliers com Z-score
df_score = df[(stats.zscore(df['idade']) < 3)]

# Indentificar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q1 - Q3

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print('Limites IQR: ', limite_baixo, limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print("Outliers pela IQR", outliers_iqr)

# Filtrar outliers em IQR
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# Filtrar enderecos invalidos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereco invalido' if len(x.split('\n')) < 3 else x)
print('Qtd de registros com enderecos grandes:', (df['endereco'] == 'Endereco invalido').sum())

# Tratar campo de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome invalido' if isinstance(x, str) and len(x) > 50 else x)
print('Qtd de registros com nomes grandes:', (df['nome'] == 'Nome invalido').sum())

print('Dados com Outliers tratados: \n', df)

# Salvar dataframe
df.to_csv('clientes_remove_outliers.csv', index=False)
