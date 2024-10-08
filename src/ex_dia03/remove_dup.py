# %%
import pandas as pd

data = {
    "Nome": ["mps", "paula", "luis", "joice", "mps", "paula"],
    "Idade": [47,27,17,37,7,47],
    "update_at": [1,2,3,1,2,3]
}

df = pd.DataFrame(data)
df
# %%
df = (df.sort_values(by="update_at", ascending=False)
        .drop_duplicates(subset="Nome", keep="first")
)
df
# %%
