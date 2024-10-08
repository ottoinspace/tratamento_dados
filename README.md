 # Tratamento de dados usando Python
 ## intro_tratamento_dados
  Analisar a estrutura dos dados utilizando comandos como head(), tail(), info(), isnull(), e sum() para identificar a presença de valores nulos e outliers.
 ## estudo_lambda
  Demonstração prática da aplicação de funções lambda em Python, onde o código:
  ```
def eleva_cubo(x):
    return x ** 3
  ```
  é funcionalmente equivalente ao código abaixo:
  ```
eleva_cubo_lambda = lambda x : x ** 3
  ```
  > Usadas em situações específicas em que o código da função geralmente é mais simples.
 ## limpeza_dados
  Mostra como e feita a limpeza dos dados;
 ### Remover dados
  Para remover colunas ou linhas em um DataFrame, podemos utilizar o método `.drop()`. Por exemplo:
```
  df.drop('pais', axis=1, inplace=True)  # Coluna
  df.drop(2, axis=0, inplace=True)  # Linha
```

 ### Normalizar campos de texto
  A normalização de campos de texto pode ser feita usando o atributo `.str`, que permite padronizar o texto, seja em minúsculas, maiúsculas ou apenas a primeira letra maiúscula:
  ```
  df['nome'] = df['nome'].str.title()
  df['endereco'] = df['endereco'].str.lower()
  df['estado'] = df['estado'].str.strip().str.upper()
  ```
> Nota: Ao normalizar textos, é recomendável manter a consistência. Escolha um único padrão, como tudo em maiúsculas ou tudo em minúsculas, para evitar confusão.

 ### Converter tipos de dados
  Para converter o tipo de um dado, utilizamos o método `.astype()`. Veja o exemplo abaixo:
  ```
  df['idade'] = df['idade'].astype(int)
  ```
 ### Tratando valores nulos
  Valores nulos podem ser tratados de diversas formas. Podemos substituí-los utilizando o método `.fillna()`:
```
df_fillna = df.fillna(0)  # Substituir valores nulos por 0
```
  Caso prefira remover os valores nulos, podemos utilizar o método `.dropna()`:
```
df_dropna = df.dropna()  # Remove valores nulos
```
  Se for necessário remover valores nulos em um campo específico, utilizamos o código abaixo:
```
df = df.dropna(subset=['cpf'])  # Remover registro com CPF nulo
```
 ## outliers
Outliers são valores que se encontram significativamente abaixo ou acima da maioria dos dados em um conjunto. Eles podem distorcer análises estatísticas e, por isso, é importante identificá-los e, se necessário, removê-los. Abaixo, são apresentados dois métodos comuns para identificar e filtrar outliers: Z-score e IQR (Interquartile Range).
### Z-score
O Z-score mede a distância de um valor em relação à média, em termos de desvios padrão. Ele é útil para identificar outliers em distribuições aproximadamente normais.
#### Identificar outliers com Z-score:
```
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[z_scores >= 3]
```
#### Filtrar outliers com Z-score
```
df_score = df[(stats.zscore(df['idade']) < 3)]
```
### IQR
O IQR é a diferença entre o terceiro quartil (Q3) e o primeiro quartil (Q1) e captura a dispersão central de 50% dos dados. Valores que estejam 1,5 vezes o IQR abaixo do Q1 ou acima do Q3 são considerados outliers.
#### Identificar outliers com IQR
```
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q1 - Q3

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
```
#### Filtrar outliers em IQR
```
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]
```
