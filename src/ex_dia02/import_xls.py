# %%
# Import data from csv...


import pandas as pd

df_transactions = pd.read_excel("transactions.xlsx")
df_transactions
# %%

df_transactions.shape
# %%

df_transactions.head()
# %%

df_transactions.tail()
# %%
colunas = ['UUID',
            'Points',
            'IdCustomer',
            'DtTransaction']
df_transactions = df_transactions[colunas]
# %%
df_transactions

# %%
df_transactions.info(memory_usage='deep')
# %%
