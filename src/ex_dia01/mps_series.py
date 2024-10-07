# %%
# Importing pandas lib

import pandas as pd


# %%
# Creating Simple List

idades = [30, 42, 90, 34]
idades


# %%
# Calculating mean and variance

media = sum(idades) / len(idades)


total = 0
for i in idades:
    total += (media - i)**2

variancia = total / (len(idades) - 1)
variancia


# %%
# Creating Pandas Series

series_idades = pd.Series(idades)
series_idades


# %%
# Calculating mean (by Pandas) 

series_idades.mean()


# %%
# Calculating variance (by Pandas)

series_idades.var()



# %%
# Showing main desc calculations (by Pandas)

series_idades.describe()


# %%
# Calculating median (by Pandas) 

series_idades.median()


# %%
# Showing shape

series_idades.shape


# %%
# Get pos/index element from List 

idades[0]


# %%
# Get pos/index element from Pandas Series

series_idades[0]
# %%
# Changing index of Pandas Series

series_idades.index = ['m','p','s','l']


# %%
# Get index element from Pandas Series

series_idades['l']


# %%
# Show all index changed

series_idades


# %%
# Get ***position element from Pandas Series

series_idades.iloc[0:3]


# %%
# Get ***index element from Pandas Series


series_idades.loc['l']


# %%
# Set name of Pandas Series


series_idades.name = 'idades'
series_idades
# %%
