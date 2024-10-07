# %%
# Import data from csv...


import pandas as pd

df_products = pd.read_csv("products.csv", sep=';', names=["Id","Name","Description"])
df_products

# %%

df_products.rename(columns={"Name":"Nome", "Description":"Descricao"}, inplace=True)
df_products
# %%
