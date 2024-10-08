# %%
import pandas as pd

df = pd.read_excel("transactions.xlsx")
df
# %%
condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user["Points"].sum()
# %%
df.groupby(["IdCustomer"])["Points"].mean()
# %%
df.groupby(["IdCustomer"])["Points"].sum()

# %%
df_summary = df.groupby(["IdCustomer"])["Points"].sum()
df_summary.reset_index()
# %%
(df.groupby(["IdCustomer"])
    .agg({  
            "Points": 'sum', 
            "UUID": 'count',
            "DtTransaction": 'max',
          }
        )
    .reset_index()
    .rename(columns={
                        "Points": "Valor",
                        "UUID": "Frequencia",
                        "DtTransaction": "UltimaData"
                    }
            )
)
# %%
import datetime

data1 = df["DtTransaction"][0]
now = datetime.datetime.now()

(now - data1).days
# %%
datetime.datetime.now() - df["DtTransaction"][0]
# %%
df
# %%
condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user
diff = datetime.datetime.now() - df_user["DtTransaction"].max()
diff.days
# %%
def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days

(df.groupby(["IdCustomer"])
    .agg({  
            "Points": 'sum', 
            "UUID": 'count',
            "DtTransaction": ['max', recencia]
          }
        )
    .reset_index()
    .rename(columns={
                        "Points": "Valor",
                        "UUID": "Frequencia",
                        "DtTransaction": "UltimaData"
                    }
            )
)
# %%
