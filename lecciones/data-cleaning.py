# %% [markdown]
# # pandas dataframes

# %%
import pandas as pd

data = pd.read_csv('../datasets/titanic/titanic3.csv')
data.head()

# %%
len(data)
data.shape
data.tail
data.columns

# %%
data.describe()

# %%
data.dtypes
# markdown
# Missing values

# %%
# pd.isnull(data["body"])
pd.notnull(data["body"])

# %%
# values, regresa un arreglo, ravel construye un unico array
pd.isnull(data["body"]).values.ravel().sum()

# %% [markdown]
# ## los valores que faltan en un dataset pueden venir por do razones:
# * Extracción de los datos
# * Recolección de los datos

# %% [markdown]
# ## Borrado de valores que faltan


# %%
# axis = 0 borra toda la fila
# axis = 1 borra toda la columna
# how = all borra el row si todas las columnas son NaN
data.dropna(axis=0, how="all")

# %% [markdown]
# ## Computo de valores faltantes

# %%
data3 = data
data.fillna(0)
data3.head()
# %%
data4 = data
data.fillna('desconocido')
data3.head()

# %%
data5 = data
data5['body'].fillna(0)
data5['home.dest'] = data5['home.dest'].fillna('desconocido')
data5.head(20)

# %%
pd.isnull(data5['age']).values.ravel().sum()

# %%
# ffill fortward fill - rellena con el valor adelante más cercano que encuenta al nan
# bgill backward fill - rellena con el valor anterior más cercano al nan
data5 = data3
print(data5['age'].head(17))
print(data5['age'].fillna(method='ffill').head(17))
print(data5['age'].fillna(method='bfill').head(17))
# %% [markdown]
# # Variables dummy

# %%
data['sex']

# %%
dummy_sex = pd.get_dummies(data['sex'], prefix='sex')
dummy_sex.head(20)

# %%
column_name = data.columns.values.tolist()
column_name

# %%
# borrar una columna
data.drop(['sex'], axis=1)

# %%
def createDummies(df, var_name):
    dummy = pd.get_dummies(df[var_name], prefix=var_name)
    df = df.drop(var_name, axis=1)
    df = pd.concat([df, dummy], axis=1)
    return df



# %%
createDummies(data3, "sex")

# %%
