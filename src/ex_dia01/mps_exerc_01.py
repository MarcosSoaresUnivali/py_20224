# %%
# Exercicio 01 - Creating simple list


lista = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
lista


# %%
# Exercicio 01 - Converting simple list to Pandas Series


import pandas as pd

serie = pd.Series(lista)
serie


# %%
# Exercicio 01 - Get mean, var and max

serie.max()


# %%

serie.mean()

# %%

serie.std()
# %%
