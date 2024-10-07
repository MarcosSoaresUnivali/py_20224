# %%
# Importing Pandas lib


import pandas as pd

# %%
# Set a dictionary


data = {
    "nome":["mps", "juh", "mar"],
    "sobrenome":["soar", "sant", "ares"],
    "idade":[47, 25, 37]
}
data


# %%
# Get 1st idade from data


data["idade"][0]


# %%
# Changing to Dataframe

df = pd.DataFrame(data)
df

# %%
# Get 1st idade from df


df["idade"].iloc[0]


# %%
# Check df column as Pandas Series


type(df["idade"])


# %%
# Get 1st sobrenome from df


df["sobrenome"].iloc[0]



# %%
# Getting 1st row of df (Pandas Series)

df.iloc[0]
type(df.iloc[0])

# %%

df.index
# %%

df.columns
# %%
# Info Method


df.info(memory_usage='deep')

# %%
# dtypes Attributes

df.dtypes


# %%
# Adding new column to df


df['peso'] = [90, 100, 66]

df.describe()


# %%
# Creating new df from another (Pandas describe method)


sumario = df.describe()
sumario['peso']['mean']


# %%
# Getting the head n rows

df.head(2)


# %%
# Getting the tail n rows

df.tail(1)


# %%
