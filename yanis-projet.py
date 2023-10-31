import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tesla.csv', index_col='Date')

df.head(5)

for c in ['Close/Last', 'Open', 'High', 'Low']:
    df[c] = df[c].str.replace('$','')
    df[c] = df[c].astype(float)

df

# +

df['High'].plot()

# +
df.drop(labels = 'Volume', axis = 1, inplace= True)


# -

df['High'].plot()

rolling = df['High'].rolling(window=30,center=True).mean()

rolling.plot()
