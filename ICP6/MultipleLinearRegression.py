import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


train = pd.read_csv('train.csv')

train.SalePrice.describe()

plt.scatter(train['GarageArea'],train['SalePrice'])

plt.show()


from scipy import stats

df = train.drop(train[train['GarageArea']>1200].index)
plt.scatter(df['GarageArea'].values,df['SalePrice'].values)
plt.show()

