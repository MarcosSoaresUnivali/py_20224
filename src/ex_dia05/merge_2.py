# %%
import pandas as pd

df = pd.read_csv("customers.csv", sep=';')
df
# %%

df_tr = pd.read_excel("transactions.xlsx")
df_tr

# %%

df_tr_prod = pd.read_parquet("transactions_cart.parquet")
df_tr_prod

# %%
df_join =   (  df_tr.merge(     df,
                                how="inner",
                                left_on="IdCustomer",
                                right_on="UUID",
                                suffixes=["_tr", "_cli"])
                    .merge(     df_tr_prod,
                                how="inner",
                                left_on="UUID_tr",
                                right_on="IdTransaction"
                    )
            )
df_join            
# %%
