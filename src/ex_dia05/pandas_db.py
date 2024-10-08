# %%

import pandas as pd
import sqlalchemy


# %%
engine = sqlalchemy.create_engine("sqlite:///database.db")
engine
# %%
pd.read_sql_table("customers", engine)
# %%
