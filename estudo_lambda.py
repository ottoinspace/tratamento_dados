import pandas as pd


# Funcao para calcular o cubo de um numero
def eleva_cubo(x):
    return x ** 3


# Expressao de lambda para calcular o cubo de um número
eleva_cubo_lambda = lambda x : x ** 3

print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

df = pd.DataFrame({'numeros': [1, 2, 3, 4, 5, 10]})

df['cubo_funcao'] = df['numeros'].apply(eleva_cubo)
df['cubo_funcao'] = df['numeros'].apply(lambda x: x ** 3)
print(df)

