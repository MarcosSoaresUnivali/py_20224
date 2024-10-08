# %%
# Import data from csv...


import pandas as pd

df = pd.read_csv("customers.csv", sep=';')
df
# %%
df.dtypes
# %%
df['Points'].astype(str)

# %%
