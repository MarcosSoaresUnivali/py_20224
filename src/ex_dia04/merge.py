# %%
import pandas as pd

data_users = {
    "id": [1,2,3,4],
    "nome": ["Teo","Mat","Nah","Mah"],
    "idade": [31,31,32,32]

}

df_users = pd.DataFrame(data_users)
df_users

# %%

data_transacoes = {
    "id_user": [1,1,1,2,3,3],
    "vl": [432,532,123,6,4,87],
    "qtProdutos": [2,1,3,6,10,2]
}


df_transacoes = pd.DataFrame(data_transacoes)
df_transacoes
# %%
df_transacoes.merge(df_users, 
                    how="left", 
                    left_on="id_user", 
                    right_on="id"
                    )
# %%
